import time
from motor import Ordinary_Car
PWM = Ordinary_Car()

def drive_by_time():
    PWM = Ordinary_Car()

def TL():
    print("turning left")
    PWM.set_motor_model(1000, 1000, -1000, -1000)
    time.sleep(0.37) #around 0.33 should be 90 degree turn

def TR():
    print("turning right")
    PWM.set_motor_model(-1000, -1000, 1000, 1000)
    time.sleep(0.4)

def fwd(): 
    print("moving forward")
    PWM.set_motor_model(-750, -750, -750, -750)
    time.sleep(1)
def f():
    print("moving fast")
    PWM.set_motor_model(-1600,-1600,-1500,-1500)
    time.sleep(2)
def Bk():
    print("backing up")
    PWM.set_motor_model(750, 750, 750, 750)
    time.sleep(1)

def stop():
   print("stopping")
   PWM.set_motor_model(0, 0, 0, 0)
   time.sleep(0.5)

def T180():
     print("turning 180")
     PWM.set_motor_model(1000,1000,-1000,-1000)
     time.sleep(0.688) 
try:
    f()
    f()
    f()

except KeyboardInterrupt:
        print("Program interrupted by user.")
        
finally:
        print("finished")
        PWM.set_motor_model(0, 0, 0, 0) 

if __name__ == '__main__':
    drive_by_time()