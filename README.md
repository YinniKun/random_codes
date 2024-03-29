# Random Code Repository

**Author:** Richard Dong

**Last Update:** December 30, 2023

This repository contains codes for a variety of automation that I make to make my life better, as well as some fun side projects that I did.

All codes should be able to run within the terminal. To run the code you desire, go to the corresponding directory and run ``python3 main.py``. To see the parameters required, use the ``-h`` flag.

Please ensure you have python 3.9+ to run all the codes.

## Descriptions by Proragms

**date_generation**: Generates all the dates with day of the week for a given period of time

**task_manager**: Automatically let you see the tasks that you should be doing today, based on your availability, the due date, and the time commitment for the tasks.

**health_data_plot**: Plots the health data stored in a csv file.

**fft_pic**: Plot the FFT of your favourite song - why listen to it when you can SEE it! (Work in progress)


## Dependencies by Programs

All programs will require ``argparse`` to run. In addition to ``argparse``, please ensure you have the folloing modules ready for the corresponding program:

**date_generation**
- datetime
- dateutil.relativedelta

**task_manager**
- os
- datetime
- dateutil.relativedelta

**health_data_plot**
- matplotlib.pyplot
- csv
- sklearn
- numpy

**fft_pic**
- matplotlib.pyplot
- numpy
- scipy,io
