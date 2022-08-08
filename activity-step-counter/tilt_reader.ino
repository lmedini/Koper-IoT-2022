//  Author: Niki Hrovatin
//  e-mail: niki.hrovatin@famnit.upr.si
//  Date: 08.08.2022
//  Activity detector developed on the workshop Koper-IoT-2022 held at InnoRenewCoe in Izola.



int ledPin = 8;         // global variable - defines the pin number
int front = 13;
int rear = 12;
int val_front = 0;
int val_rear = 0;
int delta_bucket = 10; //millis
int count_front=0;
int count_rear=0;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);        // sets the digital pin as output
  pinMode(front, INPUT);        // sets the digital pin as in
  pinMode(rear, INPUT);        // sets the digital pin as in
}

void loop() {

  collect_data();
  //Serial.print("front:");
  Serial.print(count_front);
  Serial.print(",");
  Serial.println(count_rear);
  
  
  
}

//for each sensor count the number of times the signal is HIGH in 10ms
//when the signal is HIGH open also the LED attached to the breadboard

void collect_data(){
  long int t1 = millis();
  long int t2 = millis();
  count_front=0;
  count_rear=0;
  while(t1+delta_bucket>t2){
    val_front = digitalRead(front);
    val_rear = digitalRead(rear);
    if(val_front == 1 || val_rear == 1 ){ // just open the LED
      digitalWrite(ledPin, HIGH);     // 5V    
      if(val_front == 1){
        count_front++;
      }
      if(val_rear == 1){
        count_rear++; 
      }
    }else{
      digitalWrite(ledPin, LOW);      // 0V
    }
    t2 = millis();
  }
}
