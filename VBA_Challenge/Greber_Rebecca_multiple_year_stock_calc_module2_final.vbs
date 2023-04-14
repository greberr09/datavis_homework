Sub CalcPriceChange()

Dim ws As Worksheet   ' In my version of VBA, this is needed or ws is undefined

    ' --------------------------------------------
    ' Loop through each of the worksheets
    ' --------------------------------------------
    For Each ws In ThisWorkbook.Worksheets
    ws.Activate  ' this is necessary to keep the updates in the proper worksheet
    
        ' A few messaging statements were left in to be uncommented if wanted
        ' especially to see the changes to the next worksheet
          
        Dim WorksheetName As String
        ' MsgBox (ws.Name)
        
        WorksheetName = ws.Name
        ' MsgBox ("This is the " + WorksheetName + " worksheet")
        
        ' Get the last row number
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        ' MsgBox ("last row is " + Str(LastRow))

        ' ----------------------------------------
        ' Insert four new columns for
        ' ticker, yearly change, % change, and total volume
        ' ----------------------------------------
        
        ws.Range("I1:l1").EntireColumn.Insert
        
        ' ----------------------------------------
        ' Title the columns and set widths
        ' ----------------------------------------
        ws.Cells(1, 9).Value = "Ticker"
        
        ws.Cells(1, 10).Value = "Yearly_Change"
        Columns(10).ColumnWidth = 12
        
        ws.Cells(1, 11).Value = "Percent_Change"
        Columns(11).ColumnWidth = 13
        
        ws.Cells(1, 12).Value = "Total_Stock_Volume"
        Columns(12).ColumnWidth = 17
        
        '------------------------------------------
        ' Add the total fields for tickers with largest overall
        ' yearly change, percent change, and total volume for the sheet
        '------------------------------------------
        
        Cells(1, 15).Value = "Ticker"
        Cells(1, 16).Value = "Value"
        Cells(2, 14).Value = "Greatest % Increate"
        Cells(3, 14).Value = "Greatest % Decrease"
        Cells(4, 14).Value = "Greatest Total Volume"
        Columns(14).ColumnWidth = 21
        
        ' Set an initial variable for holding the name of the stock
        Dim ticker As String
        ticker = ""
        
        ' Create a counter for the range of a particular symbol
        Dim start_row As Long
        start_row = 2

        ' Set initial variables for determing the highest and lowest price per ticker
        Dim ticker_open, ticker_close As Double
        ticker_open = 0
        ticker_close = 0
        
        ' Set variables to calculate total volume
        Dim total_volume As Double
        total_volume = 0

        ' Track row in the summary table for this ticker symbol
        Dim Summary_Table_Row As Long
        Summary_Table_Row = 2      'to account for the first row holding the column names

        '-----------------------------------------------
        ' Loop through all of the rows in the worksheet
        '-----------------------------------------------
        
        For i = 2 To LastRow

            ' Check if this is the same stock symbol
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

                ' If the end of the rows for a ticker, set the ticker symbol
                ticker = Cells(i, 1).Value
                
                '-----------------------------------------------
                ' Get the opening price for the first date and the closing price for last date.
                ' This assumes that the data are in ascending order by date for each ticker,
                ' because in examining this data, that appears to be true.  If the data were
                ' not ordered by date for each ticker, a lot more calculation would
                ' be necessary to get the first date for the ticker and the last date
                ' for that ticker.
                '-----------------------------------------------

                ticker_open = Cells(start_row, 3)
                ticker_close = Cells(i, 6)
            
                ' Add to the total volume for this stock
                 total_volume = total_volume + Cells(i, 7).Value
                       
                ' Print the stock symbol in the Summary Table
                Range("I" & Summary_Table_Row).Value = ticker
                
                ' Calculate and print the yearly change in the Summary Table
                ' The formatting method was suggested by multiple Google searches
                Range("J" & Summary_Table_Row).Value = ticker_close - ticker_open
                Range("J" & Summary_Table_Row).NumberFormat = "$#,##0.00"
                  
                ' Calculate and print the percent change in the Summary Table
                ' Because the formatting as percent multiplies value times 100,
                ' that is left out of the calculation itself.
                Range("K" & Summary_Table_Row).Value = (ticker_close - ticker_open) / ticker_open
                Range("K" & Summary_Table_Row).NumberFormat = "0.00%"
                
                ' Color the columns appropriately, green or red
                If (ticker_close - ticker_open) > 0 Then
                    Range("J" & Summary_Table_Row).Interior.ColorIndex = 4
                    Range("K" & Summary_Table_Row).Interior.ColorIndex = 4
                Else
                    Range("J" & Summary_Table_Row).Interior.ColorIndex = 3
                    Range("K" & Summary_Table_Row).Interior.ColorIndex = 3
                End If
                
                ' Print the total sales volume for this stock in the Summary Table
                 Range("L" & Summary_Table_Row).Value = total_volume
                 Range("L" & Summary_Table_Row).NumberFormat = "$#,##0"

                ' Increment the summary table row and the ticker start row
                Summary_Table_Row = Summary_Table_Row + 1
                start_row = i + 1
      
                ' Reset the stock totals
                ticker_open = 0
                ticker_close = 0
                total_volume = 0
                ticker = ""

        ' If the cell immediately following a row is the same stock symbol
        Else
                ' Add to the total volume for this stock
                total_volume = total_volume + Cells(i, 7).Value

        End If

      Next i
      
      '-----------------------------------------------
      ' Calculate and prting the totals for the sheet
      ' Greatest increase, decrease, and highest volume
      '-----------------------------------------------
      
       ' Create variables to use in calculating the maximum

        Dim max_increase, min_increase, max_vol As Double
        max_increase = 0
        max_decrease = 0
        max_vol = 0
         
        Dim cntr As Long
        cntr = 0

        Dim max_ticker, min_ticker, vol_ticker As String
        
        ' Get the maximum increase from the summary table
        max_increase = Application.WorksheetFunction.Max(Range("K2:K" & Summary_Table_Row))
        
        
        ' Get the ticker symbol for this max.
        ' This is used because a vlookup needs the first column to be the key, and here we are
        ' trying to get the ticker in the first column from a value in another column.
        ' This works equally well with the loop below or with the Match function.  I tried
        ' both to see if one was notably faster than the other.  It would seem that the Match function
        ' should be faster as it is searching an array and returning the value when found, but no difference
        ' was apparent just by simple observation without measuring tools.  The Match function  is more
        ' sensitive to data being invalid or missing, and will return an error that has to be handled, so that
        ' would add more coding.  In our spreedsheets for this module, the data are all present and in the proper
        ' type, so this runs smoothly here but otherwise as the error handling was not coded, ultimately
        ' I decided for this purpose the loop would be more robust in case someone inadvertently wipes out part of
        ' the data in the spreadsheet.

        For cntr = 2 To Summary_Table_Row
            If (Cells(cntr, 11).Value = max_increase) Then
              max_ticker = Cells(cntr, 9).Value
            End If
        Next cntr
        
        '  Alternative printing method
        ' The commented out code was run for all of the spreadsheets, with additional cell printing, to test the results
        ' The two methods produced the same values
        '
        ' Dim test_ticker As String
        ' test_ticker = ""
        ' Dim test_counter As Integer
        ' test_counter = 0
        ' test_counter = Application.WorksheetFunction.Match(max_increase, Range("K2:K" & Summary_Table_Row), 0)
        ' test_counter = test_counter + 1   ' to account for zero-based array
        ' test_ticker = Cells(test_counter, 9)
    
        
        ' Get the maximum decrease from the summary table
        ' The maximum decrease will be the minimum value of the changes
        max_decrease = Application.WorksheetFunction.Min(Range("K2:K" & Summary_Table_Row))
        
      ' Get the ticker symbol for this maximum decrease
        For cntr = 2 To Summary_Table_Row
            If (Cells(cntr, 11).Value = max_decrease) Then
              min_ticker = Cells(cntr, 9).Value
            End If
        Next cntr
        
        ' alternative getting ticker method
        ' test_counter = Application.WorksheetFunction.Match(max_decrease, Range("K2:K" & Summary_Table_Row), 0)
        ' test_counter = test_counter + 1
        ' test_ticker = Cells(test_counter, 9)

        ' Calculate the maximum volume and get associated ticker
        max_vol = Application.WorksheetFunction.Max(Range("L2:L" & Summary_Table_Row))
        
        For cntr = 2 To Summary_Table_Row
            If (Cells(cntr, 12).Value = max_vol) Then
              vol_ticker = Cells(cntr, 9).Value
            End If
        Next cntr
        
        ' alternative getting ticker method
        ' test_counter = Application.WorksheetFunction.Match(max_vol, Range("L2:L" & Summary_Table_Row), 0)
        ' test_counter = test_counter + 1
        ' test_ticker = Cells(test_counter, 9)
        
        '--------------------------------------
        ' Print the calculated values
        '--------------------------------------
        
        ' Print the highest percent change
        Cells(2, 15).Value = max_ticker
        Cells(2, 16).Value = max_increase
        Cells(2, 16).NumberFormat = "0.00%"
        
        ' Print the maximum decrease in value
        Cells(3, 15).Value = min_ticker
        Cells(3, 16).Value = max_decrease
        Cells(3, 16).NumberFormat = "0.00%"
        
        ' Print the highest volume
        Cells(4, 15).Value = vol_ticker
        Cells(4, 16).Value = max_vol
        Cells(4, 16).NumberFormat = "$#,##0"
        
    '--------------------------------------
    ' get next worksheet worksheet
    '--------------------------------------
    Next ws

End Sub
