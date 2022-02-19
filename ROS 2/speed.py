import time
import serial
ser = serial.Serial('COM5', 9600, timeout=1)

while True:
    print("forward")
    ser.write(b'w')
    time.sleep(2.5)