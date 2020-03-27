
## Name	: 
Inition Robot Car Control Using Myo Armband Gesture
## Module	: 
Gesture Based User Interface, BSc Hons Software Development.

## Introuduction: 
I was required to develop a project by using gesture or voice to control hardware devices or software objects. Hence, I have choosen the project of moving a robot car using the hand gestures. Following are the devices/software needed.


## Required Hardware

4tronix inition robot car chasis -  Website [here](https://4tronix.co.uk/blog/?p=169)

Rasberry pi 3 Model B V1.2 - Website [here](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)       

Robohat V1.7 - Website [here](https://shop.4tronix.co.uk/products/robohat)       

![alt tag](https://github.com/g00351263/RobotCar_Myo_Pi3/blob/master/initio.jpg)

Myo Armband - Website [here](https://www.myo.com/)    
![alt tag](https://github.com/g00351263/RobotCar_Myo_Pi3/blob/master/myo.jpg)

## Required Software

Rasbian OS for Rasberry pi- Website [here](https://www.raspberrypi.org/downloads/raspbian/)

Python to run scripts

## Installations and Testing

1. Install Rasbian OS into Raspberry Pi.
	1. Click here and follow instruction.		
[Rasbian](https://www.youtube.com/watch?v=RQ6JvnXwDCM)

2. Get Myo Armband Setup using PyoConnect Software for Raspberry Pi.
	1. Click here and follow instruction.
[PyoConnect](http://www.fernandocosentino.net/pyoconnect/)

		
3. Using the python run the scripts on command line i.e. python project.py.

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

##Code Explaination

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
				
				1. def onPoseEdge(pose):
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
			
			3. After Combining above 2 we can move car with gesture from Myo Armband
				
				1. def onPoseEdge(pose):
					if pose == pose.REST:
					elif pose == pose.FIST:
					elif pose == pose.WAVE_OUT:
					elif pose == pose.WAVE_IN:
					elif pose == pose.FINGERS_SPREAD:


## Issues During The Project
1. Shared the Pi and robohat with classmates, who burned down the pi and robohat, bought new robohat first, which was also defected and not supplying the current to dedicated motor connectors on roboHat. So, i utilized my electronics knowledge to change the one of the 2 diodes which were protecting the circuit on adapter connector and wire connector. hence, i used the direct wire connector which is shown by vin on robohat.

2. 2nd problem was the i had no TV, so couldn't connect the Pi to big screen, hence was using my mobile phone to connect to Raspberry desktop as remote. but for this option i had to connect PI to my own phone hotspot as IP address was assigned to PI from phone, and it wasn't changing all the time.

3. Corona Virus outbreak pandemic, colleges closed, no physical access to any material or hardware from college, but still got through the project.

4. Code for the both of the above devices was hard to adopt as Myo is discontinued and Robohat is not being used to much. usually people can control low power consumption components with GPIO library and directly from PI board, but power output wasn't enough to run 2 motors of our robot car.
					
## Authors

[Raja Naseer Ahmed Khan Dated 1/03/2020](https://github.com/g00351263/RobotCar_Myo_Pi3)            

## License

This project is licensed under the [MIT](https://github.com/g00351263/RobotCar_Myo_Pi3/blob/master/LICENSE) License 
        