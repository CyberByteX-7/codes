int sensor = 7;

void setup() {
  pinMode(sensor, INPUT);
  Serial.begin(9600);
}

void loop() {
  int value = digitalRead(sensor);

  if (value == HIGH) {
    Serial.println("Object Detected - Shape: Circle");
  } else {
    Serial.println("No Object - Shape: Square");
  }

  delay(1000);
}