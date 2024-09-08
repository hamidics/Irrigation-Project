def automatic_registeration1():

     count=time.time()+30*1
     while time.time()<count:
          try:
                time.sleep(1)
                received_value = long(ser.readline())
                print(received_value)
                val=[0,0,0,0]
                val=split(val,received_value)
                
                if val[0]==20:
                        id = val[2]
                        type = val[1]
                        data = val[3]
                        time.sleep(1)
                        automatic_sensor_actuator_registration(type, id)
          except:
              # print 'hi me except'
               continue 
