import servo
import math
import server
a=0
diff=0
angle=0
while 1:
    data=server.get_data()
    if data[0]==0:
        servo.servo1_set(0)
        servo.servo2_set(0)
    elif data[5]:
        if(data[2]-data[4]==0):
            continue
       # if((data[2]>data[4])and (data[1]>data[3])):
       #     angle=math.atan(((data[2]-data[4])/(data[1]-data[3])))
       # elif((data[2]>data[4])and (data[1]<data[3])):
       #     angle=math.atan(((data[4]-data[2])/(data[1]-data[3])))
        if((data[4]<data[2])and(data[3]<data[1])):
            print("case 1")
            angle=math.atan((data[4]-data[2])/(data[3]-data[1]))
            diff=(math.pi/2-angle)+data[5]*math.pi/180
        elif((data[4]<data[2])and(data[3]>data[1])):
            print("case 2")
            angle=math.atan((data[2]-data[4])/(data[3]-data[1]))
            diff=math.pi/2-((math.pi/2-angle)+data[5]*math.pi/180)
#        elif((data[4]>data[2])and(data[3]<data[1])):
  #          print("case 3")
   #         angle=math.atan((data[4]-data[2])/(data[3]-data[1]))
    #        diff=((math.pi/2-angle)+data[5]*math.pi/180)
        print(diff*180/math.pi)
#        diff=(math.pi/2-angle)+data[5]*math.pi/180
        #print(diff*180/math.pi)
        if a==0:
            g=1
            if (diff>0):
                g=g*-1
            if(data[1]<data[3]):
                g=g*-1
            if(data[2]<data[4]):
                g=g*-1
            servo.point_dir(g)
            if diff<10:
                a=1
        else:
            servo.go_dir(diff*-1)
            if((data[2]-data[4])**2+(data[1]-data[3])**2>100):
               a=0




