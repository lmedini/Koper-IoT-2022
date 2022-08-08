import serial
import time
import my_client as my_client
import step_counter

ser = None

SCAL = 9  # scale the number of steps (5s measurements) to steps per minute


def setup():
    global ser
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('/dev/ttyACM0', 9800, timeout=1)
    for t in range(200):
        line = ser.readline()   # throw away first line

# delta is the number of seconds to report


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


def record_data():
    while True:
        line = ser.readline()   # read a byte
        if len(line) > 2:
            # convert the byte string to a unicode string
            string = line.decode().rstrip('\r\n')
            #counts = string.split(",")
            print(string)
    ser.close()

 # report every 5 seconds and report in steps per minute


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
                c += 2
                print("Step number: ", c)
        end = time.time()
        if end - start > 5:
            start = time.time()
            c = c * SCAL  # convert in steps per minute should be 11 for maximum
            print("Steps per minute: ", c)
            my_client.put_activity(c)
            c = 0


if __name__ == "__main__":
    setup()
    # activity_detection(5)
    # record_data()
    count_steps()
