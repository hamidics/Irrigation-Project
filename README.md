Raspberrypi group were responsible to work with Raspberrypi and make it ready to be used as a server to send and receive data from/to other devices which are connected in Dripping Irrigation project. They had to work with RF Senders and Receivers, Arduinos and Raspberrypi to provide communication between devices and then install a webserver on the Raspberrypi to host the final web application on it. 

Main Tasks and Responsibilities
Raspberrypi group had the following responsibilities during the project timeline:
•	Installing preferred operating system on Raspberrypi.
•	Install needed libraries on Raspberrypi for sending/ receiving data from/to RF Transmitters.
•	Make functions to send, receive, pack and unpack the data.
•	Work with other groups to provide send/receive functionalities on the Arduinos.
•	Installing a web server with the support of Python to host the web application and the database of Dripping Irrigation project on it. 
•	Testing send/ receive functionalities.
•	Merge the system with the works of other groups.
![image](https://github.com/user-attachments/assets/49d00508-9042-487b-a726-85c6d30bcf09)

Step by step tasks done by the group members and their results:
After the first group meeting, our group made a diagram for the whole project. As you see in the following diagram all communication parties were specified. Besides in each part of the communication party the needed tools like Arduinos and RF Transmitters and Receivers were specified. 
 
Figure 1 Project diagram

Afterward we did our work in the following manner:

Step 1
We started to install an OS on the Raspberrypi. We tested Ubuntu, Windows and Noobs. But during the installation we had problems with Ubuntu and Windows. Both of the had problem in working with Raspberrypi. They needed more space and also more processing power. Finally, we installed Noobs and checked with the requirements of the project. It was lightweight OS and was working very good. 
For installation of Noobs we followed the following link:
https://www.Raspberrypi.org/help/noobs-setup/


Step 2
After installing the operating system, we installed a Python web server by the name of Flask and we followed instructions from the following link:
https://developer.codero.com/community/installing-flask-on-ubuntu/

After installation we made a small test program to check if everything is working or not. But during this time we faced a problem with Web group and then we decided to change the web server. 

Step 3
 When we faced a problem with Web development group we decided to change web server to Django according to their suggestion. We installed the web server and tested. Everything was then ready for the web development group. 

Step 4 
After installing the web server we started to do research about RF Transmitter and Receiver. So we used WiringPi python library and made two test program for sending and receiving data from/to sender/receiver. During testing the WiringPi, we found some problems, sometimes it was working and sometimes not. We couldn’t find a good solution so we decided to change the library to RCSwitch and some test codes to test our communication in RaspberryPi:

Figure 2 Sample code for sending data using RCSwitch

Step 5
We hosted the web application in RaspberryPi for further testing and working with it.

Merging our work with other groups:

Step 6
It was the time to merge everything we did with the work of other groups, but during the test we found another issue. Our sending/receiving code which was written in python and RCSwitch library had problem with the same library that was used by Actuator and Sensor group. We had to find another solution and make communication working between Raspberrypi and Arduinos that were being used by other groups. After doing a long research and many tests we found Virtual Wire library. It was called piVirtualWire in Raspberrypi. After installing piVirtualWire for python, we checked different code samples to test our RF receiver and transmitter with python. So we wrote the following code samples for testing both sender and receiver:


But after a while we found that the problem doesn’t depend on our library. The communication problem was because of supplying low electricity power for the sender and receiver so we changed back to RCSwitch library. 
Step 7
It was the time to coordinate with web development to help them in designing the data model and how the final database should look like. We provided them complete information about the project and helped them in designing the final data model for the web application.
Step 8
 Then we help Sensor and Actuator groups to use nano Arduinos. We provided them the communication code as well to make them able to send their data to the server (Raspberrypi)
Step 9
Everything got ready and the only part of communication was to design a packet structure. We made a packet structure and suggested other groups to use it as well. The packet structure is shown in the following picture:






Step 10
Merging our send/receive, pack, unpack, register and run function with web app group was done successfully and we had the following code snippets for different purposes (All codes of our group were merged in a file named RaspberrypiWebappIntegration.py
 Which is located in webapp/PlantIrrigationSystem/logic:

Automatic Registration:
It is called once and will run for 30 seconds, it automatically registers actuators and sensors in the database.

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

InsertData:
It runs in the backgrounds and is listening for the new data from sensors and then checks the data (if the soil need water or not). If the soil need water, then a command will be sent to the actuator to open the valve for 600 seconds. The loop checks the sensor values every 3 seconds and if the soil humadity is enough again, close valve command will be sent to the actuator. 



Split:
Is used to split a packet and put it in an array:

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


Concat:
Use to make a packet to send to the actuator.

# Function to concat the received value
def concat(appID, devicetype, TX_ID, Sensor1Data):
            z=appID*100000000+devicetype*10000000+TX_ID*10000+Sensor1Data
            return z;


Manually turn actuator on/off:
This function is used to manually turn the actuator on/off.

def send_actuator_duration_id_toTurnON(actuator_id, duration):
    
    #put the code of resbarrypi to send value to the actuator with actuator_id and duration
    print("The recived value of actuator id is:")
    print(actuator_id)
    print("The recived value of actuator duration is:")
    print(duration)
    packet=concat(20, 2, int(actuator_id), int(duration))
    sendPacket(packet)


Manually sending a packet:

def sendPacket(packet):
        sender.sendDecimal(packet, 32)


Manually receiving a packet:

def receivePacket():
        while True:
            if ser.ready():
                received_value = long(ser.readline())
                val=[0,0,0,0]
                val=split(val, received_value)

        return val



Step 11
Everything was working according to the plan but again the communication range betwenn aruinos and Raspberrypi was not good. It was only about 1 – 2 meters. So we had to use another solution. At the very end we came up with the solution of using an Arduino with connected receiver and then connecting it to the Raspberrypi to receive the data from the sensors. The following code snippets were used for this purpose:

Raspberrypi Part:
Connecting to the serial port and read the data from Arduino:

ser=serial.Serial('/dev/ttyUSB0',9600)


Reading the data from serial port:

received_value = long(ser.readline())


Arduino Part:


const int ledPin = 13;
void setup() {
 Serial.begin(9600);
  mySwitch.enableReceive(receivePin);  // Receiver on inerrupt 0 =&gt; that is pin #2
  mySwitch.enableTransmit(transmitPin);
}

int checkvalue(long val)
{
  long App, Act, DevType, Sec, temp, temp1, id, value;
  App = val / 100000000;
  temp = val % 100000000;

  DevType = temp / 10000000;
  temp1 = val % 10000000;

  id = temp1 / 10000;
  value = val % 10000;

if(App==20 && (DevType==1 || DevType==3)){
      return 1;
}else{
  return 0;
  
}
}



void loop() {
int receivedpack=0;
long value;
 if (mySwitch.available()) {
      value = mySwitch.getReceivedValue();
       
     
      receivedpack=checkvalue(value);
      if(receivedpack==1){
         Serial.println(value);
      delay(2000);
    
      mySwitch.resetAvailable();
      }
  }
}



Technical Information for Connecting RF Transmitter/ Receiver to RaspberryPi and/or Arduinos
RaspberryPi connection with RF Transmitter / Receiver:
Connect sender Module: 	
ADATA: Pin 11 which is BCM GPIO 17 and WiringPi Pin 0	
VCC: +3,3V on my breakout (without Breakout use Pin 1 on RPi)	
GND: GND on my breakout (without Breakout use Pin 6 on RPi)	

Connect receiver Module: 	
DATA: Pin 12 which is BCM GPIO 18 and WiringPi Pin 1 (Dosn’t matter which of the both data pins you use)	
VCC: +3,3V on my breakout (without Breakout use Pin 1 on RPi)	
GND: GND on my breakout (without Breakout use Pin 6 on RPi)
In the following picture pins of RaspberryPi with their numbers are shown:
 
Figure 5 RaspberryPi Serial pins

In the following picture the sender connection with RaspberryPi is shown:
 

In the following picture the receiver pins are provided which could be connected to the RaspberryPi:
 

Arduino connection with RF Transmitter / Receiver
Arduino as receiver connection is provided in the following picture:

 
and Arduino as sender connection is provided in the following picture:

 


Conclusion 
After a long process to work on the system we could finally make it usable. For the first time when we went to install it in the garden it had problem, but after working on our final solution for receiving the data using Arduino and then Raspberrypi everything was working fine. 
 
References
http://www.homautomation.org/2013/09/21/433mhtz-rf-communication-between-arduino-and-raspberry-pi/
http://www.homautomation.org/2014/03/02/433mhtz-rf-communication-between-arduino-and-raspberry-pi-arduino-as-receiver/
http://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/
https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=66946
http://shop.ninjablocks.com/blogs/how-to/7506204-adding-433-to-your-raspberry-pi
http://www.princetronics.com/how-to-read-433-mhz-codes-w-raspberry-pi-433-mhz-receiver/



![image](https://github.com/user-attachments/assets/129723ff-1bd2-4f78-9698-c76750067e69)
