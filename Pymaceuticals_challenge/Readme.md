

This challenge uses Jupyter notebook, matplotlib, numpy, scipy, and Pandas plotting. It also uses "random" and "string."

The code takes in two input csv files, located in the "data" folder, "Mouuse_metadata.csv" and "Study_results.csv". The code optionally prints out the cleaned and merged data into an "output" directory, to a file called "cleaned_mice_csv." This file will be created if it does not exist, or overwritten if it does exist, but the directory must exist for the output to be written. A flag (currently set o "N"), controls whether the output is written or not.

A separate flag, currently set to "Y", controls whether a single mouse is chosen randomly or whether to use a hard-coded single mouse ID that is set in the code. These are not currently set as user input flags, so the flag variable has to be changed manually. Accepting user inputs would be an enhancement but would preclude "running all" without input.

This study was requested by Pymaceuticals, Inc., from one of its senior data scientists. The study examined a number of metrics to try to determine the relative efficacy of ten drug regimens that are intended to treat a very common form of skin cancer. The purpose of this study was to compare results from pPymaceuticals’ drug, Capomulin, with the nine other treatment regimens.

The study began with 249 mice and ran for 45 days. Weights of tumors were observed and measured at intervals throughout the study. Some mice did not survive for the 45 days.

The executives at Pymaceuticals requested certain tables and figures for a technical report on the clinical study, and have also asked for a top-level summary of the study results.

The analysis included examing mean, median, variance, standard deviation, and standard err for the tumor sizes of mice being treated with each of the ten drug regimens. The analysis also includeed bar, line, pie, and scatter plots to compare number of observations per drug regimen, the number of male and female mice, tumor size over time for an individual mouse, and tumor size to mouse weight.

All of the plots are included in this Jupyter notebook.
