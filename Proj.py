#FINAL CODE
import csv
import time
import datetime
import random
global movnam
global details
global seats
details=[]
seats=[]
movnam=' '                                                                     
sm=[['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10'],
    ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10'],
    ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10'],
    ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10'],
    ['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10'],
    ['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10'],
    ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10'],
    ['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10'],
    ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10']]

def menu1(): #LOGIN MENU
    print("\n\t\t\t +--------------+")
    print("\t\t\t |   1.SIGNUP   |")
    print("\t\t\t |   2.LOGIN    |")
    print("\t\t\t +--------------+")
    choice=int(input("Enter your choice: "))
    if choice==1:
        Signup()
    elif choice==2:
        login()
    else:
        print("Wrong input")
        menu1()
        

def sup(): #Signup information
    print("-"*188)
    name1 = input("Enter first name: ")
    name2 = input("Enter last name: ")
    gnd = input("Enter your gender: ")
    uname =input("Enter your valid mail ID: ")
    fh=open("user.csv","r",newline="")
    s=csv.reader(fh)
    for rec in s:
        if uname==rec[3]:
            print("Username already exists!! Login instead")
            print("1.Signup again?")
            print("2.Login instead")
            ch=int(input("Enter your choice: "))
            if ch==1:
                Signup()
            elif ch==2:
                login()
            else:
                print("Wrong input")
        else:
            continue
    while True:
        psswd = input("Enter password: ")
        psswd2 = input("Confirm password: ")
        if psswd == psswd2:
            break
        else:
            print("PASSWORDS DO NOT MATCH!")
    phn = input("Enter mobile no: ")
    if len(phn)!= 10:
        phn = input("Enter valid mobile no: ")
    else:
        print("Valid phone no")
    rec=[name1,name2,gnd,uname,psswd,phn]
    return rec
    print(rec)
            
def Signup():  #Signup
    fh=open("user.csv","a",newline="")
    l=sup()
    s=csv.writer(fh)
    s.writerow(l)
    fh.close()
    print("SIGNED UP SUCCESSFULLY")
    print("-"*188)
    c = input('DO YOU WANT TO LOGIN : ')
    if c in 'yY':
        menu1()
    elif c in 'nN':
        print("Thank you!! See you again!!")
        print("-"*188)
        pass

def login():  #Login
    print("-"*188)
    x=0
    uname=input("Enter your user name: ")
    pswd=input("Enter your password: ")
    try:
        while True:
            fh=open("user.csv","r",newline="\r\n")
            s=csv.reader(fh)
            for rec in s:
                if rec==[]:
                    continue
                elif rec[3]==uname and rec[4]==pswd:
                    x=1
                    details.append(rec)
                    break
                elif rec[3]==uname and rec[4]!=pswd:
                    x=2
                    break
                elif rec[3]!=uname:
                    x=3
                    continue
            if x==1:
                print("Hello",rec[0]+' '+rec[1],". Your have successfully login to our system")
                menu2()
                break
            elif x==2:
                print("Incorrect password")
                ans=input("Do you want to login again(y/n):")
                if ans.lower()=='y':
                    login()
                break
            elif x==3:
                print("User doesnt exist\n 1.Login again\n 2.Register account")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    login()
                elif choice==2:
                    Signup()
                elif choice!=1 and choice!=2:
                    print("Wrong input")
                    continue
                break
            
    except:
        fh.close()

        
def menu2():  #MAIN MENU
    print("-"*188)
    c=0
    z=0
    while z==0:
        print("""\n\t\t\t|------------------------------------------|
\t\t\t|               MAIN MENU                  |
\t\t\t|               ---- ----                  |
\t\t\t|1. SEARCH/BOOK UPCOMING/RELEASED MOVIES   |
\t\t\t|2. CANCEL BOOKING                         |
\t\t\t|3. SUPPORT                                |
\t\t\t|4. FEEDBACK                               |
\t\t\t|5. EXIT                                   |
\t\t\t|------------------------------------------|""")
        c=int(input("\n\t\t   ENTER YOUR CHOICE :-   "))
        if c==1:
            search()
        elif c==2:
            cancel()
        elif c==3:
            support()
            c=input('\n\t\t\tDO YOU WANT TO EXIT : ')
            if c=='y' or c=='Y':
                ex()
                break
        elif c==4:
            feed()
            c=input('\n\t\t\tDO YOU WANT TO EXIT : ')    
            if c=='y' or c=='Y':
                ex()
                break
        elif c==5:
            ex()
            z=1
        else:
            print('\n\t\t\t###INVALID CHOICE###\n')
            menu2()
    
        

def search():  #to search movies
    print("-"*188)
    s1=0
    while True:
        print( """\t\t\t   +-------------------------+
\t\t\t   |     SEARCH FOR MOVIES   |
\t\t\t   |     ------ --- ------   |
\t\t\t   +-------------------------+
\t\t\t   |1. UPCOMING              |
\t\t\t   |2. NOW SHOWING           |  
\t\t\t   |3. GO BACK               |
\t\t\t   +-------------------------+\n""")
        s1=int(input('\t\t    SEARCH FOR ? '))
        if s1==1:
            upcoming()
        elif s1==2:
            now_showing()
        elif s1==3:
            break
        else:
            print('\n\t\t\t ###INVALID CHOICE###\n')
    


def upcoming():  #to display upcoming movies
    print("-"*188)
    inp1=0                                              #Select Language
    while True:
        print("""\t\t\t   |---------------------------|
\t\t\t   |        LANGUAGE           |
\t\t\t   |        --------           |
\t\t\t   |---------------------------|
\t\t\t   |1. ENGLISH                 |
\t\t\t   |2. HINDI                   |  
\t\t\t   |3. GO BACK                 |
\t\t\t   |---------------------------|\n""")
        inp1=int(input('\t\t   SELECT LANGUAGE : '))
        if inp1==1:
            inp2=0                                      #Select Category of movies
            while True:
                print("-"*188)
                print("""\n\t\t\t   |---------------------------|
\t\t\t   |        CATEGORY           |
\t\t\t   |        --------           |
\t\t\t   |---------------------------|
\t\t\t   |1. HORROR                  |
\t\t\t   |2. ACTION                  |
\t\t\t   |3. COMEDY                  |  
\t\t\t   |4. GO BACK                 |
\t\t\t   |---------------------------|\n""")
                inp2=int(input('\t\t   SELECT CATEGORY : '))
                if inp2==1:
                    inp3=0                              #Select movie
                    while True:
                        print("-"*188)
                        print("""\t\t\t   |-----------------------------------|
\t\t\t   | UPCOMING ENGLISH HORROR  MOVIES   |
\t\t\t   | -------- ------- ------  ------   |
\t\t\t   |-----------------------------------|
\t\t\t   |* SCREAM                           |
\t\t\t   |* ORPHAN: FIRST KILL               |
\t\t\t   |* MORBIUS                          |
\t\t\t   |1. GO BACK                         |
\t\t\t   |-----------------------------------|\n""")
                        inp3=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if inp3==1:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                         
                elif inp2==2:
                    inp3=0
                    while True:
                        print("-"*188)
                        print("""\t\t\t   |--------------------------------|
\t\t\t   | UPCOMING ENGLISH ACTION MOVIES |
\t\t\t   | -------- ------- ------ ------ |
\t\t\t   |--------------------------------|
\t\t\t   |* MISSION IMPOSSIBLE 7          |
\t\t\t   |* AVATAR 2                      |
\t\t\t   |* JURASSIC WORLD                |
\t\t\t   |1. GO BACK                      |
\t\t\t   |--------------------------------|\n""")
                        inp3=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if inp3==1:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                        
                elif inp2==3:
                    inp3=0
                    while True:
                        print("-"*188)
                        print("""\t\t\t   |--------------------------------|
\t\t\t   | UPCOMING ENGLISH COMEDY MOVIES |
\t\t\t   | -------- ------- ------ ------ |
\t\t\t   |--------------------------------|
\t\t\t   |* MARRY ME                      |
\t\t\t   |* THE BAD GUYS                  |
\t\t\t   |* LEGALLY BLONDE 3              |  
\t\t\t   |1. GO BACK                      |
\t\t\t   |--------------------------------|\n""")
                        inp3=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if inp3==1:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')

                elif inp2==4:
                    break
                else:
                    print("\t\t\t###INVALID CHOICE###\n")
                              
        elif inp1==2:
            inp2=0
            while True:
                print("-"*188)
                print("""\t\t\t   |---------------------------|
\t\t\t   |        CATEGORY           |
\t\t\t   |        --------           |
\t\t\t   |---------------------------|
\t\t\t   |1. HORROR                  |
\t\t\t   |2. ACTION                  |
\t\t\t   |3. COMEDY                  |  
\t\t\t   |4. GO BACK                 |
\t\t\t   |---------------------------|\n""")
                inp2=int(input('\t\t   SELECT CATEGORY : '))
                if inp2==1:
                    inp3=0
                    while True:
                        print("""\t\t\t   |-----------------------------------|
\t\t\t   |   UPCOMING HINDI HORROR MOVIES    |
\t\t\t   |   -------- ----- ------ ------    |
\t\t\t   |-----------------------------------|
\t\t\t   |* BHEDIYA                          |
\t\t\t   |* ROCKET GANG                      |
\t\t\t   |* BHOOL BHULAIYAA 2                |
\t\t\t   |1. GO BACK                         |
\t\t\t   |-----------------------------------|\n""")
                        inp3=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if inp3==1:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                    
                elif inp2==2:
                    inp3=0
                    while True:
                        print("-"*188)
                        print("""\t\t\t   |-------------------------------|
\t\t\t   | UPCOMING HINDI ACTION MOVIES  |
\t\t\t   | -------- ----- ------ ------  |
\t\t\t   |-------------------------------|
\t\t\t   |*  RRR                         |
\t\t\t   |*  ATTACK                      |
\t\t\t   |*  BACHCHAN PANDEY             |
\t\t\t   |1. GO BACK                     |
\t\t\t   |-------------------------------|\n""")
                        inp3=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if inp3==1:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                    
                elif inp2==3:
                    inp3=0
                    while inp3!=4:
                        print("-"*188)
                        print("""\t\t\t   |--------------------------------|
\t\t\t   | UPCOMING HINDI COMEDY MOVIES   |
\t\t\t   | -------- ----- ------ ------   |
\t\t\t   |--------------------------------|
\t\t\t   |* BADHAAI DO                    |
\t\t\t   |* CIRCUS                        |
\t\t\t   |* BHOOL BHULAIYAA 2             |  
\t\t\t   |1. GO BACK                      |
\t\t\t   |--------------------------------|\n""")
                        inp3=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if inp3==1:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                    
                elif inp2==4:
                     break
                else:
                    print('\t\t\t###INVALID CHOICE###\n')
                    
        elif inp1==3:
             break
        else:
             print('\t\t\t###INVALID CHOICE###\n')
        


def options():
    print("-"*188)
    print("""\t\t\t   +-------------------------------+
\t\t\t   |       OPTIONS                 |
\t\t\t   |       -------                 |
\t\t\t   +-------------------------------+
\t\t\t   |1. BOOK THIS MOVIE             |
\t\t\t   |2. GO BACK                     |
\t\t\t   +-------------------------------+\n""")

def now_showing():  #to display now_showing movies
    print("-"*188)
    s2=0
    while True:
        print ("""\t\t\t   +---------------------------+
\t\t\t   |        LANGUAGE           |
\t\t\t   |        --------           |
\t\t\t   +---------------------------+
\t\t\t   |1. ENGLISH                 |
\t\t\t   |2. HINDI                   | 
\t\t\t   |3. GO BACK                 |
\t\t\t   +---------------------------+\n""")
        s2=int(input('\t\t   SELECT LANGUAGE : '))
        if s2==1:
            s3=0
            while True:
                print("-"*188)
                print ("""\t\t\t   +---------------------------+
\t\t\t   |        CATEGORY           |
\t\t\t   |        --------           |
\t\t\t   +---------------------------+
\t\t\t   |1. HORROR                  |
\t\t\t   |2. ACTION                  |
\t\t\t   |3. COMEDY                  |   
\t\t\t   |4. GO BACK                 |
\t\t\t   +---------------------------+\n""")
                s3=int(input('\t\t   SELECT CATEGORY : '))
                if s3==1:
                    s4=0
                    while True:
                        print("-"*188)
                        print ("""\t\t\t   +-----------------------------------+
\t\t\t   |     NOW SHOWING HORROR MOVIES     |
\t\t\t   |     --- ------- ------ ------     |
\t\t\t   +-----------------------------------+
\t\t\t   |1. SCREAM                          |
\t\t\t   |2. MORBIUS                         | 
\t\t\t   |3. ORPHAN: FIRST KILL              |
\t\t\t   |4. GO BACK                         |
\t\t\t   +-----------------------------------+\n""")
                        
                        s4=int(input('\t\t   ENTER YOUR MOVIE CHOICE : '))
                        if s4==1:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Scream'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                                        
                        elif s4==2:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Morbius'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                               
                        elif s4==3:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Orphan: First Kill'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                          
                        elif s4==4:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                                           
                elif s3==2:
                    s4=0
                    while True:
                        print("-"*188)
                        print ("""\t\t\t   +--------------------------+
\t\t\t   | NOW SHOWING ACTION MOVIES |
\t\t\t   | --- ------- ------ ------ |
\t\t\t   +---------------------------+
\t\t\t   |1. SPIDERMAN: NO WAY HOME  |
\t\t\t   |2. FAST AND FURIOUS 10     |
\t\t\t   |3. DANGEROUS               |
\t\t\t   |4. GO BACK                 |
\t\t\t   +---------------------------+\n""")
                        s4=int(input('\t\t   ENTER YOUR CHOICE : '))
                        s5=0
                        if s4==1:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Spiderman: No Way Home'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                            
                        elif s4==2:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Fast and Furious 10'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\n\t\t\t###INVALID CHOICE###\n')
                                                            
                        elif s4==3:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam="Dangerous"
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                            
                        elif s4==4:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                       
                elif s3==3:
                    s4=0
                    while s4!=4:
                        print("-"*188)
                        print ("""\t\t\t   +--------------------------+
\t\t\t   |  NOW SHOWING COMEDY MOVIES  |
\t\t\t   |  --- ------- ------ ------  |
\t\t\t   +-----------------------------+
\t\t\t   |1. THE FRENCH DISPATCH       |
\t\t\t   |2. LUCA                      |
\t\t\t   |3. HOLMES AND WATSON         |   
\t\t\t   |4. GO BACK                   |
\t\t\t   +-----------------------------+\n""")
                        s4=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if s4==1:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam="The French Dispatch"
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                           
                        elif s4==2:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Luca'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                            
                        elif s4==3:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Holmes and Watson'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                    
                        elif s4==4:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICE###\n')
                                            
                elif s3==4:
                    break
                else:
                    print('\t\t\t###INVALID CHOICE###\n')
                                   
        elif s2==2:
            s3=0
            while True:
                print("-"*188)
                print ("""\t\t\t   +---------------------------+
\t\t\t   |        CATEGORY           |
\t\t\t   |        --------           |
\t\t\t   +---------------------------+
\t\t\t   |1. HORROR                  |
\t\t\t   |2. ACTION                  |
\t\t\t   |3. COMEDY                  |   
\t\t\t   |4. GO BACK                 |
\t\t\t   +---------------------------+\n""")
                s3=int(input('\t\t   SELECT CATEGORY : '))
                if s3==1:
                    s4=0
                    while True:
                        print("-"*188)
                        print("""\t\t\t   +-----------------------------------+
\t\t\t   |    NOW SHOWING HORROR MOVIES      |
\t\t\t   |    --- ------- ------ ------      |
\t\t\t   +-----------------------------------+
\t\t\t   |1. STREE 2                         |
\t\t\t   |2. PHONE BHOOT                     |
\t\t\t   |3. RAAZ REBOOT AGAIN               |
\t\t\t   |4. GO BACK                         |
\t\t\t   +-----------------------------------+\n""")
                        s4=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if s4==1:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED:'))
                                if s5==1:
                                    movnam='Stree 2'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###a\n')
                                                                   
                        elif s4==2:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Phone Bhoot'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t ###INVALID CHOICE###\n')
                                                            
                        elif s4==3:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED: '))
                                if s5==1:
                                    movnam='Raaz Reboot Again'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                                    
                        elif s4==4:
                            break
                        else:
                            print('\t\t\t###INVALID CHOICEa###\n')
                                            
                elif s3==2:
                    s4=0
                    while True:
                        print("-"*188)
                        print ("""\t\t\t   +--------------------------+
\t\t\t   |   NOW SHOWING ACTION MOVIES   |
\t\t\t   |   --- ------- ------ ------   |
\t\t\t   +-------------------------------+
\t\t\t   |1. SHAMSHERA                   |
\t\t\t   |2. HIT: THE FIRST CASE         |
\t\t\t   |3. ADIPURUSH                   |
\t\t\t   |4. GO BACK                     |
\t\t\t   +-------------------------------+\n""")
                        s4=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if s4==1:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Shamshera'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                      break 
                                else:
                                    print('\t\t\t###INVALID CHOICE###\n')
                                                            
                        elif s4==2:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Hit: The First Case'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t ###INVALID CHOICE###\n')
                                                            
                        elif s4==3:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED :'))
                                if s5==1:
                                    movnam='Adipurush'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t ###INVALID CHOICE###\n')
                                                            
                        elif s4==4:
                            break
                        else:
                            print('\t\t\t ###INVALID CHOICE###\n')
                                            
                if s3==3:
                    s4=0
                    while True:
                        print("-"*188)
                        print ("""\t\t\t   +------------------------------+
\t\t\t   |  NOW SHOWING COMEDY MOVIES  |
\t\t\t   |  --- ------- ------ ------  |
\t\t\t   +-----------------------------+
\t\t\t   |1. DOCTOR G                  |
\t\t\t   |2. DESI MAGIC                |
\t\t\t   |3. PLAN B                    |   
\t\t\t   |4. GO BACK                   |
\t\t\t   +-----------------------------+\n""")
                        s4=int(input('\t\t   ENTER YOUR CHOICE : '))
                        if s4==1:
                            while True:
                                options()
                                s5=int(input('\n\t\t   SELECT AN OPTION TO PROCEED : '))
                                if s5==1:
                                    movnam='Doctor G'
                                    details.append(movnam)
                                    book()
                                elif s5==2: 
                                    break
                                else:
                                    print('\t\t ###INVALID CHOICE###\n')
                                                            
                        elif s4==2:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED : '))
                                if s5==1:
                                    movnam='Desi Magic'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                      break                              
                                else:
                                    print('\t\t\t ###INVALID CHOICE###\n')
                                                           
                        elif s4==3:
                            while True:
                                options()
                                s5=int(input('\t\t   SELECT AN OPTION TO PROCEED : '))
                                if s5==1:
                                    movnam='Plan B'
                                    details.append(movnam)
                                    book()
                                elif s5==2:
                                    break
                                else:
                                    print('\t\t\t ###INVALID CHOICE###\n')
                                                            
                        elif s4==4:
                            break
                        else:
                            print('\t\t\t ###INVALID CHOICE###\n')
                            
                elif s3==4:
                    break
                else:
                    print('\t\t\t ###INVALID CHOICE###\n')
                    
        elif s2==3:
            break
        else:
            print('\t\t\t ###INVALID CHOICEc###\n')


def book(): #to confirm booking
    print("-"*188)
    ch=input('\t\t\t DO YOU WANT TO BOOK THIS MOVIE (Y/N) : ')
    if ch=='y' or ch=='Y':
        venue()
        pay()
        ticket()
        exit()
        
def ddate(): #to book movie on valid date
   k=time.localtime()
   while True:
       print("-"*188)
       date=input('\t\t\t  CHOOSE YOUR SHOW DATE (DD/MM/YYYY)     : ')
       print('\t\t\t','..'*26,'\n')
       spl=date.split('/')
       if spl[2]!=str(k[0]):                                       # Invalid year checking
           print('\t\t\t INVALID SHOW DATE(Incorrect year)!\n')
       elif int(spl[1])<k[1] or int(spl[1])>k[1]:                  #Invalid month checking
           print('\t\t\t INVALID SHOW DATE(Incorrect month)!\n')
       elif int(spl[1])== k[1]:
           if k[2]>int(spl[0]) or k[2]==int(spl[0]):               #If local date is > than show date
               print('\t\t\t SHOW IS NOT AVAILABLE ON THIS DATE!\n')
           elif int(spl[0])>k[2]:                                  #if show date is > than local date
               break
       else:
           break
   day, month, year = (int(x) for x in date.split('/'))    
   ans = datetime.date(year, month, day)
   day=ans.strftime("%A").upper()
   return [date,day]

def stc(sm):  #to choose caetgory,seat
    cost=0
    l=sm
    ch=' '
    while ch!='n' or ch!='N':
        print("-"*188)
        print('\t\t         ________________________________________________')
        print('\t\t        /   __________________________________________   \ ')
        print('\t\t        |  |                                          |  | ')
        print('\t\t        |  |        			              |  | ')
        print('\t\t        |  |         ALL EYES THIS WAY PLEASE         |  | ')
        print('\t\t        |  |                                          |  | ')
        print('\t\t        |  |__________________________________________|  | ')
        print('\t\t        \________________________________________________/ \n\n')

        s=' '
        for i in range(9):
            print("\t\t\t\t",end=" ")
            for j in range(10):
                print(sm[i][j],end=" ")
            print()
        print()
                            
        print("\t\t\t","_"*43)
        print('\t\t\t ** : NOT AVAILABLE ')
        print('\t\t\tA-F : NORMAL ')
        print('\t\t\t S  : SILVER ')
        print('\t\t\t G  : GOLD ')
        print('\t\t\t P  : PLATINUM ')
        print("\t\t\t","_"*43)
        print("\t\t\t+","+"*20,"+")
        print('\t\t\t+  COST PER SEAT       +')
        print("\t\t\t+","-"*20,"+")
        print('\t\t\t+  NORMAL   : Rs.150   +')
        print('\t\t\t+  SILVER   : Rs.200   +')
        print('\t\t\t+  GOLD     : Rs.250   +')
        print('\t\t\t+  PLATINUM : Rs.300   +')
        print("\t\t\t+","+"*20,"+")
        while True:
            n=int(input('\t\t\tHOW MANY SEATS DO YOU WANT : '))
            if n>10:
                print('\t\t\t---YOU CAN BOOK A MAXIMUM OF 10 SEATS!---')
                
            elif n>0 and n<=10:
                break
            else:
                print('\n\t\t\t---INVALID INPUT!---\n')
        pt,au,ag,nrm=0,0,0,0
        for k in range(n):
            while True:
                print('\n\t\t\tSEAT            : ',k+1)
                c=input('\n\t\t\tCHOOSE CATEGORY : '.upper())
                if c=='p' or c=='P':
                    pt+=1
                    cost+=300
                    break
                elif c=='g' or c=='G':
                    au+=1
                    cost+=250
                    break
                elif c=='s' or c=='S':
                    ag+=1
                    cost+=200
                    break
                elif c in 'abcdef' or c in 'ABCDEF':
                    nrm+=1
                    cost+=150
                    break
                else:
                    print('\n\t\t\t ### SEAT CATEGORY NOT AVAILABLE ###')
                    continue
            sref=0
            while True:
                s=input('\n\t\t\tCHOOSE THE SEAT : '.upper())
                for i in l:
                    for j in i:
                        if j==s:
                            sref=1
                if s[0]!=c:
                    print('\n\t\t\t---INVALID SEAT---\n')
                    continue
                elif sref==0:
                    print('\n\t\t\t---SEAT NOT FOUND---\n' )
                elif sref==1:
                    break
            seats.append(s)
            for i in range(9):
                for j in range(10):
                    if l[i][j]==s:
                        l[i][j]='**'
                        break
        sm=l
        print("-"*188)
        ch=input('\t\t    DO YOU WANT TO BOOK MORE SEATS (Y/N) : ')
        print('\t\t','--'*30)
        if ch=='N' or ch=='n':
            print('\n\n\t\t\t    -=>BOOKED SEATS : ** \n')
            print('\t\t         ________________________________________________')
            print('\t\t        /   __________________________________________   \ ')
            print('\t\t        |  |                                          |  | ')
            print('\t\t        |  |        			              |  | ')
            print('\t\t        |  |         ALL EYES THIS WAY PLEASE         |  | ')
            print('\t\t        |  |                                          |  | ')
            print('\t\t        |  |__________________________________________|  | ')
            print('\t\t        \________________________________________________/ \n\n')

            for  i in range(9):
                print("\t\t\t\t",end=" ")
                for j in range(10):
                    print(sm[i][j],end=" ")
                print()
            print()
            break
        else:
            pass
    return [cost,seats]

def venue():  #to select venue, show timing
    udet=[]
    ddt=ddate()  #d[date,day]
    date=ddt[0]
    day=ddt[1]
    print("\t\t\t+"+"-"*50+"+")
    print("\t\t\t1. DT Cinemas: DLF Place, Saket                    +".upper())
    print("\t\t\t+"+".."*25+"+")
    print("\t\t\t2. Cinepolis: Unity One Mall Rohini, Delhi         +".upper())
    print("\t\t\t+"+".."*25+"+")
    print("\t\t\t3. Cinepolis: Grand Venice Mall, Greater Noida     +".upper())
    print("\t\t\t+"+"-"*50+"+")
    plc=["DT Cinemas: DLF Place, Saket\t\t  ".upper(),"Cinepolis: Unity One Mall Rohini, Delhi    ".upper(),"Cinepolis: Grand Venice Mall, Greater Noida".upper()]
    h=int(input("\n\t\t\t>>> Choose Your Desired Venue : "))
    udet.append(plc[h-1])
    while True:
        print("-"*188)
        if h==1:
            print("\t\t\t    |--------------------|")
            print("\t\t\t    |     SHOW TIMINGS   |")
            print("\t\t\t    |     ---- -------   |")
            print("\t\t\t    |--------------------|")
            print("\t\t\t    |1. 10:00 AM         |")
            print("\t\t\t    |2. 05:00 PM         |")
            print("\t\t\t    |3. 08:30 PM         |")
            print("\t\t\t    |--------------------|\n")
            tm=["10:00 AM","05:00 PM","08:30 PM"]
            j=int(input("\n\t\t\t Select Your Show Timings     : "))
            if j>3 or j==0:
                print('\n\t\t\t >>>INVALID CHOICE!<<<\n')
                continue
            else:
                udet.append(tm[j-1])
                break
            
        
        elif h==2:
            print("\t\t\t|--------------------|")
            print("\t\t\t|     SHOW TIMINGS   |")
            print("\t\t\t|     ---- -------   |")
            print("\t\t\t|--------------------|")
            print("\t\t\t|1. 11:25 AM         |")
            print("\t\t\t|2. 03:26 PM         |")
            print("\t\t\t|3. 05:45 PM         |")
            print("\t\t\t|4. 08:33 PM         |")
            print("\t\t\t|--------------------|\n")
            tm=["11:25 AM","03:26 PM","05:45 PM","08:33 PM"]
            j=int(input("\n\t\t\t Select Your Show Timings     : "))
            if j>4 or j==0:
                print('\n\t\t\t >>>INVALID CHOICE!<<<\n')
                continue
            else:
                udet.append(tm[j-1])
                break
        elif h==3:
            print("\t\t\t|--------------------|")
            print("\t\t\t|     SHOW TIMINGS   |")
            print("\t\t\t|     ---- -------   |")
            print("\t\t\t|--------------------|")
            print("\t\t\t|1. 10:32 AM         |")
            print("\t\t\t|2. 11:56 AM         |")
            print("\t\t\t|3. 01:11 PM         |")
            print("\t\t\t|4. 04:40 PM         |")
            print("\t\t\t|5. 07:55 PM         |")
            print("\t\t\t|--------------------|\n")
            tm=["10:32 AM","11:56 AM","01:11 PM","04:40 PM","07:55 PM"]
            j=int(input("\n\t\t Select Your Show Timings     : "))
            if j>5 or j==0:
                print('\n\t\t\t\t\t >>>INVALID CHOICE!<<<\n')
                continue
            else:
                udet.append(tm[j-1])
                break

        elif h not in [1,2,3]:
             print('\n\t\t\t >>>INVALID CHOICE!<<<\n')
             h=int(input("\n\t\t\t>>> Choose Your Desired Venue : ".upper()))
              
    """udet=["place","show timing",["cost","seats"]]
       details=[[name1,name2,gnd,uname,psswd,phn],movnam,
         ["place","show timing",["cost","seats"],["showdate","showday"]],"ticket-type","bookingid"]"""
    
    t=time.localtime()
    st=stc(sm)
    cost=st[0]
    udet.append(st)
    udet.append(ddt)
    details.append(list(udet))

    print("\n\n\t\t","+"*67)
    print('\t\t| \t\t\tBOOKING SUMMARY',' '*29,'|')
    print("\t\t+","-"*67,"+")
    print('\t\t   -=> NAME            :',details[0][0],details[0][1])
    print('\t\t   -=> EMAIL ID        :',details[0][3])
    print('\t\t   -=> MOBILE          :',details[0][5])
    print('\t\t   -=> MOVIE           :',details[1])
    print('\t\t   -=> PLACE           :',udet[0])
    print('\t\t   -=> SEAT(S)         :',end=" ")
    for i in range(len(st[1])):
        print(st[1][i],",",end='')
    print("\n\t\t   -=> COST            :",st[0])
    print('\t\t   -=> SHOW DATE       :',date)
    print('\t\t   -=> DAY             :',day)
    print('\t\t   -=> BOOKING DATE    :',t[2],'/',t[1],'/',t[0])
    print('\t\t   -=> SHOW TIMINGS    :',udet[1])
    print('\t\t   -=> TAX (GST)       :','Rs.',float(0.1)*cost)
    
def pay():  #payment methods
    print("-"*188)
    a=0
    while a!=4 or a!=5:
        bytckt() #text art
        print ("""\t\t\t+==========================================+
\t\t\t| *  PAYMENT OPTIONS                       |
\t\t\t|==========================================|
\t\t\t| 1. Credit/Debit Card                     |
\t\t\t| 2. Net Banking                           |
\t\t\t| 3. Paytm                                 |
\t\t\t| 4. CANCEL PAYMENT AND BACK TO MAIN MENU  |
\t\t\t+==========================================+""")
        a=int(input("\t\t\tEnter Your Payment Mode : ".upper()))
        if a==1: 
            credeb()            
            c=input('\t\t\tDO YOU WANT TO PROCEED (Y/N) : ')
            if c=='y' or c=='Y':
                break      
            else:
                pass
        elif a==2:
            bnkp()#text art 
            netbanking()
            c=input('\n\t\t\tDO YOU WANT TO PROCEED (Y/N) : ')
            if c=='y' or c=='Y':
                break
                
        elif a==3:
            print("-"*188)
            print('\t\t\t*****PAYTM TRANSACTION MODE*****\n')
            p=0
            while len(str(p))!=10:
                p=input('\n\t\t\tENTER YOUR PHONE NO. : ')
                if len(str(p))==10:
                    break
                else:
                    print('\t\t\t----PLEASE ENTER YOUR VALID PHONE NO.! ----')
            h=input("\n\t\t\tEnter Your Valid Paytm Number  : ".upper())
            c=input('\t\t\tDO YOU WANT TO PROCEED (Y/N) : ')
            if c=='y' or c=='Y':
                break
        elif a==4:
            menu2()
            details.remove()
        else:
            print("\t\tWrong input!!")
            
           
def credeb():  #credit card payment
    print("-"*188)
    while True:
        cno=input("\t\t\tENTER CREDIT CARD/DEBIT CARD NO. :-  ")
        c=len(str(cno))
        if c==16:
            break
        else:
            print("\t\t\t-----INVALID CREDIT/DEBIT CARD NO!-----")
    while True:        
        cvv=input("\t\t\tENTER THE CVV NO. :-  ")
        c=len(str(cvv))
        if c==3:
            break
        else:
            print("\t\t\tINVALID CVV NO")
    while True:
        pin=input("\t\t\tENTER YOUR PIN :-  ")
        p=len(str(pin))
        if p==4:
            break
        else:
            print("\t\t\tINVALID PIN")

def netbanking():  #netbanking payment method
    print("-"*188)
    bname=input("\t\t\t -> BANK NAME    :-  ")
    bid=input("\t\t\t -> USER ID      :-  ")
    bpas=input("\t\t\t -> PASSWORD     :-  ")

def addbook():  #to add booking details to csv file
    a=open("bookings.csv","a+",newline="")
    s=csv.writer(a)
    s.writerow(details)
    a.close()
    menu2()

def ticket(): #to generate ticket
    print("-"*188)
    while True:
        print("""\t\t\t  +----------------------+
\t\t\t  |      TICKET TYPE     |
\t\t\t  |      ------ ----     |
\t\t\t  |1. E-TICKET           |
\t\t\t  |2. BOX-OFFICE PICKUP  |
\t\t\t  +----------------------+\n""")
        c=int(input('\t\t\t -=> SELECT TICKET TYPE : '))        
        if c==1:
            print("""\n\t\t\t--------------------------------------------------------------------
\t\t\t   ***E-TICKET***
\t\t\t--------------------------------------------------------------------
\t\t\t-> Download the e-ticket on your mobile to enter the cinema and show your booking id.
\t\t\t-> No PrintOut Needed.
\t\t\t-> Entry will not be provided without showing booking id\n""")
            details.append('E-TICKET')
            break
        
        elif c==2:
            print("""\n\t\t\t---------------------------------------
\t\t\t ***BOX-OFFICE PICKUP***
\t\t\t---------------------------------------
\t\t\t -> COLLECT THE TICKETS FROM BOX OFFICE\n""")
            details.append('BOX-OFFICE PICKUP')
            break        
        else:
            print('\n\t\t\t\t\t---INVALID CHOICE!---')
     
    print('\t\t\t PAYMENT MADE SUCCESSFULLY ')
    print('\t\t\t YOUR TICKETS ARE BOOKED :) ')


    bookingid=str(random.randint(1000,9999))
    print("\t\t >>>>>>BOOKING ID(Confidential!!Do not share with anyone!) : ",bookingid,"<<<<<<")
    details.append(bookingid)
    addbook()
    print("-"*188)
    
def cancel():  #cancel ticket
    print("-"*188)
    """details=[[name1,name2,gnd,uname,psswd,phn],"movnam",
         ["place","show timing",["cost","seats"],["showdate","showday"]],"ticket-type","bookingid"]"""
    lines=list()
    date=input('\t\t\t ENTER THE DATE ON WHICH YOU BOOKED THE MOVIE (DD/MM/YYYY) : ')
    x=time.localtime()
    y=date.split('/')
    if y[0]!=str(x[2]) and y[1]!=str(x[1]) and y[2]!=str(x[0]):
        print('\n\t\t\t### SORRY! YOU CAN NOT CANCEL YOUR BOOKING. :-(              ###')   
        print('\n\t\t\t### BOOKING CAN BE CANCELLED ONLY ON THE SAME DAY OF BOOKING ###')
    
    elif y[0]==str(x[2]) and y[1]==str(x[1]) and y[2]==str(x[0]):
        bookid=input("Enter your booking id: ")
        with open("bookings.csv","r",newline="\r\n") as fh:
            rd_obj=csv.reader(fh)
            for row in rd_obj:
                lines.append(row)
                if row[4]==bookid:
                    lines.remove(row)
                    print("Booking record sucessfully deleted")
                else:
                    continue
                

        with open("bookings.csv","w",newline="") as fh:
            w_obj=csv.writer(fh)
            w_obj.writerows(lines)
    else:
        print('\n\t\t\t### SORRY! YOU CAN NOT CANCEL YOUR BOOKING. :-(              ###')   
        print('\n\t\t\t### BOOKING CAN BE CANCELLED ONLY ON THE SAME DAY OF BOOKING ###')
            
          
def support():  #support for any query 
    print("-"*188)
    print ("""\t\t\t    +------------------------------------------+
\t\t\t    |   SUPPORT     : CONTACT FOR ANY QUERY    |
\t\t\t    |   -------       ------- --- --- -----    |
\t\t\t    +------------------------------------------+
\t\t\t    | * MANAGER     : PIYUSH SAXENA            | 
\t\t\t    |    MOBILE     : 9643566981               |
\t\t\t    | * STRAW BOSS  : ROHAN GUPTA              |
\t\t\t    |    MOBILE     : 9811582304               |
\t\t\t    | * ACCOUNTANT  : YASH RAJ SINGH BISHT     |
\t\t\t    |    MOBILE     : 9811582304               |
\t\t\t    +------------------------------------------+""")

                            
    

def feed():  #to display customer feedback
    print("-"*188)
    print("\t\t\t +------------------------+")
    print('\t\t\t | 1. CUSTOMER FEEDBACKS  |')
    print("\t\t\t +------------------------+")
    print('\t\t\t | 2. ONLINE INTERACTIONS |')
    print("\t\t\t +------------------------+")
    print('\t\t\t | 3. LEAVE YOUR FEEDBACK |')
    print("\t\t\t +------------------------+")
    ch=int(input('\n\t\t\tENTER YOUR CHOICE : '))
    if ch==1:
        print('\t\t\t +----------------------------------------------------------------------------------+')
        print('\t\t\t | -> RAKSHIT11    -- I LOVE THIS SITE,EXCELLENT CUSTOMER SUPPORT                   |')
        print('\t\t\t | -> SARTHAKJN34  -- MY BOOKED TICKETS ARE NOT SHOWING UP                          |')
        print('\t\t\t | -> AYUSH_G      -- MY DEDUCTED BALNCING IS TWICE THAN EXPECTED                   |')
        print('\t\t\t | -> TUSHAR_M     -- THIS SITE IS THE BEST                                         |')
        print('\t\t\t +----------------------------------------------------------------------------------+')
        ch=input('\n\t\t\t\t\t   WANT TO LOAD MORE COMMENTS ( Y/N) ........ : ')
        if ch=='Y'or ch=='y':
            print('\t\t\t +----------------------------------------------------------------------------------+')
            print('\t\t\t | -> NISHCHAY_J -- MY ACCOUNT IS BANNED FOR NO REASON. PLEASE LOOK INTO IT         |')
            print('\t\t\t | -> RAJAT_VALECHA-- WANT TO BOOK MORE FILMS. EXCELLENT SITE <3                    |')
            print('\t\t\t +----------------------------------------------------------------------------------+')
            print('\n\t\t\t--THE END-- :-)')
        elif ch=='n' or ch=='N':
            print('\t\t\t +----------------------------------------------------------------------------------+')
            print('\n\t\t\t--THE END-- :-)')
    elif ch==2:
        print("\t    +-----------------------------------+")
        print("\t    |       ONLINE  SUPPORT             |")
        print("\t    |       ------ --------             |")
        print("\t    +-----------------------------------+")
        print("\t    | 1. YOUTUBE SUPPORT LINK           |")
        print("\t    | 2. DISCORD SUPPRT LINK            |")
        print("\t    | 3. TWITTER LINK                   |")
        print("\t    | 4. FACEBOOK LINK                  |")
        print("\t    | 5. EXIT                           |")
        print("\t    +-----------------------------------+")
        while True:
            ch=int(input('\n\t\t\tENTER YOUR CHOICE :'))
            if ch==1:
                print('\n\t\t\t      +------------------------------------------------+')
                print('\t\t\t     |     https://www.YOUTUBE.com/uzumy/ht/gKJn.in   |')
                print('\t\t\t      +------------------------------------------------+')
                break
            if ch==2:
                print('\n\t\t\t      +------------------------------------------------+')
                print('\t\t\t     |     https://www.DISCORD.com/jujd/s/ggh.in      |')
                print('\t\t\t      +------------------------------------------------+')
                break
            if ch==3:
                print('\n\t\t\t      +------------------------------------------------+')
                print('\t\t\t     |     https://www.TWITTER.com/sddsa/fs/asa.in    |')
                print('\t\t\t      +------------------------------------------------+')
                break
            if ch==4:
                print('\n\t\t\t      +------------------------------------------------+')
                print('\t\t\t     |     https://www.FACEBOOK.com/dfs/gdsgd.com     |')
                print('\t\t\t      +------------------------------------------------+')
            elif ch==5:
                break
    elif ch==3:
        fd=input('\t\t\tWRITE YOUR FEEDBACK HERE ALONG WITH YOUR UNIQUE USERNAME -=>')
        print("Thank you for your feedback!! Looking forward to serve you!!")

def title1():  #title text art 2
    print("-"*188)
    tm=time.localtime()
    date=str(tm[2])+'/'+str(tm[1])+'/'+str(tm[0])
    day, month, year = (int(x) for x in date.split('/'))    
    ans = datetime.date(year, month, day)
    day=ans.strftime("%A").upper()
    hour=tm[3]
    mint=tm[4]
    ap=' '
    if hour>=12 and hour<=23:
        hour=hour-12
        ap='PM'
    else:
        ap='AM'
    print('\t',day,'\n\n\t',tm[2],'/',tm[1],'/',tm[0],'\t\t\t\t\t\t\t\t\t',hour,':',mint,ap,'\n\n\n')
    print('\t           )       )        )                     )        (         )      )              ')
    print('\t   (    ( /(    ( /(     ( /(        (         ( /(        )\ )   ( /(   ( /(    (  (      ')
    print("\t ( )\   )\())   )\())    )\())       )\))(     )\())      (()/(   )\())  )\())   )\))(    ")
    print('\t  )((_) ((_)\   ((_)\   ((_)\       ((_)()\   ((_)\        /(_)) ((_)\  ((_)\   ((_)()\ )  ')
    print('\t ((_)_  ((_)    ((_)   ((_)        (_()((_)  __ ((_)      (_))    _((_)   ((_)  _(())\_)() ')
    print('\t | _ )  / _ \   / _ \  | |/ /       |  \/  | \ \ / /      / __|  | || |  / _ \  \ \((_)/ / ')
    print("\t | _ \ | (_) | | (_) | | ' <        | |\/| |  \ V /       \__ \  | __ | | (_) |  \ \/\/ /  ")
    print('\t |___/  \___/   \___/  |_|\_\       |_|  |_|   |_|        |___/  |_||_|  \___/    \_/\_/   \n\n')

def title2(): #title text art 2
    print('\t\t                              /^\^\^^/^/^\ ')
    print('\t\t                            /^\  \ \/ /  /^\ ')
    print('\t\t                            \+/ \ \\// /  \+/ ') 
    print('\t\t                                  \\//')
    print('\t\t                                 /----\ ')
    print('\t\t                                | #### | ')
    print('\t\t                                 \----/                                 ')
    print('\t\t [ " " " " ]             /^^\---/%    %\---/^^\             [ " " " " ] ')
    print('\t\t  |       |              \  /    %    %    \  /              |       | ')
    print('\t\t  |   o   |   +=================]  %%  [=================+   |   o   | ')
    print('\t\t  |       |___|  *                                     * |___|       | ')
    print('\t\t  |   o   |        |                                  |      |   o   | ')
    print('\t\t  |       |       -|-------     WELCOME TO     -------|-     |       | ')
    print('\t\t /    o    \                    ------- --                  /    o    \ ')
    print('\t\t |         |              -=>  BOOK MY SHOW  <=-            |         | ')
    print('\t\t |   /\    |__                 ---- -- ----               __|   /\    | ')
    print('\t\t |  ||||   |  |  *                                    *  |  |  ||||   | ')
    print('\t\t |  ||||   |  +==========================================+  |  ||||   | ')
    print('\t\t/\/\/\/\/\/\                                               /\/\/\/\/\/\ ')

def ex():  #exit text art
    print("\t\t\t	                 ____________")
    print("\t\t\t                      // ^^^^{}^^^^ \\\ ")
    print("\t\t\t                     //..@--------@..\\\ ")
    print("\t\t\t                    //&%&%&%&/\&%&%&%&\\\ ")
    print("\t\t\t                   ||&%&%&_.'  '._&%&%&|| ")
    print("\t\t\t            	   ||&%'''    	'''%&  || ")
    print('\t\t\t                   ||&%& THANKS FOR &%&|| ')
    print('\t\t\t                   ||&%&  VISITING! &%&|| ')
    print('\t\t\t                   ||&%&  SEE YOU   &%&|| ')
    print('\t\t\t                   ||&%&   AGAIN :-)&%&|| ')
    print('\t\t\t             ______||&%&&==========&&%&||______')
    print('\t\t\t             ======######################=======')
    print("-"*188)
    
def bytckt():  #now showing text art
    print('\t\t\t             @-   ___________________-@')
    print('\t\t\t      	  @-______|   NOW SHOWING   |_____-@')
    print('\t\t\t           |   SPIDERMAN:NO WAY HOME     | ')
    print('\t\t\t    _______|_____________________________|__________')
    print('\t\t\t   |        ----=> BUY TICKETS HERE------           | ')
    print('\t\t\t   |________________________________________________| ')
    print('\t\t\t   |               -               -                | ')
    print('\t\t\t   |   -           -         	    -           -   | ')
    print('\t\t\t   |    	 _____________________              | ')
    print('\t\t\t   |  - -   |	 |   |  TICKETS  |   |	  |   - -   | ')
    print('\t\t\t   |        |    |   |     |     |   |	  |         | ')
    print('\t\t\t   |  - -   |____| - |o____o____o| - |____|   - -   | ')
    print('\t\t\t   |   -    |	 |   |     --    |   |    |    -    | ')
    print('\t\t\t   |   -    |	 | - | -PAY HERE-| - |	  |    -    | ')
    print('\t\t\t   |_______ |====|___|___________|___|====|_________| ')
    print('\t\t\t   /                   	                            \ ')
    print('\t\t\t  /__________________________________________________\ \n\n')


def bnkp(): #netbanking text art
    print('\t\t\t     	 _._._                        _._._')
    print('\t\t\t    	_|   |_                      _|   |_')
    print('\t\t\t        | ... |_._._._._._._._._._._| ... |')
    print('\t\t\t    	| ||| |  o  NET BANKING  o  | ||| |')
    print('\t\t\t    	| """ |  """    """    """  | """ |')
    print('\t\t\t   ())  |[-|-]|[-|-]   [-|-]   [-|-]|[-|-]|  ()) ')
    print("\t\t\t  (())) |     |---------------------|     | (())) ")
    print('\t\t\t (())())| """ |  """	"""	""" | """ |(())()) ')
    print('\t\t\t (()))()|[-|-]|  :::   .-"-.   :::  |[-|-]|(()))() ')
    print('\t\t\t ()))(()|     | |~|~|  |_|_|  |~|~| |     |()))(() ')
    print('\t\t\t	|||_____|_|_|_|_|_|_|_|_|_|_|___|||')
    print('\t\t\t  ~ ~^^ @@@@@@@@@@@@@@/=======\@@@@@@@@@@@@ ^^~ ~')
    print('\t\t\t  ^~^~                            	     ~^~^')
title1()
title2()
menu1()
