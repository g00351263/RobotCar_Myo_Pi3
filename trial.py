
# End of General Functions
#======================================================================


#======================================================================
# Motor Functions
#
# stop(): Stops both motors
def stop():
	print('stop')
	
# forward(speed): Sets both motors to move forward at speed. 0 <= speed <= 100
def forward():
	print('forward')
	
    
# reverse(speed): Sets both motors to reverse at speed. 0 <= speed <= 100
def reverse():
	print('reverse')

# spinLeft(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
def spinLeft():
	print('left')
    
# spinRight(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
def spinRight():
	print('right')

    
# turnReverse(leftSpeed, rightSpeed): Moves backwards in an arc by setting different speeds. 0 <= leftSpeed,rightSpeed <= 100
def turnReverse():
	print('reverse')
# End of IR Sensor Functions
#======================================================================
#======================================================================
# UltraSonic Functions
#
# getDistance(). Returns the distance in cm to the nearest reflecting object. 0 == no object
def getDistance():
	return 9;

