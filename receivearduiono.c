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
