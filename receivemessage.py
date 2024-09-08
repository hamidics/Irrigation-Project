import piVirtualWire
import pigpio
import time

pi=pigpio.pi()
rx=piVirtualWire.rx(pi, 18, 1000)
while True:
	while rx.ready():
		print ‘’.join(map(char, rx.get()))
		time.sleep(0.5)
rx.cancel()
pi.stop()
