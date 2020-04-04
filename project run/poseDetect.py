# Raja Naseer Ahmed khan

# this class will give us easy access to main method all the poses defined, also the robot movement is inserted here on pose detection
import sys
import time
import carFunctions

# getting files from lib folder
sys.path.append('../lib/')


# all the imports needed for working with myo and poses
from myo_starter import DeviceListener
from gesture import PoseType

# class decelartion
class PrintPoseListener(DeviceListener):
    # pose function which will be called from main with arguments will be updated as user moves hands
	def on_pose(self, pose):
            gesture = PoseType(pose)
            print(gesture.name)
            if ( gesture.name== "FINGERS_SPREAD"):
                    print("-------------------")
                    print("Forward")
                    print("--------------------")
					
					# getting distance from ultrasonic sensor
                    dist = carFunctions.getDistance()
                    
					# printing the distance from ultrasonic sensor
                    print(dist)
                    
					# if distance is <= 15 cms
                    if avgDistance <= 15:
					# car will wait and stop for 1.5 ms
                        time.sleep(1.5)
                        carFunctions.stop()
		
				# car will reverse for 1.5 ms
                        time.sleep(1.5)
                        carFunctions.reverse(30)
						

				# car will turn left until the distance more than 15		
						time.sleep(1.5)
						carFunctions.spinLeft(30)
						
                        time.sleep(1.5)
						
				    # if distance greater then 15 keep moving forward on myo signal
                    else:
                        carFunctions.forward(50)
                #forward
   
            elif(gesture.name== "WAVE_IN"):
                    print("--------------------")
                    print("Left Turning")
                    print("--------------------")
                    carFunctions.spinLeft(50)
                #lef
  
            elif(gesture.name== "WAVE_OUT"):
                    print("--------------------")
                    print("Right Turning")
                    print("--------------------")
                    carFunctions.spinRight(50)
                    
                #right
            elif(gesture.name== "REST"):
                    print("--------------------")
                    print("Stopped")
                    print("--------------------")
                    carFunctions.stop()
                #right
            
            elif(gesture.name== "FIST"):
                    print("---------------------")
                    print("Reverse")
                    print("--------------------")

                    carFunctions.reverse(50)

                
                
                 
                 
                    
