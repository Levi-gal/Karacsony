import os
import time
def gyertyak(x):
    os.system('cls')
    if (x==1):
        print(r"""
        
            )              
           (_)    
          .-'-.          
          |   |           
          |   |        
          |   |    
          |   |          
        __|   |__
     .-´  |   |  `-. 
    :     `---´     :
     `-._  Hit  _.-' 
         ˘˘˘˘˘˘˘         
         """)
    elif(x==2):
        print(r"""
        
            )                )
           (_)              (_)
          .-'-.            .-'-.
          |   |            |   |
          |   |            |   |
          |   |            |   |
          |   |            |   |
        __|   |__        __|   |__
     .-´  |   |  `-.  .-´  |   |  `-.
    :     `---´     ::     `---´     :
     `-._  Hit  _.-'  '-._Rem-ény_.-'
         ˘˘˘˘˘˘˘          ˇˇˇˇˇˇˇ  
         """)
    elif (x==3):
        print(r"""
        
            )                )                )
           (_)              (_)              (_)
          .-'-.            .-'-.            .-'-.
          |   |            |   |            |   |
          |   |            |   |            |   |
          |   |            |   |            |   |
          |   |            |   |            |   |
        __|   |__        __|   |__        __|   |__
     .-´  |   |  `-.  .-´  |   |  `-.  .-´  |   |  `-.
    :     `---´     ::     `---´     ::     `---´     :
     `-._  Hit  _.-'  '-._Rem-ény_.-'  '-._ Ör-öm _.-'
         ˘˘˘˘˘˘˘          ˇˇˇˇˇˇˇ          ˇˇˇˇˇˇˇ
         """)
    elif (x==4):
        print(r"""
        
            )                )                )                )
           (_)              (_)              (_)              (_)
          .-'-.            .-'-.            .-'-.            .-'-.
          |   |            |   |            |   |            |   |
          |   |            |   |            |   |            |   |
          |   |            |   |            |   |            |   |
          |   |            |   |            |   |            |   |
        __|   |__        __|   |__        __|   |__        __|   |__
     .-´  |   |  `-.  .-´  |   |  `-.  .-´  |   |  `-.  .-´  |   |  `-.
    :     `---´     ::     `---´     ::     `---´     ::     `---´     :     
     `-._  Hit  _.-'  '-._Rem-ény_.-'  '-._ Ör-öm _.-'  '-._Szeretet_.-'
         ˘˘˘˘˘˘˘          ˇˇˇˇˇˇˇ          ˇˇˇˇˇˇˇ          ˇˇˇˇˇˇˇ
         """)
    else:
        print("Többet választottál bazdmeg")


karinap = input("December hanyadika van?: ")
karinap = int(karinap)

kari = 24-karinap

print(f'\n{kari} nap van még karácsonyig\n')

input('Üss egy entert a továbblépéshez!')

if (kari<6):
    for x in range(4):
        gyertyak(x+1)
        time.sleep(1)
elif (5<kari<13):
    for x in range(3):
        gyertyak(x+1)
        time.sleep(1)
elif (12<kari<20):
    for x in range(2):
        gyertyak(x+1)
        time.sleep(1)
else :
        gyertyak(1)
        time.sleep(1)