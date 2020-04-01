
## Name	: 
Inition Robot Car Control Using Myo Armband Gesture
## Module	: 
Gesture Based User Interface, BSc Hons Software Development.

## Introuduction: 
I was required to develop a project by using gesture or voice to control hardware devices or software objects. Hence, I have choosen the project of moving a robot car using the hand gestures. Following are the devices/software needed.


(Important) Make sure python version (2.7)is the version used, otherwise might get conflict and code won't run. Also let myo armband heat up to work.

## Required Hardware

4tronix inition robot car chasis -  Website [here](https://4tronix.co.uk/blog/?p=169)

Rasberry pi 3 Model B V1.2 - Website [here](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)       

Robohat V1.7 - Website [here](https://shop.4tronix.co.uk/products/robohat)       

![alt tag](https://github.com/g00351263/RobotCar_Myo_Pi3/blob/master/images/initio.jpg)

Myo Armband - Website [here](https://www.myo.com/)    
![alt tag](https://github.com/g00351263/RobotCar_Myo_Pi3/blob/master/images/myo.jpg)

## Required Software

Rasbian OS for Rasberry pi- Website [here](https://www.raspberrypi.org/downloads/raspbian/)

Python to run scripts

Direct bluetooth connection between Linux and Myo armband using Bluegiga BGAPI/BGLib

Tested in a Raspberry Pi. video: https://www.youtube.com/watch?v=AWxEL4l4Fg8

### Pre-requirements for your Myo device
- Firmware version 1.3.1448 or higher
- It is necessary to calibrate your Myo device using the official software.
- Use the Myo dongle bluetooth

### Requirements
- python >=2.6
- pySerial
- enum34

### Execute Sample
The Myo dongle bluetooth must be connected.

- Open the console "terminal" 
- Go to sample folder in the project
- Execute this command:
  ```
  python run.py


## Installations and Testing

1. Install Rasbian OS into Raspberry Pi.
	1. Click here and follow instruction.		
[Rasbian](https://www.youtube.com/watch?v=RQ6JvnXwDCM)

2. Get Myo Armband Setup using PyoConnect Software for Raspberry Pi.
	1. Click here and follow instruction.
[PyoConnect](http://www.fernandocosentino.net/pyoconnect/)

		
3. Using the python version -- run the scripts on command line i.e. python project.py.

4. Wear the Myo armband on any of arm just below elbow.
	1. Click here for learn how to use Myo.
[Myo](https://support.getmyo.com/hc/en-us/articles/201169525-How-to-wear-the-Myo-armband)

		
5. Do the Following Gesture to move the robot car.

	1. Fist is to move backward
	2. Open Hand to move forward
	3. Wave Left to move left
	4. Wave Right to move right
	5. Relaxing hand to stop car

6. Some other good tutorials for the project. Click here
[Tutorial](https://www.hackster.io/brink-io/rover-controlled-using-myo-armband-and-raspberry-pi-3-c09379)

## Code Explaination

1. First is to connect Myo with Pi, Follow the code at http://www.fernandocosentino.net/pyoconnect/) also you can get here all the code to detect the poses.

2. Setup The RoboHat into the python file by following code
	1.	import robohat 
		1. this line gives access to roboHat libraries, which has the options to control 2 motors for running car all around, also i have fitted the ultrasonic sensor to detect the distance from an object.
		
			1.	Following are the pre-built functions used from library to move car
			
				1. robohat.stop() for stopping car
				2. robohat.forward() moving forward
				3. robohat.reverse() to reverse
				3. robohat.spinRight() to turn right
				4. robohat.spinLeft() to turn Left
			
			2. Following is the functions made from pyoconnect to detect pose
				
				1. def on_Pose(pose):
					if pose == pose.REST:
					elif pose == pose.FIST:
					elif pose == pose.WAVE_OUT:
					elif pose == pose.WAVE_IN:
					elif pose == pose.FINGERS_SPREAD:
			
			
			3. After Combining above 2 we can move car with gesture from Myo Armband
				
				1. def on_pose(pose):
					if pose == pose.REST:
					robohat.stop()
					elif pose == pose.FIST:
					robohat.reverse()
					elif pose == pose.WAVE_OUT:
					robohat.spinLeft()
					elif pose == pose.WAVE_IN:
					robohat.spinRight()
					elif pose == pose.FINGERS_SPREAD:
					robohat.forward()

			4. We can get distance from the ultrasonic sensor 
by using robohat.getDistance() and combining this with if statement in pose = Fist then get distance and distance less than 20 cms then turn right and continue until distance is less than 20 cms.

## Files and Their Details
1. run this for project.py = has main function to run and starting Myo listner to pass on values to car.

2. pose_listener.py = is used to get the poses performed and return funtions on detection of each pose.

3. device_listener.py = is used to start listening to Myo armband.

4. robohat = giving access to functions to robohat circuit using low level interace in Raspbbery pi 3.

5. pose_type.py = enum giving access to pose types with numbers unique numbers assigned to each pose.

6. \lib\vibration_type.py = enum file for assigning numbers to vibration types

7. \lib\myo.py = has all the functions from myo libaries available for working with Myo (its downloaded from pyoconnect)

8. \lib\ble.py = is giving access to bluetooth of Raspberry pi with code downloaded one of the reference.

9. \lib\packet.py = getting the structured function from utilities and returning data from my.

10. \lib\utilities.py = is defining structure of for some of the functions will be used fetch,pass and map data.

## Issues During The Project
1. Shared the Pi and robohat with classmates, who burned down the pi and robohat, bought new robohat first, which was also defected and not supplying the current to dedicated motor connectors on roboHat. So, i utilized my electronics knowledge to change the one of the 2 diodes which were protecting the circuit on adapter connector and wire connector. hence, i used the direct wire connector which is shown by vin on robohat.

2. 2nd problem was the i had no TV, so couldn't connect the Pi to big screen, hence was using my mobile phone to connect to Raspberry desktop as remote. but for this option i had to connect PI to my own phone hotspot as IP address was assigned to PI from phone, and it wasn't changing all the time.

3. Corona Virus outbreak pandemic, colleges closed, no physical access to any material or hardware from college, but still got through the project.

4. Code for the both of the above devices was hard to adopt as Myo is discontinued and Robohat is not being used to much. usually people can control low power consumption components with GPIO library and directly from PI board, but power output wasn't enough to run 2 motors of our robot car.

## Conclusion

We have learned how to use our coding skills along with the electronic components to get bit glimpse of Embedded Programming, but this wasn't a true embedded programming as we have to go through the libraries to make Myo work, which has been discontinued product, Hence not much support was available. Real Robotics programming is similar where we control the output power of each terminal, which is then input in another function to compute the output of each desired terminal will signal, That will calculate the speed, rotation angle, and stop statements of the robot.

## Recommendations

I would sincerely recommend to use the available gesture devices which are still in production, as there will be lots of support avaialbe and in all the languages would be supported to.				
## Authors

[Raja Naseer Ahmed Khan Dated 1/03/2020](https://github.com/g00351263/RobotCar_Myo_Pi3)

## References            

[PyoConnect](http://www.fernandocosentino.net/pyoconnect/)
[Myo Connection](https://github.com/avineshmohan/Rover-Myo)

## License

This project is licensed under the [MIT](https://github.com/g00351263/RobotCar_Myo_Pi3/blob/master/LICENSE) License 
        