## plotting for a particular workout
## Works best if using the Auto Export program to export data stored in Apple Watch

import argparse
import matplotlib.pyplot as plt
import csv

## Define some indeces
workout = 0
date = 1
duration = 3
total_energy = 4
max_heart_rate = 6
avg_heart_rate = 7
distance = 8
avg_speed = 9


def main():
    print("======Start Running the Plotting Program=====")
    L = []
    with open(args.file) as f:
        next(f)
        csv_file = csv.reader(f)
        for row in csv_file:
            if row[workout] == args.workout:
                L.append(row)
    start_date = L[-1][date].split(" ")[0]
    # Plot heart rate data
    if args.heartrate:
        fig,ax = plt.subplots()
        ax.set_xlabel(f"Number of workout since {start_date}")
        ax.set_ylabel("Heart rate in bpm")
        max_hr = []
        avg_hr = []
        for each in L:
            try:
                max_hr.append(float(each[max_heart_rate]))
                avg_hr.append(float(each[avg_heart_rate]))
            except:
                pass
        number_max = list(range(1,len(max_hr)+1))
        number_avg = list(range(1,len(avg_hr)+1))
        ax.plot(number_max,max_hr[::-1],marker=".",markerfacecolor='blue',linestyle="-",color="blue",label="Maximum Heart Rate")
        ax.plot(number_avg,avg_hr[::-1],marker=".",markerfacecolor='red',linestyle="-",color="red",label="average Heart Rate")
        ax.legend(loc="best")
        ax.set_title(f"Heart Rate for {args.workout} starting from {start_date}")
        plt.savefig(f"Heart Rate for {args.workout} starting from {start_date}.pdf")
        print("Plot for heart rate is saved!")
    # Plot for energy
    if args.energy:
        fig,ax = plt.subplots()
        ax.set_xlabel(f"Number of workout since {start_date}")
        ax.set_ylabel("Energy in kJ")
        energy = []
        for each in L:
            try:
                energy.append(float(each[total_energy]))
            except:
                pass
        number_energy = list(range(1,len(energy)+1))
        ax.plot(number_energy,energy[::-1],marker=".",markerfacecolor='blue',linestyle="-",color="red",label="Maximum Heart Rate")
        ax.set_title(f"Total Energy for {args.workout} starting from {start_date}")
        plt.savefig(f"Total Energy for {args.workout} starting from {start_date}.pdf")
        print("Plot for energy is saved!")
    # Plot for distance
    if args.distance:
        fig,ax = plt.subplots()
        ax.set_xlabel(f"Number of workout since {start_date}")
        ax.set_ylabel("Distance in km")
        dis = []
        for each in L:
            try:
                dis.append(float(each[distance]))
            except:
                pass
        number_dis = list(range(1,len(dis)+1))
        ax.plot(number_dis,dis[::-1],marker=".",markerfacecolor='blue',linestyle="-",color="red",label="Maximum Heart Rate")
        ax.set_title(f"Distance for {args.workout} starting from {start_date}")
        plt.savefig(f"Distance for {args.workout} starting from {start_date}.pdf")
        print("Plot for distance is saved!")
    # Plot for speed
    if args.speed:
        fig,ax = plt.subplots()
        ax.set_xlabel(f"Number of workout since {start_date}")
        ax.set_ylabel("Speed in km/h")
        spd = []
        for each in L:
            try:
                spd.append(float(each[avg_speed]))
            except:
                pass
        number_spd = list(range(1,len(spd)+1))
        ax.plot(number_spd,spd[::-1],marker=".",markerfacecolor='blue',linestyle="-",color="red",label="Maximum Heart Rate")
        ax.set_title(f"Speed for {args.workout} starting from {start_date}")
        plt.savefig(f"Speed for {args.workout} starting from {start_date}.pdf")
        print("Plot for energy is saved!")
    # Plot for duration
    if args.duration:
        fig,ax = plt.subplots()
        ax.set_xlabel(f"Number of workout since {start_date}")
        ax.set_ylabel("Duration in minutes")
        factors = (60, 1, 1/60)
        dur = []
        for each in L:
            my_time = each[duration]
            try:
                time = sum(i*j for i, j in zip(map(int, my_time.split(':')), factors))
                dur.append(float(time))
            except:
                pass
        number_dur = list(range(1,len(dur)+1))
        ax.plot(number_dur,dur[::-1],marker=".",markerfacecolor='blue',linestyle="-",color="red",label="Maximum Heart Rate")
        ax.set_title(f"Duration for {args.workout} starting from {start_date}")
        plt.savefig(f"Duration for {args.workout} starting from {start_date}.pdf")
        print("Plot for duration is saved!")
    print("======Finish Running the Plotting Program=====")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    description = 'Plots your desired workout information over a period of time from a csv.')
    parser.add_argument("-w", "--workout", default = "Swimming",
                        help="The name of the workout. Default is Swimming")
    parser.add_argument("-f", "--file",
                        help="The name of the csv file.")
    parser.add_argument("-hea", "--heartrate", action=argparse.BooleanOptionalAction,
                        help="Plotting your heartrate data or not")
    parser.add_argument("-ene", "--energy", action=argparse.BooleanOptionalAction,
                        help="Plotting your energy data or not")   
    parser.add_argument("-dis", "--distance", action=argparse.BooleanOptionalAction,
                        help="Plotting your distance data or not")
    parser.add_argument("-spd", "--speed", action=argparse.BooleanOptionalAction,
                        help="Plotting your speed data or not")  
    parser.add_argument("-dur", "--duration", action=argparse.BooleanOptionalAction,
                        help="Plotting your duration data or not")                 
    args = parser.parse_args()
    main()
