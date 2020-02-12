#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         7          // Configurable, see typical pin layout above
#define SS_PIN          6 
MFRC522 rfid(SS_PIN, RST_PIN);   // Create MFRC522 instance.

 int count=0;
 String url ;
void setup() 
{
  Serial.begin(9600);
  SPI.begin();      // Initiate  SPI bus
  rfid.PCD_Init();   // Initiate MFRC522
}
void loop() 
{
  
  // Look for new cards
  if ( ! rfid.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! rfid.PICC_ReadCardSerial()) 
  {
    return;
  }
  String id= "";

  for (byte i = 0; i < rfid.uid.size; i++) 
  {
     id.concat(String(rfid.uid.uidByte[i]));
     id.concat(String(rfid.uid.uidByte[i], HEX));
  }
     id.toUpperCase();      
  // Serial.println(id);
   if(id=="233E913688203CB13183")
     {
        Serial.println("a");
     }
     
   if(id=="164A41569C2317163A3")
     {
        Serial.println("b");
     }

  
} 
