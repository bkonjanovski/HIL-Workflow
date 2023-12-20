import serial
import time
import RPi.GPIO as GPIO

ser = serial.Serial('/dev/ttyACM0', 115200)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17, GPIO.LOW)
 
#def echo_serial(input: bytes):
#       if not isinstance(input, (bytes)) or len(input) != 1:  
#                raise TypeError("Input must be a single byte")  
#        ser.write(input)
#        res = ser.read(1)
#        return res.decode()

def check_gpio_signal(): 
    GPIO.output(17, GPIO.HIGH)
    res = ser.read(7)
    return res.decode()

