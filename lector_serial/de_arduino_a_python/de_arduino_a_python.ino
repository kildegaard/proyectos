#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int16_t sensor1, sensor2, sensor3, sensor4;

void setup() {
    Serial.begin(9600);
    lcd.begin(16, 2);
}

void loop() {
    sensor1 = analogRead(A0);
    sensor2 = analogRead(A1);
    sensor3 = analogRead(A2);
    sensor4 = analogRead(A3);
    Serial.println(String(sensor1) + "," + String(sensor2) + "," + String(sensor3) + "," + String(sensor4));
    lcd.setCursor(0,0);
    lcd.print("A0: " + String(sensor1));
    lcd.print(" A1: " + String(sensor2));
    lcd.setCursor(0,1);
    lcd.print("A3: " + String(sensor3));
    lcd.print(" A4: " + String(sensor4));
    delay(1000);
}
