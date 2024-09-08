import piVirtualWire
import pigpio
import time

pi=pigpio.pi()
tx=piVirtualWire.tx(pi, 17, 1000)
msg=’1234’
tx.put(msg)
tx.waitForReady()
tx.cancel()
pi.stop()
