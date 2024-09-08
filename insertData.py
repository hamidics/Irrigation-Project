def insertData1():
     
     while True:
          try:
               time.sleep(1)
               #if ser.ready():
               received_value = long(ser.readline())
               val=[0,0,0,0]
               val=split(val,received_value)
               
               if val[0]==20:
                    type = val[1]
                    id = val[2]
                    data = val[3]
                    if type==1:
                         insert_new_sensor_datapoint(id, data)
                         actid=get_actuator_id_for_sensor(id)
                         #print actid
                         #getting sensor type
                         sensortype=get_type_for_sensor(id)
                         #print sensortype
                         if sensortype==1:
                              #min in water or max in humid soil is 326
                               conditionvalue1=350
                               condition=data>conditionvalue1
                         elif sensortype==3:
                              #value bigger than 470 has enough water
                               conditionvalue=450
                               condition=data<=conditionvalue
                              
                         if condition:
                              pack=concat(val[0],2,actid,600)
                              time.sleep(1)
                              sendPacket(pack)
                              print(pack)
                         else :
                              time.sleep(1)
                              pack=concat(val[0],2,actid,0)
                              sendPacket(pack)
                              print(pack)
          except:
         #      print 'hi me except'
               continue
