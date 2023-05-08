This challenge uses Pandas and Jupyter Notebook to analyze statistical data about the schools in a city's school district.  The report is intended to help the school board and the mayor in making strategic decisions concerning future school budgets and priorities.

The code was based on a jupyter notebook script that was provided, which set out the overall general layout required, and provided a number of formulas to be used in calculating certain metrics.  That is generally indicated in comments within the code.  Slack Overflow and chatGPT were consulted quite a number of times, generally for debugging and for using certain function calls.   Information about comparable school district statistics in other districts was gleaned, as noted, from the school districts or cities, and from school association organizations.

## Data

The analysis is based on two sets of inputs, one with data for the schools themselves, including the number of students in the school, the school budget, and the school type, and one with information about each high school student in the district, including student name, ID, gender, school name, grade, and math and reading scores on standardized tests.  For this project, the raw data is stored in two csv files, "schools_complete.csv" and "students_complete.csv", in the "Resources" folder.  All of the outputs are interactive while running the Jupyter Notebook, and no output files are created other than in the updated Jupyter Notebook file, "PyCitySchools.ipynb."

## Dependencies

To run the code requires that the Pandas library be installed, as well as Juypter Notebook, and a working environment exists.  The code was not tested using Kaggle, and the dependencies or paths might require some tweaking to run that way.

## Method

The analysis proceeded by first merging the two sets of data into one combined file, and calculating various statistics to produce key metrics at the school district level.  The analysis proceeded by examining the same sets of metrics in a number of different aggregate groupings.  Aggregate metrics were created for each school; for each grade, district-wide; by the amount of spending for each school; based on the size of the school compared to other schools in the district; and based on the different school types, district_wide.  
