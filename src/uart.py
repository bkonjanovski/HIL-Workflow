import serial
import time
import RPi.GPIO as GPIO
from rpi_hardware_pwm import HardwarePWM

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
    ser.flush()
    time.sleep(3)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(3)
    res = ser.read(7)
    return res.decode()
    GPIO.output(17, GPIO.LOW)

def check_pwm_signal(): 
	pwm = HardwarePWM(pwm_channel=0, hz=500)
	pwm.start(50) 
	time.sleep(10)
	res = ser.read()
	return res.decode()
	pwm.stop()




