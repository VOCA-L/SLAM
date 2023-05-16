// Encoder pin
#define ENCODER_B_A A2
#define ENCODER_B_B A3

// count, last channel value(a, b) 
int count = 0;
byte last_a;
byte last_b;
bool flag = true;

void setup() {
  // set Serial baudrate
  Serial.begin(9600);

  // set encoder's pin mode
  pinMode(ENCODER_B_A, INPUT);
  pinMode(ENCODER_B_B, INPUT);
  
  // Init last channel value(a, b)
  
  // Serial.print("Init channel a: ");
  // Serial.println(digitalRead(ENCODER_B_A));
  // Serial.print("Init channel b: ");
  // Serial.println(digitalRead(ENCODER_B_B));

}

void loop() {
  if (flag) {
    delay(3000);
    flag = false;
    last_a = digitalRead(ENCODER_B_A);
    last_b = digitalRead(ENCODER_B_B);
  }
  
  if (Serial.available()) {
    if ('s' == Serial.read()) {
      Serial.print("Count:  ");
      Serial.println(count);
    }
  }
  byte channel_a = digitalRead(ENCODER_B_A);
  byte channel_b = digitalRead(ENCODER_B_B);

  if ((channel_a != last_a) || (channel_b != last_b)) {
    count++;
    last_a = channel_a;
    last_b = channel_b;
  }

  // if ((channel_a != last_a)) {
  //   count++;
  //   Serial.print("Encoder Count:  ");
  //   Serial.println(count);
  //   last_a = channel_a;
  //   last_b = channel_b;
  // }
}
