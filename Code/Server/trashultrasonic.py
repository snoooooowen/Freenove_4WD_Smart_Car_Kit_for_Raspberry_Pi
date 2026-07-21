from ultrasonic import Ultrasonic
from motor import Ordinary_Car
import time

PWM = Ordinary_Car()
dist_sensor = Ultrasonic()

try:
    while True:
        dist = dist_sensor.get_distance()
        print(f"current distance is {dist} cm")

        time.sleep(0.01)

        if dist <= 3:
            print("stopping")
            PWM.set_motor_model(0, 0, 0, 0)
            time.sleep(0.5)

except KeyboardInterrupt:
    Ultrasonic.close()
    print("\nEnd of program")
