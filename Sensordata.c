#include <RCSwitch.h>
 long Sensor1Data =0;
 long appID= 25;
 long TX_ID = 41;
RCSwitch mySwitch = RCSwitch(); 
void setup() {
  Serial.begin(9600);
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(10);
}

void loop() {
      Sensor1Data = analogRead(A0);
    // Same switch as above, but using decimal code /
     if (Sensor1Data > 999)
      Sensor1Data = 999;
    long z=appID * 100000  + TX_ID * 1000 + Sensor1Data;
    Serial.println(z);
    mySwitch.send( z, 24);
}
