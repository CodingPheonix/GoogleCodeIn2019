#include <ESP8266WiFi.h>

#define WIFI_NAME "Agrawals"
#define PASSWORD "23190914"

#define LED_PIN D1
#define SENSOR_POWER D2
#define SOIL_PIN D3
#define TIMEOUT  5000
#define SLEEP_TIME_SECONDS 1800

String writeAPIKey="4NAY9GRA15TEY2YI";

int numMeasure = 5;
int ADCValue = 0;
                         
WiFiClient client;

void setup()
{
    Serial.begin( 115200 );
    while (WiFi.status() != WL_CONNECTED) {
        WiFi.begin( WIFI_NAME , PASSWORD );
        Serial.println( "Connecting to Wi-Fi" );
        delay( 2500 );
    }
    Serial.println( "Connected" );
    pinMode( SENSOR_POWER , OUTPUT );
    pinMode( LED_PIN , OUTPUT );
    digitalWrite( SENSOR_POWER , LOW );
    digitalWrite( LED_PIN , LOW );
}

void loop()
{

    //Get data from the soil pin
    int data = String( readSoil( numMeasure ) ); 
    Serial.print( "Soil Moisture = " );
    Serial.println(data);

    //Logic for ON_TIME and OFF_TIME
    bool IS_ON = (data <= 150);
    
    if (IS_ON){
       digitalWrite( LED_PIN , HIGH );
    }
    
    HTTPPost(IS_ON);
    
    delay( 1000 );
    Serial.print( "Goodnight for "+String( SLEEP_TIME_SECONDS ) + " Seconds" );
    ESP.deepSleep( SLEEP_TIME_SECONDS * 1000000 );

    //Similar to --> delay( 20000 );
}

long readSoil(int numAve)
{
  long ADCValue = 0;
  
  for ( int i = 0; i < numAve; i++ ) {
    digitalWrite( SENSOR_POWER, HIGH );
    delay(10);    
    ADCValue += analogRead( SOIL_PIN );
    digitalWrite( SENSOR_POWER, LOW );
  }
  
  ADCValue = ADCValue / numAve;
  return ADCValue;

}
  
int HTTPPost(bool ON){
  
    if (client.connect( "api.thingspeak.com" , 80)){

        String postData= "api_key="+writeAPIKey+"field1="+ON*1;
        Serial.println(postData);

        // POST data via HTTP.
        Serial.println( "Connecting to ThingSpeak for update..." );
        Serial.println();
        
        client.println( "POST /update HTTP/1.1" );
        client.println( "Host: api.thingspeak.com" );
        client.println( "Connection: close" );
        client.println( "Content-Type: application/x-www-form-urlencoded" );
        client.println( "Content-Length: " + String( postData.length() ) );
        client.println();
        client.println( postData );
        
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
