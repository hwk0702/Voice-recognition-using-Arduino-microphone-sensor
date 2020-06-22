#define LOG_OUT 1 // use the log output function
#define FFT_N 256 // set to 256 point fft

#include <FFT.h> // include the library
#include <avr/io.h>
#include <avr/interrupt.h>

const int inputPin = 2; 
const int ledPin = 3;

long startTime = 0;

void setup() {
  Serial.begin(115200); // use the serial port
  //TIMSK0 = 0; // turn off timer0 for lower jitter
  ADCSRA = 0xe5; // set the adc to free running mode
  ADMUX = 0x40; // use adc0
  DIDR0 = 0x01; // turn off the digital input for adc0
  pinMode(inputPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  
  if (digitalRead(inputPin)==LOW){
    startTime = millis();
    digitalWrite(ledPin,HIGH);
    
    while (millis()-startTime<=1000){
       // reduces jitter
      cli();  // UDRE interrupt slows this way down on arduino1.0
      for (int i = 0 ; i < 512 ; i += 2) { // save 256 samples
        while(!(ADCSRA & 0x10)); // wait for adc to be ready
        ADCSRA = 0xf5; // restart adc
        byte m = ADCL; // fetch adc data
        byte j = ADCH;
        int k = (j << 8) | m; // form into an int
        k -= 0x0200; // form into a signed int
        k <<= 6; // form into a 16b signed int
        fft_input[i] = k; // put real data into even bins
        fft_input[i+1] = 0; // set odd bins to 0
      }
      fft_window(); // window the data for better frequency response
      fft_reorder(); // reorder the data before doing the fft
      fft_run(); // process the data in the fft
      fft_mag_log(); // take the output of the fft
      sei();
      /*
      Serial.write(fft_log_out, FFT_N/2); // send out the data
      Serial.write("\n");
      */
      
      for (int i=0; i <= 128; i++){
        Serial.print(fft_log_out[i]);
        if (i!=128) Serial.print(',');
      }
      
      Serial.print("\n");
      
      //if (millis()-startTime==2000) break;
    }
    digitalWrite(ledPin,LOW);
    //Serial.println("exit");
  }
  else{
    digitalWrite(ledPin,LOW);
  }
  
    /*
    for (int i=0; i <= 128; i++){
      Serial.println(fft_log_out[i]);
    }
    Serial.print("\n");
    */
  
}
