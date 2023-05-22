#ifndef webconnector_h
#define webconnector_h

// für ESP8266: 
#include <ESP8266WiFi.h>
// für ESP32: 
//#include <WiFi.h>
#include <WiFiClient.h>



class WebConnector {
  public:
    // Initialize the server
    void init();
    void handleConnection();
    String getActiveCommand();
  private:
    String input;
    String activeCommand;

};

#endif
