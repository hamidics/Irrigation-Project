# Function to split the received value
def split(val, valn):
 #valn=20 1 300 0899
         appId = valn / 100000000
         tempdevid=valn%100000000
         devicetype=tempdevid/10000000
         temp = valn % 10000000
         TXid = temp / 10000
         SensorValue = temp % 10000
         val=[appId,devicetype, TXid, SensorValue]
         print(appId)
         print(devicetype)
         print(TXid)
         print(SensorValue)
         return val
