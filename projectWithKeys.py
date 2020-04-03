
import sys
sys.path.append('./modules/')
import tty
import termios
import car, time




from myo import Myo
from print_pose_listener import PrintPoseListener
from vibration_type import VibrationType
from pose_type import PoseType
from device_listener import DeviceListener



speed = 4

# this function is used to get the alphabet keys pressed to move the car
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

# this function is used to get the direction keys pressed on keyboard
def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows



print "Tests the motors by using the arrow keys to control"
print "Use , or < to slow down"
print "Use . or > to speed up"
print "Speed changes take effect when the next arrow key is pressed"
print "Press Ctrl-C to end"
print

car.init()
print('Start Myo for Linux')

listener = PrintPoseListener()
myo = Myo()
# main loop
def main():
    
    try:
        myo.connect()
        myo.add_listener(listener)
        myo.vibrate(VibrationType.SHORT)
        
        while True:
            myo.run()
            dist = car.getDistance()
            print "Distance: ", int(dist)


            keyp = readkey()
            if keyp == 'w' or ord(keyp) == 16:
                car.forward(speed)
                car.obstruction(dist)
            elif keyp == 'z' or ord(keyp) == 17:
                car.reverse(speed)
                print 'Reverse', speed
            elif keyp == 's' or ord(keyp) == 18:
                car.spinRight(speed)
                print 'Spin Right', speed
            elif keyp == 'a' or ord(keyp) == 19:
                car.spinLeft(speed)
                print 'Spin Left', speed
            elif keyp == '.' or keyp == '>':
                speed = min(100, speed+10)
                print 'Speed+', speed
            elif keyp == ',' or keyp == '<':
                speed = max (0, speed-10)
                print 'Speed-', speed
            elif keyp == ' ':
                car.stop()
                print 'Stop'
            elif ord(keyp) == 3:
                break

    except KeyboardInterrupt:
        print
        pass

    finally:
        car.cleanup()
        myo.safely_disconnect()
        print('Finished.')

if __name__ == '__main__':
    main()
