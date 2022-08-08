"""
  Author: Niki Hrovatin
  e-mail: niki.hrovatin@famnit.upr.si
  Date: 08.08.2022
  Activity detector developed on the workshop Koper-IoT-2022 held at InnoRenewCoe in Izola.
"""

import serial
import time
import my_client as my_client
import step_counter

ser = None  # serial communication


def setup():
    global ser
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('/dev/ttyACM0', 9800, timeout=1)
    for t in range(200):
        line = ser.readline()   # throw away first line


"""
Uses step_counter.py to count the number of steps
Reports steps per minute on 5s interval
"""

# scale the number of steps (5s measurements) to steps per minute, should be 11
SCAL = 9
# set to 9 to have the number of steps in the range 0 - 100


def count_steps():
    global SCAL
    detector = step_counter.Detector()
    c = 0
    start = time.time()
    while True:
        line = ser.readline()   # read a byte
        if len(line) > 2:
            string = line.decode().rstrip('\r\n')
            counts = string.split(",")
            rear = int(counts[1])  # only rear sensor
            if detector.detect(rear):
                c += 2  # each detection is 2 steps, since the sensor is on one shoe
                print("Step number: ", c)
        end = time.time()
        if end - start > 5:
            start = time.time()
            c = c * SCAL
            print("Steps per minute: ", c)
            my_client.put_activity(c)  # send steps to the server
            c = 0


"""
testing function
delta is the number of seconds to report
"""


def activity_detection(delta):
    global ser
    while True:
        tot_counts = 0
        for t in range(100*delta):
            line = ser.readline()   # read a byte
            if len(line) > 2:
                # convert the byte string to a unicode string
                string = line.decode().rstrip('\r\n')
                counts = string.split(",")
                if int(counts[0]) > 1:
                    tot_counts = tot_counts + 1
                if int(counts[1]) > 1:
                    tot_counts = tot_counts + 1
        print(tot_counts)
        my_client.put_activity(tot_counts)
    ser.close()


"""
Used to record data for analysis
"""


def record_data():
    while True:
        line = ser.readline()   # read a byte
        if len(line) > 2:
            # convert the byte string to a unicode string
            string = line.decode().rstrip('\r\n')
            #counts = string.split(",")
            print(string)
    ser.close()


if __name__ == "__main__":
    setup()
    # activity_detection(5)
    # record_data()
    count_steps()
