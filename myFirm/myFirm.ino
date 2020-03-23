#include "LowPower.h"

//constants
const int pinT1 = 0;
const int pinT2 = 2;
const int baudRate = 9600;
const float analogTomV = 3300.0/1024.0; // Reference of 3.3V divided by 10 bit read (2^10)
const int sleep_reps = 75;          // 75 * 8 seconds -- 10 minutes

const int n = 10;                   //Samples for tempeterature reading

//global variables
char bufferIn[6];
float value = 0.0;                  //Value read from serial
int iWrite = 0;                     //Value to update
String cmd;                         //Command from serial
String data;

void setup() {
  analogReference(EXTERNAL);
  
  Serial.begin(baudRate);
  while(!Serial)  {;}
}

void loop() {
  Serial.println((getTemp(pinT1) + getTemp(pinT2))/2);
  Serial.flush();

  for(int i = 0; i<sleep_reps; ++i)
    LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
}

float getTemp(int pin)
{
  float mV = 0;
  float temp = 0;

  for(int i = 0; i < n; i++){
    mV = (float) analogRead(pin)*analogTomV;
    temp = temp + (mV-500.0)/10.0; //mV to degrees Celsius
  }
    return temp/float(n);
}
