print ("++++++++++++++++++++++++++++++++++++++++")
import random
num_random = random.randint( 0 , 100 )
number = 0
try :
    while number != num_random:
        number = int(input("ทายตัวเลขขอบเขต 0 - 100 : "))
        if number > num_random:
            print ("++++++++++++++++++++++++++++++++++++++++")
            print (f"เลขที่คุณทาย : {number}")
            print (f"ทายผิดแล้วเยอะเกินไป")
            print ("++++++++++++++++++++++++++++++++++++++++")
        else :
            if number < num_random:
                print (f"เลขที่คุณทาย : {number}")
                print (f"ทายผิดแล้วน้อยเกินไป")
                print ("++++++++++++++++++++++++++++++++++++++++")
            else: 
                print (f"เลขที่คุณทาย : {number}")
                print (f"ถูกต้องนะค้าบบบบ")
                print ("++++++++++++++++++++++++++++++++++++++++")
except ValueError :
    print ("กรุณาใส่ตัวเลขค่ะ")
except Exception :
    print ("มีข้อผิดพลาดกรุณาติดต่อคนเขียน")
finally :
    print ("End")