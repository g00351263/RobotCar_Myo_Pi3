# Raja Naseer Ahmed khan

# this class will give us easy access to main method all the poses defined, also the robot movement is inserted here on pose detection
import sys

# functions if we need sleep method to give gap
import time

# access to robohat circuit
import robohat

# getting files from lib folder
sys.path.append('../lib/')


# all the funtionss needed for working with myo and poses
from device_listener import DeviceListener
from pose_type import PoseType

# class decelartion
class PrintPoseListener(DeviceListener):
    # pose function which will be called from main with arguments will be updated as user moves hands
	def on_pose(self, pose):
            pose_type = PoseType(pose)
            print(pose_type.name)
            if ( pose_type.name== "FINGERS_SPREAD"):
                    print("-------------------")
                    print("Forward")
                    print("--------------------")
                    robohat.reverse(10)
                #forward
        
            elif(pose_type.name== "DOUBLE_TAP"):
                    print("---------------------")
                    print("nothing")
                    print("---------------------")
    
                #reverse
   
            elif(pose_type.name== "WAVE_IN"):
                    print("--------------------")
                    print("Left Turning")
                    print("--------------------")
                    robohat.spinLeft(10)

                #left
  
            elif(pose_type.name== "WAVE_OUT"):
                    print("--------------------")
                    print("Right Turning")
                    print("--------------------")
                    robohat.spinRight(10)
                    
                #right
            elif(pose_type.name== "REST"):
                    print("--------------------")
                    print("Stopped")
                    print("--------------------")
                    robohat.stop()
                #right
            
            elif(pose_type.name== "FIST"):
                    print("---------------------")
                    print("Reverse")
                    print("--------------------")
                    robohat.forward(10)

                
                
                 
                 
                    
