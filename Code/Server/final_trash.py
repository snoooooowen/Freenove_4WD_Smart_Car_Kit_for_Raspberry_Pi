#Name: final_trash.py
#Author: Nathan Lee and Owen Chan
#Purpose: Make our robot, Trubbish, navigate a track with obstacles, collect trash, then go back to the start.
from motor import Ordinary_Car #Import class Ordinary_Car from motor.py. Lets the code interact with the motors of the car.
from infrared import LineSensor 
from infrared import Infrared #Import Infrared and LineSensor from infrared.py
import time 
from gpiozero import DistanceSensor, PWMSoftwareFallback, DistanceSensorNoEcho
import warnings
from ultrasonic import Ultrasonic
#Import time, gpiozero, warnings, and Class Ultrasonic from ultrasonic.py

PWM = Ordinary_Car() #Car variable equals PWM to not rewrite code
sensors = Infrared() #Infrared() is set equal to sensors

#movement functions
#Wheels are (Top left, bottom left, top right, bottom right). You might have to negate all values of robot is going backwards.
def T180(): #Turns robot 180 Left
     print("turning 180")
     
     #turning left 
     PWM.set_motor_model(700,700,-700,-700) 
     time.sleep(1) 
     
     #pause
     PWM.set_motor_model(0, 0, 0, 0)
     time.sleep(0.3)


def avoid_obstacle_L(): #First version of avoid obstacle. Will stop, slide to the left, move past the obstacle, then slide right back to the track
    print("Avoiding obstacle...")
    # Stop
    PWM.set_motor_model(0, 0, 0, 0)
    time.sleep(0.5)

    # Slide left
    PWM.set_motor_model(600, -600, -600, 600)
    time.sleep(0.8)

    # Drive past the obstacle
    PWM.set_motor_model(-600, -600, -600, -600)
    time.sleep(0.9)

    # Slide right
    PWM.set_motor_model(-600, 600, 600, -600)
    time.sleep(0.9)

    # Stop briefly before resuming line following
    PWM.set_motor_model(0, 0, 0, 0)
    time.sleep(0.3)

    print("Obstacle avoided.")


def avoid_obstacle_R(): #Reverse function of avoid_obstacle_L()

    print("Avoiding obstacle...")
    # Stop
    PWM.set_motor_model(0, 0, 0, 0)
    time.sleep(0.5)

    # Slide right
    PWM.set_motor_model(-700, 700, 700, -700)
    time.sleep(0.7)

    # Drive past the obstacle
    PWM.set_motor_model(-600, -600, -600, -600)
    time.sleep(0.9)

    #slide left
    PWM.set_motor_model(700, -700, -700, 700)
    time.sleep(0.75)

    # Stop briefly before resuming line following
    PWM.set_motor_model(0, 0, 0, 0)
    time.sleep(0.3)

    print("Obstacle avoided.")


if __name__ == '__main__':
    try:
        with Ultrasonic() as ultrasonic:
            # Continuously read and print the combined value of all infrared sensors
            while True: #while this function is true, the ultrasonic sensor and infrared will continuously read the sensor values every 0.01 seconds. 
                distance = ultrasonic.get_distance()
                print(f"Ultrasonic distance: {distance}cm")
                time.sleep(0.01)

                infrared_value = sensors.read_all_infrared()
                print(f"Infrared value: {infrared_value}")
                time.sleep(0.01)


                # Obstacle detected
                if distance is not None and distance <= 20.5: 
                    # When the object detected within the Ultrasonic sensor is less than 20.5 centimeters, it will set all motors to zero
                    PWM.set_motor_model(0, 0, 0, 0)

                    while True: #After all motors are set to zero, it will prompt the user to give a statement.
                        choice = input(
                            "\nObstacle detected!\n"
                            "Type 'move left' to go around left\n"
                            "Type 'move right' to go around right\n"
                            "Type 'goal' if this is the destination and you would like to turn around\n> "
                            "Type 'done' if you are done: "
                        ).strip().lower()

                        if choice == "move left": #If you type "move left" it will execute avoid_obstacle_L(). See on line 27
                            avoid_obstacle_L()
                            break      # Continue line following

                        elif choice == "move right": #If you type "move right" it will execute avoid_obstacle_R(). See on line 52
                            avoid_obstacle_R()
                            break

                        elif choice == "done": # finishes the code. Sets all motors to zero and exits
                            print("finished")
                            PWM.set_motor_model(0, 0, 0, 0)
                            sensors.close()
                            PWM.close()
                            exit()

                        elif choice == "goal": #makes a full 180 to turn around to do the track again.
                            print("turning around")
                            T180()
                            break

                        else: #Whenever users types something that isn't one of the prompts above. Please type one of those.
                            print("Invalid input. Please type 'move', 'goal' or 'done'.")

               #There are 3 infrared sensors. Left sensor has value 4, Middle sensor has value 2, Right sensor has value 1.
               #The infrared sensors allow the robot to be within black line boundaries of track.
                elif infrared_value == 6: #Left and Middle sensor are triggered.
                    print("far right")
                    PWM.set_motor_model(-700, -700, 500, 500) #Left wheels go forward while right slowly goes backward to make a sharp turn right

                elif infrared_value == 3: #Right and middle sensor are triggered
                    print("far left")
                    PWM.set_motor_model(500, 500, -700, -700) #Right wheels go forward while left slowly goes backward to make a sharp turn left

                elif infrared_value == 0: # No sensors are triggered
                    print("going forward")
                    PWM.set_motor_model(-500, -500, -500, -500) #All wheels move forward

                elif infrared_value == 1: #Right sensor is triggered
                    print("small left")
                    PWM.set_motor_model(400, 400, -500, -500) #The wheels make a tiny left to adjust.

                elif infrared_value == 4: #Left sensor is triggered
                    print("small right")
                    PWM.set_motor_model(-500, -500, 400, 400) #The wheels make a tiny right to adjust.

                elif infrared_value == 7: #All sensors are triggered
                    print("did we finish")
                    PWM.set_motor_model(700, 700, 700, 700) #Wheels make a small back to retry a section

                elif infrared_value == 2: #Middle sensor is triggered
                    print("middle weird")
                    PWM.set_motor_model(-500, -500, 500, 500) #Rotates to fix only middle sensor being activated

                else: #Failsafe if nothing works
                    print("oh no")
                    PWM.set_motor_model(0, 0, 0, 0) #Stops the car


    except KeyboardInterrupt: #Whenever you type ^C/ctrl+C, it will force stop the entire program.
        sensors.close() #Closes sensors
        PWM.close() #Closes motors
        print("\nEnd of program")
