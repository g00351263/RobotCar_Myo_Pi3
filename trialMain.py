import trial
import time


def main():
	print('main function')

	dist = trial.getDistance()
	
	if trial.getDistance() <= 10:
		print('obstruction')
		trial.stop()
		time.sleep(1.5)
		trial.reverse()
		time.sleep(1.5)
		trial.spinLeft()
		time.sleep(1.5)
	else:
		trial.forward()
	
if __name__ == '__main__':
	main()