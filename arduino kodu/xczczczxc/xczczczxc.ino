#define potsinyal A0 


int deger = 0; 


void setup() 
{
  Serial.begin(9600); 
 
  


}

void loop() 
{
  deger = analogRead(potsinyal); 
  
  
  Serial.println(deger); 
  
  
  delay(250); 
}