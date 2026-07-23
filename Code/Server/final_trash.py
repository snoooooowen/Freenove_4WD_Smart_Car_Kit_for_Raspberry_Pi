from motor import Ordinary_Car
from infrared import LineSensor
from infrared import Infrared
import time
from gpiozero import DistanceSensor, PWMSoftwareFallback, DistanceSensorNoEcho
import warnings
from ultrasonic import Ultrasonic


PWM = Ordinary_Car()
sensors = Infrared()


def T180():
     print("turning 180")
     PWM.set_motor_model(1000,1000,-1000,-1000)
     time.sleep(0.688) 

def avoid_obstacle():
    print("Avoiding obstacle...")
    # Stop
    PWM.set_motor_model(0, 0, 0, 0)
    time.sleep(0.5)

    # slide lefy
    PWM.set_motor_model(600, -600, -600, 600)
    time.sleep(1)

    # Drive past the obstacle
    PWM.set_motor_model(-600, -600, -600, -600)
    time.sleep(1.3)

    #slide right
    PWM.set_motor_model(-600, 600, 600, -600)
    time.sleep(1)

    # Stop briefly before resuming line following
    PWM.set_motor_model(0, 0, 0, 0)
    time.sleep(0.3)

    print("Obstacle avoided.")


if __name__ == '__main__':
    try:
        with Ultrasonic() as ultrasonic:
            # Continuously read and print the combined value of all infrared sensors
            while True:
                distance = ultrasonic.get_distance()
                print(f"Ultrasonic distance: {distance}cm")
                time.sleep(0.01)

                infrared_value = sensors.read_all_infrared()
                print(f"Infrared value: {infrared_value}")
                time.sleep(0.01)

                # Obstacle detected
                if distance is not None and distance <= 20:
                    PWM.set_motor_model(0, 0, 0, 0)

                    while True:
                        choice = input(
                            "\nObstacle detected!\n"
                            "Type 'move' to go around it\n"
                            "Type 'goal' if this is the destination and you would like to turn around\n> "
                            "Type 'done' if you are done"
                        ).strip().lower()

                        if choice == "move":
                            avoid_obstacle()
                            break      # Continue line following

                        elif choice == "done":
                            print("finished")
                            PWM.set_motor_model(0, 0, 0, 0)
                            sensors.close()
                            PWM.close()
                            exit()

                        elif choice == "goal":
                            print("turning around")
                            T180()
                            break

                        else:
                            print("Invalid input. Please type 'move', 'goal' or 'done'.")

                elif infrared_value == 6:
                    print("far right")
                    PWM.set_motor_model(-700, -700, 500, 500)

                elif infrared_value == 3:
                    print("far left")
                    PWM.set_motor_model(500, 500, -700, -700)

                elif infrared_value == 0:
                    print("going forward")
                    PWM.set_motor_model(-500, -500, -500, -500)

                elif infrared_value == 1:
                    print("small left")
                    PWM.set_motor_model(400, 400, -500, -500)

                elif infrared_value == 4:
                    print("small right")
                    PWM.set_motor_model(-500, -500, 400, 400)

                elif infrared_value == 7:
                    print("did we finish")
                    PWM.set_motor_model(500, 500, 500, 500)

                elif infrared_value == 2:
                    print("middle weird")
                    PWM.set_motor_model(-500, -500, 500, 500)

                else:
                    print("oh no")
                    PWM.set_motor_model(0, 0, 0, 0)

    except KeyboardInterrupt:
        sensors.close()
        PWM.close()
        print("\nEnd of program")