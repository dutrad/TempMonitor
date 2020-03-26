#include "LowPower.h"

//constants
const int pinT1 = 0;
const int pinT2 = 2;
const int baudRate = 9600;
const float analogTomV = 3300.0/1024.0; // Reference of 3.3V divided by 10 bit read (2^10)
const int n = 10;                   //Samples for tempeterature reading

void setup() {
  analogReference(EXTERNAL);
  
  Serial.begin(baudRate);
  while(!Serial)  {;}
}

void loop() {
  LowPower.idle(SLEEP_FOREVER, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, 
                SPI_OFF, USART0_ON, TWI_OFF);
}

void serialEvent()
{
  Serial.println((getTemp(pinT1) + getTemp(pinT2))/2);
  Serial.flush();
  LowPower.idle(SLEEP_FOREVER, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, 
                SPI_OFF, USART0_ON, TWI_OFF);
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
