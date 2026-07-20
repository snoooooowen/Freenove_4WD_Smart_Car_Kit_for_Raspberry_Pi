from motor import Ordinary_Car
import time
PWM = Ordinary_Car()          

try:
    while True:
        direction = input("Enter direction (w/a/d/s/e/q/r): ")
        if direction == "w":
            PWM.set_motor_model(-2000,-2000,-2000,-2000)       #Forward
        if direction == "s":
            PWM.set_motor_model(2000,2000,2000,2000)   #Back
        if direction == "a":
            PWM.set_motor_model(2000,-2000,-2000, 2000)     #slide Left 
        if direction == "d":
            PWM.set_motor_model(-2000,2000,2000,-2000)       #slide right
        if direction == "e":
            PWM.set_motor_model(2000,2000,-2000,-2000)     #turn left
        if direction == "q":
            PWM.set_motor_model(-2000,-2000,2000,2000)     #turn Right    
        if direction == "r":
            PWM.set_motor_model(0,0,0,0)                   #Stop
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    print ("\nEnd of program")
finally:
    PWM.close()

