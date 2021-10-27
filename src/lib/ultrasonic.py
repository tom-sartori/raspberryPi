from grovepi import *

# plug it to a D-port

# Commande Format Ultrasonic read
uRead_cmd = [7]

# Read value from Grove Ultrasonic
# Set I/O Digital pin 
def ultrasonicRead(pin):
	write_i2c_block(address, uRead_cmd + [pin, unused, unused])
	time.sleep(.06)	#firmware has a time of 50ms so wait for more than that
	read_i2c_byte(address)
	number = read_i2c_block(address)
	return (number[1] * 256 + number[2])
