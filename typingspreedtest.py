from time import *
import random as r

def mistake(partest, usertest):
    error =0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error +1
        except:
            error = error +1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay =time_e - time_s
    time_R =round(time_delay,2)
    speed =len(userinput)/ time_R
    return speed, time_R


while True:
    ck = input("Ready to test: y / n:")
    if ck.lower() =="y":
            test = [
            "Hello, this is a test message.",
            "It contains multiple sentences.",
            "Let's see how it works.",
            "This is the end of the test."
    ]
            test1 = r.choice(test) 

            print("***** Typing Speed Test *****")
            print()
            print(test1)
            print()

            time_1 =time()
            testinput =input("Enter: ")
            time_2 =time()


            print ("Speed: ",speed_time(time_1, time_2, testinput), "w/sec")
            print("Mistake: ", mistake(test1, testinput))

    elif ck.lower() =="n":
         print("Text exit, Thak you")
         break
    else:
         print("Please enter y or n")
 

