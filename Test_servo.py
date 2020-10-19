import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

print("\n+----------/ ServoMoteur  Controlleur /----------+")
print("|                                                |")
print("| Le Servo doit etre branche au pin 11 / GPIO 17 |")
print("|                                                |")
print("+------------------------------------------------+\n")


#angle = 90
duree = 0.04

pwm=GPIO.PWM(17,100)
pwm.start(5)

i = 0
#angleChoisi = angle/10 + ajoutAngle

pwm.ChangeDutyCycle(20)
time.sleep(0.1)
pwm.stop()
GPIO.cleanup()