#include <ESP8266WiFi.h>

const char* ssid = "Agrawals"; //Enter SSID
const char* password = "23190914"; //Enter Password

#define LED_PIN D1
#define SOIL_PIN A0
#define TIMEOUT  5000
#define SLEEP_TIME_SECONDS 10

String writeAPIKey="YZECBAM777W3KPA3";

int numMeasure = 5;
int ADCValue = 0;
int Total = 0;

WiFiClient client;

void setup(void)
{
  Serial.begin(9600);
  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
     delay(500);
     Serial.print("*");
  }
  
  Serial.println("");
  Serial.println("WiFi connection Successful");
  Serial.print("The IP Address of ESP8266 Module is: ");
  Serial.print(WiFi.localIP());// Print the IP address
  
  pinMode( LED_PIN , OUTPUT );
  digitalWrite( LED_PIN , LOW );
}

void loop()
{
    

    //Get data from the soil pin
    int data = readSoil( numMeasure ); 
    Serial.print( "Soil Moisture = " );
    Serial.println(data);

    //Logic for ON_TIME and OFF_TIME
    bool IS_ON = (data >= 650);
    
    if (IS_ON){
       digitalWrite( LED_PIN , HIGH );
       delay(15000);
       digitalWrite( LED_PIN , LOW );
       Total = Total + 15;
    }
    HTTPPost(IS_ON);
    
    delay( 1000 );
    Serial.print( "Goodnight for "+String( SLEEP_TIME_SECONDS ) + " Seconds" );
    delay( SLEEP_TIME_SECONDS * 1000 );
}

long readSoil(int numAve)
{
  long ADCValue = 0;
  for ( int i = 0; i < numAve; i++ ) {
    delay(1000);    
    ADCValue += analogRead( SOIL_PIN );
  }
  
  ADCValue = ADCValue / numAve;
  return ADCValue;

}

int HTTPPost(bool ON){
  
    if (client.connect( "api.thingspeak.com" , 80)){

        String postData= "api_key=" + writeAPIKey+"&field1="+ON*1+"&field2="+Total;

        // POST data via HTTP.
        Serial.println( "Connecting to ThingSpeak for update..." );
        Serial.println();
        client.println( "POST /update HTTP/1.1" );
        client.println( "Host: api.thingspeak.com" );
        client.println( "Connection: close" );
        client.println( "Content-Type: application/x-www-form-urlencoded" );
        client.println( "Content-Length: " + String( postData.length() ) );
        client.println();
        client.print(postData);
        
        Serial.println( postData );
        
        String answer=getResponse();
        Serial.println( answer );
    }
    else
    {
      Serial.println ( "Connection Failed" );
    }
    
}

String getResponse(){
  String response;
  long startTime = millis();

  delay( 200 );
  while ( client.available() < 1 && (( millis() - startTime ) < TIMEOUT ) ){
        delay( 5 );
  }
  
  if( client.available() > 0 ){ 
     char charIn;
     do {
         charIn = client.read(); // Read a char from the buffer.
         response += charIn;     // Append the char to the string response.
        } while ( client.available() > 0 );
    }
  client.stop();
        
  return response;
}
