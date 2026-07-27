Garbage Goons: Trubbish - The Mobile Trash Can

Trubbish is a trash car that can avoid obstacles, follow white paths and stop before hitting any objects in its path. Garbage Goons Inc. is proud to release the code and provide service to Tokyo!

-------------------------------------------

Setup: To run the car, you will have to first assemble the car with provided materials. Next you should connect to the appropriate Raspberry Pi through Visual Studio Code. Then you will clone this git repository into your VS Code, using instructions from Github. You should now have the correct code and libraries installed onto your raspberry pi. 

-------------------------------------------

Testing: To test the individual parts, open and run the correct python file (files described below), and check the terminal to make sure all parts are in order.


Test File Locations (⚠️ means car will move when you run the program):

Motor: Code -> Server -> motor.py (to test if Motors are working)⚠️ or nathanrobot2.0.py (to test certain actions of car)⚠️

Infrared: Code -> Server -> infrared.py (to test if infrared sensors are working)

Line following: Code -> Server -> nathanielinfrared.py (to test line following with motors)⚠️

Ultrasonic: Code -> Server -> trashultrasonic.py (to test ultrasonic sensors and stopping function)

-------------------------------------------

To run the final program, place your car on the path, and run final_trash.py from Code -> Server.
