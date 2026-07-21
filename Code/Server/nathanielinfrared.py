from infrared import LineSensor
from infrared import Infrared
import time
from motor import Ordinary_Car

PWM = Ordinary_Car()
sensors = Infrared()


if __name__ == '__main__':
    try:
        # Continuously read and print the combined value of all infrared sensors
        while True:
            infrared_value = sensors.read_all_infrared()
            print(f"Infrared value: {infrared_value}")
            time.sleep(0.01)
            
        
            if infrared_value == 6:
                print("far right")
                PWM.set_motor_model(-700, -700, 500 , 500)
            
            elif infrared_value == 3:
                print("far left")
                PWM.set_motor_model (500, 500, -700, -700)

            elif infrared_value == 0:
                print ("going forward")
                PWM.set_motor_model (-500, -500, -500, -500)
            
            elif infrared_value ==1:
                print("small left")
                PWM.set_motor_model(400, 400, -500, -500 )

            elif infrared_value == 4:
                print("small right ")
                PWM.set_motor_model(-500, -500,400 , 400)

            elif infrared_value==7:
                print ("did we finish")
                PWM.set_motor_model(500, 500, 500, 500)
            
            elif infrared_value==2:
                print ("middle wierd")
                PWM.set_motor_model(-500, -500, 500, 500)

            else:
                print ("oh no")
                PWM.set_motor_model(0, 0, 0, 0)
            
    except KeyboardInterrupt:
        # Close the Infrared object and print a message when interrupte
        sensors.close()
        PWM.close()
        print("\nEnd of program")
