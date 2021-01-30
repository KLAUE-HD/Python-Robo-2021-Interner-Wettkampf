import time
from compLib.Motor import *
from compLib.IRSensor import IRSensor

class compLib.IRSensor.IRSensor:
        @staticmethod
        def bottom_left():
                SensorLeft 
                
        @staticmethod
        def bottom_right():
                
        @staticmethod
        def bottom_front():
        

class compLib.Motor.Motor:
        @staticmethod
        def power(port, percent):
                for port in range(0,4):
        
        @staticmethod
        def all_off():
                Motor.power(port, 0)
                Motor.power(port, 0)
                Motor.power(port, 0)
                Motor.power(port, 0)

        @staticmethod      
        def all_on():
                Motor.power(port, 0)
                Motor.power(port, 0)
                Motor.power(port, 0)
                Motor.power(port, 0)
                
    
def forward(port):
    for port in range(0, 4):
        Motor.power(port, 30);

def backward():
    for port in range(0, 4):
        Motor.power(port, -30);


IO.setup(Pin1,IO.IN) #GPIO L -> Front IR out
IO.setup(Pin2,IO.IN) #GPIO L -> Left IR out
IO.setup(Pin3,IO.IN) #GPIO L -> Right IR out

IO.setup(Pin4,IO.OUT) #GPIO L -> Motor UpRight terminal A
IO.setup(Pin5,IO.OUT) #GPIO L -> Motor UpRight terminal B

IO.setup(Pin4,IO.OUT) #GPIO L -> Motor DownRight terminal A
IO.setup(Pin5,IO.OUT) #GPIO L -> Motor DownRight terminal B

IO.setup(Pin6,IO.OUT) #GPIO L -> Motor UpLeft terminal A
IO.setup(Pin7,IO.OUT) #GPIO L -> Motor UpLeft terminal B

IO.setup(Pin6,IO.OUT) #GPIO L -> Motor DownLeft terminal A
IO.setup(Pin7,IO.OUT) #GPIO L -> Motor DownLeft terminal B

def main():
    # L => Leer (Freie Stelle zum Füllen)
    #--------------Sensor--------------#
    Pin1 = L #Front-IN
    Pin2 = L #Left-IN
    Pin3 = L #Right-IN
    #--------------Right Motor--------------#
    Pin4 = L #UpRight-OUT-A
    Pin5 = L #UpRight-OUT-B
    
    Pin8 = L #DownRight-OUT-A 
    Pin9 = L #DownRight-OUT-B
    #--------------Left Motor--------------#
    Pin6 = L #UpLeft-OUT-A
    Pin7 = L #UpLeft-OUT-B

    Pin10 = L #DownLeft-OUT-A
    Pin11 = L #DownLeft-OUT-B
    #--------------Funktion--------------#
    while(1):
        if(IO.input(Pin2)==True and IO.input(Pin3)==True): #both while move forward
                forward(port)
        #-------------------------------------------------------------------------#
            IO.output(Pin4,True) #R1_A+
            IO.output(Pin5,False) #R1_B-

            IO.output(Pin8,True) #R2_A+
            IO.output(Pin9,False) #R2_B-



            IO.output(Pin6,True) #L1_A+
            IO.output(Pin7,False) #L1_B-

            IO.output(Pin10,True) #L2_A+
            IO.output(Pin11,False) #L2_B-

        elif(IO.input(Pin2)==False and IO.input(Pin3)==True): #turn right
                
        #-------------------------------------------------------------------------#
            IO.output(Pin4,True) #R1_A+
            IO.output(Pin5,True) #R1_B+

            IO.output(Pin8,True) #R2_A+
            IO.output(Pin9,True) #R2_B+
            

            IO.output(Pin6,True) #L1_A+
            IO.output(Pin7,False) #L1_B-

            IO.output(Pin10,True) #L2_A+
            IO.output(Pin11,False) #L2_B-

        elif(IO.input(Pin2)==True and IO.input(Pin3)==False): #turn left
                
        #-------------------------------------------------------------------------#
            IO.output(Pin4,True) #R1_A+
            IO.output(Pin5,False) #R1_B-

            IO.output(Pin8,True) #R2_A+
            IO.output(Pin9,False) #R2_B-
            

            IO.output(Pin6,True) #L1_A+
            IO.output(Pin7,True) #L1_B+

            IO.output(Pin10,True) #L2_A+
            IO.output(Pin11,True) #L2_B+

        else:  #stay still
                
        #-------------------------------------------------------------------------#
            IO.output(Pin4,True) #R1_A+
            IO.output(Pin5,True) #R1_B+

            IO.output(Pin8,True) #R2_A+
            IO.output(Pin9,True) #R2_B+
            

            IO.output(Pin6,True) #L1_A+
            IO.output(Pin7,True) #L1_B+

            IO.output(Pin10,True) #L2_A+
            IO.output(Pin11,True) #L2_B+
            
main()
