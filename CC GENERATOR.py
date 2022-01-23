import random
import os
import colorama
import time as t
from colorama import  Fore,Style
G = Fore.GREEN
B = Fore.WHITE
G = Fore.GREEN
C = Fore.CYAN
G = Fore.GREEN
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")
os.system("clear")
print(Fore.RED+"""CC GENERATOR BY Lêkzï""")
t.sleep(5)
os.system("apt install figlet")
os.system("clear")
def loop():
    os.system("clear")
    #colors
    red = "\033[1;31;40m"
    yellow = "\033[1;33;40m"
    global green
    green = "\033[1;32;40m"
    global white
    white = "\033[0;37;40m"
    #BG colors
    global redd
    redd = "\033[0;33;41m"
    print(yellow)
    os.system("figlet CC GENERATOR")
    print(white)
    print(green+"""            
           ==========================
             	  CC GENERATOR 
           ==========================
""")
    print(green + "=====================================================" + white)
    print(yellow + """
    	[+]Tool name:CC GENERATOR
	[+]Creator:Lêkzï
	[+]Team:Greyhax0rs™
	[+]Contact me on whatsapp:+2347064822519
    """ + white)
    print(green + "=====================================================" + white)
    print(yellow + "Choose a card to generate below:" + white)
    print(green + """
    1.VisaCard
    2.MasterCard
    """ + white)
    print(yellow + "=====================================================" + white)
    print(green + "[0]Update Me" + white)
    print(yellow + "=====================================================" + white)
    cc = input(yellow + "Your input: " + white)
    if cc == "1":
        print(yellow +"processing..." + white)
        t.sleep(5)
        #Credit Card Random Bin for Visa
        rand1 = 4
        rand2 = random.randrange(1, 8) 
        rand3 = random.randrange(2, 8) 
        rand4 = random.randrange(3, 8)
        rand5 = random.randrange(0, 8)
        rand6 = random.randrange (1, 8)
       #Random Credit Card Account Number
        acc1 = random.randrange(1, 4)
        acc2 = random.randrange(5, 7)
        acc3 = random.randrange(0, 6)
        acc4 = random.randrange(2, 5)
        acc5 = random.randrange(7, 8)
        acc6 = random.randrange(6, 8)
        acc7 = random.randrange(1, 5)
        acc8 = random.randrange(3, 7)
        acc9 = random.randrange(4, 6)
       #Doubling Even position
        aa = ((rand1 * 2)%9) 
        bb = ((rand3 * 2)%9)
        cc = ((rand5 *2)%9)
        a = ((acc1 * 2 )% 9) 
        b = ((acc3 * 2 )% 9) 
        c = ((acc5 * 2) % 9) 
        d = ((acc7 * 2) % 9) 
        e = ((acc9 * 2)% 9)
       #Sum digits
        Rand1 = aa
        Rand2 = rand2
        Rand3 = bb
        Rand4 = rand4
        Rand5 = cc
        Rand6 = rand6
        Acc1 = a
        A = acc2
        Acc3 = b
        B = acc4
        Acc5 = c
        C = acc6
        Acc7 = d
        D = acc8
        Acc9 = e
        #add sum digit to get check number
        acc = Rand1 + Rand2 + Rand3 + Rand4 + Rand5 + Rand6 + Acc1 + A + Acc3 + B +Acc5 + C + Acc7 + D + Acc9
        checkSum = ((acc * 9)% 10)
        #Converting all Data to string
        ran1 = str(rand1)
        ran2 = str(rand2)
        ran3 = str(rand3) 
        ran4 = str(rand4) 
        ran5 = str(rand5) 
        ran6 = str(rand6)
        za = str(acc1)
        za1 = str(acc2)
        za2 = str(acc3)
        za3 = str(acc4)
        za4 = str(acc5)
        za5 = str(acc6)
        za6 = str(acc7)
        za7 = str(acc8)
        za8 = str(acc9)
        check = str(checkSum)
        #Joining all cc number together
        ccnumber = ran1 + ran2 + ran3 + ran4 + ran5 + ran6 + za + za1 + za2 + za3 + za4 + za5 + za6 + za7 + za8 + check
        cvv = random.randrange(354, 958)
        mm = random.randrange(1, 12)
        yy = random.randrange(22, 25)
        print(yellow + """
====================CC Details below=================
        Card number: """, ccnumber, """
        CVV: """, cvv, """
        Expiry Date: MM:""", mm, """ YY:""",yy,  white)
    elif cc == "2":
        #Credit Card Random Bin for MasterCard
        rand1 = 4
        rand2 = random.randrange(1, 8) 
        rand3 = random.randrange(2, 8) 
        rand4 = random.randrange(3, 8)
        rand5 = random.randrange(0, 8)
        rand6 = random.randrange (1, 8)
       #Random Credit Card Account Number
        acc1 = random.randrange(1, 4)
        acc2 = random.randrange(5, 7)
        acc3 = random.randrange(0, 6)
        acc4 = random.randrange(2, 5)
        acc5 = random.randrange(7, 8)
        acc6 = random.randrange(6, 8)
        acc7 = random.randrange(1, 5)
        acc8 = random.randrange(3, 7)
        acc9 = random.randrange(4, 6)
       #Doubling Even position
        aa = ((rand1 * 2)%9) 
        bb = ((rand3 * 2)%9)
        cc = ((rand5 *2)%9)
        a = ((acc1 * 2 )% 9) 
        b = ((acc3 * 2 )% 9) 
        c = ((acc5 * 2) % 9) 
        d = ((acc7 * 2) % 9) 
        e = ((acc9 * 2)% 9)
       #Sum digits
        Rand1 = aa
        Rand2 = rand2
        Rand3 = bb
        Rand4 = rand4
        Rand5 = cc
        Rand6 = rand6
        Acc1 = a
        A = acc2
        Acc3 = b
        B = acc4
        Acc5 = c
        C = acc6
        Acc7 = d
        D = acc8
        Acc9 = e
        #add sum digit to get check number
        acc = Rand1 + Rand2 + Rand3 + Rand4 + Rand5 + Rand6 + Acc1 + A + Acc3 + B +Acc5 + C + Acc7 + D + Acc9
        checkSum = ((acc * 9)% 10)
        #Converting all Data to string
        ran1 = str(rand1)
        ran2 = str(rand2)
        ran3 = str(rand3) 
        ran4 = str(rand4) 
        ran5 = str(rand5) 
        ran6 = str(rand6)
        za = str(acc1)
        za1 = str(acc2)
        za2 = str(acc3)
        za3 = str(acc4)
        za4 = str(acc5)
        za5 = str(acc6)
        za6 = str(acc7)
        za7 = str(acc8)
        za8 = str(acc9)
        check = str(checkSum)
        #Joining all cc number together
        ccnumber = ran1 + ran2 + ran3 + ran4 + ran5 + ran6 + za + za1 + za2 + za3 + za4 + za5 + za6 + za7 + za8 + check
        cvv = random.randrange(354, 958)
        mm = random.randrange(1, 12)
        yy = random.randrange(22, 25)
        print(yellow + """
================CC Details below=====================
        Card number: """, ccnumber, """
        CVV: """, cvv, """
        Expiry Date: MM:""", mm, """ YY:""",yy,  white)
        t.sleep(3)
        loop()
    elif cc == "0":
        os.system("clear")
        print(red + "Updating CC GENERATOR..." + white)
        t.sleep(5)
        os.system("""
        cd
        rm -f -r CC GENERATOR
        git clone https://github.com/Lekzi/CC GENERATOR
        clear""")
        print(red + """
        Now type this
        cd $HOME
        cd CC GENERATOR
        python3 GENERATOR.py
        """ + white)
        exit()
        
    
        loop()
        
       
loop()
cont = input (green + "Do you want to generate more?[y/n]? " + white)
if cont == "y" or cont == "Y":
    loop()
else:
    exit()
