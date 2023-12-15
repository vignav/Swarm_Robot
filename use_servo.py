import servo
import math
import server
a = 0
while 1:
    data = server.get_data()
    #print(data)
    if data[0] == 0 :
        servo.servo1_set(0)
        servo.servo2_set(0)
    elif data[5]:
        if ( data[2] - data[4] == 0  ):
            continue
        angle = math.atan(1/((data[2]-data[4])/(data[1]-data[3])))
        diff = angle + data[5]*math.pi/180
        print(diff)
        if a == 0 :
            g = 1
            if diff > 0 :
                g = g * -1

            if data[1] < data[3] :
                g = g * -1
            if data[2] < data[4] :
                g = g * -1


            servo.point_dir(g)

            if diff < 10:
                a = 1
        else :
            servo.go_dir(diff*-1)
            if (  (data[2]-data[4])**2 + (data[1]-data[3])**2 > 100 ):
                a = 0

#        print(str(data[2]-data[4]) +" "+str(data[1]-data[3]) +" "+str(angle))
#        print(data)
        #servo.servo1_set(0)
        #servo.servo2_set(0)
#        print( str((data[5]*math.pi)/180)+ " - " + str(angle) + "=" + str(((data[5]*math.pi)/180)-angle) )
#        servo.go_dir(-angle + (data[5]*math.pi)/180 - math.pi/2)
        #servo.go_dir( data[5]*math.pi/180)

'''

try:
    while 1:
        servo.go_dir(-0.07)

except KeyboardInterrupt:
        servo.servo1.value = 0
        servo.servo2.value = 0
'''
