# Raja Naseer Ahmed Khan

# access to functions from struct files
from struct import *

# class defined to be used to connect and check data
class DeviceListener(object):

#function which will handle data
	def handle_data(self, data):
		if data.cls != 4 and data.command != 5:
			return

		connection, attribute, data_type = unpack('BHB', data.payload[:4])
		payload = data.payload[5:]

		if attribute == 0x23:
			data_type, value, address, _, _, _ = unpack('6B', payload)

			if data_type == 3:
				self.on_pose(value)

				# functions that will pass the pose
	def on_pose(self, pose):
		pass
