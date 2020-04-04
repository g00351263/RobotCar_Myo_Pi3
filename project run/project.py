# Raja Naseer Ahmed Khan Gesture Based Programming

import sys
import time

# access to robohat function
import carFunctions

# getting access to function for my from libarar
sys.path.append('../modules/')


# accessing my libraries
from myo import Myo

# access to poses libarary
from poseDetect import PrintPoseListener

# accessing the myo viration library
from myo_vibrate import VibrationType

# accessing the pose and type of pose interface
from gesture import PoseType

# connection listner to myo
from myo_starter import DeviceListener

# intialising the robohat circuit
carFunctions.init()

# main method
def main():
    print('Myo Heating UP')
    # saving the pose in variable
    listener = PrintPoseListener()
    
    # access to myo via variable obj
    myo = Myo()

    try:
        
        # connection to myo
        myo.connect()
        
        # adding pose to myo
        myo.add_listener(listener)
        
        #vibration on start
        myo.vibrate(VibrationType.SHORT)
        
        #keep running until program we exit
        while True:
            myo.run()
        
    except KeyboardInterrupt:
        pass
    except ValueError as ex:
        print(ex)
    finally:
        myo.safely_disconnect()
        print('Myo App is ended.')


if __name__ == '__main__':
    main()
    
    
    
