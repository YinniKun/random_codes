# Random Code Repository

This repository contains codes for a variety of automations that I make to make my life better.

All codes should be able to run within the terminal. To run the code you desire, go to the corresponding directory and run ``python3 main.py``. To see the parameters required, use the ``-h`` flag.

## Descriptions by Proragms

**date_generation**: Generates all the dates with day of the week for a given period of time

**task_manager**: Automatically let you see the tasks that you should be doing today, based on your availability, the due date, and the time commitment for the tasks. (Work in progress)


## Dependencies by Programs

All programs will require ``argparse`` to run. In addition to ``argparse``, please ensure you have the folloing modules ready for the corresponding program:

**date_generation**
- argparse
- datetime
- dateutil.relativedelta

**task_manager**
Work in progress
