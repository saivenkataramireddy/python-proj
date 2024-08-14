#this project is about hotel management system 
import random
import datetime
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
#creating home fonction
i=0

def home():
    print(" Welcome To Hotel s.v.r.r grand\n")
    print("1 Booking\n")
    print("2 Rooms Information\n")
    print("3 Restaurent/Room service \n")
    print("4 Payment\n")
    print("5 Record\n")
    print("0 Exit\n")
    ch=int(input("Choice your option:->"))
     
    if ch == 1:
        print(" ")
        booking()
     
    elif ch == 2:
        print(" ")
        Rooms_info()
     
    elif ch == 3:
        print(" ")
        restaurant()
     
    elif ch == 4:
        print(" ")
        Payment()
     
    elif ch == 5:
        print(" ")
        Record()
     
    else:
        exit() 
# Function used in booking  
def date(c):     
    if c[2] >= 2024 and c[2] <= 2025:         
        if c[1] != 0 and c[1] <= 12:             
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:                 
                if c[2]%4 == 0 and c[0] <= 29:
                    pass                 
                elif c[0]<29:
                    pass                 
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    booking()            
            # if month is odd & less than equal 
            # to 7th  month 
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass             
            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass             
            # if month is even & greater than equal 
            # to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass             
            # if month is odd & greater than equal
            # to 8th  month
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:  
                pass             
            else: 
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                booking()                 
        else:
            print("Invalid date\n")
            name.pop(i)
            phno.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            booking()             
    else:
        print("Invalid date\n")
        name.pop(i)
        phno.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        booking()
#booking function
def booking():
    global i #using i global variable
    print("------------------------\n")
    print("Booking Rooms")
    print("-------------------------\n")
    print(" ")
    while 1:
        n=str(input("Enter Name:"))
        p1=input("Enter Phone Number:")
        a= str(input("Enter Address:"))
        #checking the input field is filled or is empty
        if n!="" and p1!="" and a!="":
            name.append(n)
            add.append(a)
            break
        else:
            print("\t input fields are can't be empty:")
            print("....please fill input fields")
    cii=str(input("check_in"))
    checkin.append(cii)
    cii=cii.split('/')
    ci=cii
    ci[0]=int(ci[0])
    ci[1]=int(ci[1])
    ci[2]=int(ci[2])
    date(ci)
    coo=str(input("check_out"))
    checkout.append(coo)
    coo=coo.split('/')
    co=coo
    co[0]=int(co[0])
    co[1]=int(co[1])
    co[2]=int(co[2])
    #here checking the check out date must be after check out date or not
    if co[1]<ci[1] and co[2]<ci[2]:
        print("\n Check out date must fall after check in date")
        name.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        booking()
    elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
        print("\n Check out date must fall after check in date")
        name.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        booking()
    else:
        pass
    date(co)
    d1=datetime.datetime(ci[2],ci[1],ci[0])
    d2=datetime.datetime(co[2],co[1],co[0])
    d=(d2-d1).days
    day.append(d)
    print("=====SELECT ROOM TYPE====")
    print("1. Standard Ac")
    print("2. Standard Non-Ac")
    print("3. 3-Bed Non-Ac")
    print("4. 3-Bed Ac")
    ch=int(input("Enter Your Choice:-->"))
    if ch== 1:
        room.append("Standard Ac")
        print("Room Type Standard Ac ")
        price.append(3000)
    elif ch== 2:
        room.append("Standard Non-Ac")
        print("Room type standart Non-Ac")
        price.append(4000)
    elif ch== 3:
        room.append("3-Bed Non-Ac")
        print("Room type 3-Bed Non-Ac")
        price.append(4500)
    elif ch== 4:
        room.append("3-Bed Ac")
        print("Room type 3-Bed Ac")
        price.append(5000)
    else:
        print("wrong choice")
    # randomly generating room no. and customer 
    # id for customer
    rn = random.randrange(40)+300
    cid = random.randrange(40)+10
    # checks if allotted room no. & customer 
    # id already not allotted
    while rn in roomno or cid in custid:
        rn = random.randrange(60)+300
        cid = random.randrange(60)+10
    rc.append(0)
    p.append(0)
    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0,i):
            if p1==phno[n]:
                if p[n]==1:
                    phno.append(p1)
    elif p1 in phno:
        for n in range(0,i):
            if p1==phno[n]:
                if p[n]==0:
                    print("\t phone no . already exists and payment yet not done...!:(")
                    name.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    booking()
    print("")
    print("\t\t***Room Booked Successfully***: )")
    print("Room No.-",rn)
    print("Customer Id- ",cid)
    roomno.append(rn)
    custid.append(cid)
    i=i+1
    n=int(input("Press 0 to-Back-->"))
    if n==0:
        home()
    else:
        exit()
# Rooms Information
def Rooms_info():
    print("----Hotel Rooms Information----")
    print("")
    print("STANDARD AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        home()
    else:
        exit()
def restaurant():
    ph=int(input("Customer Id:"))
    global i
    f=0
    r=0
    for n in range(0,i):
        if custid[n]==ph and p[n]==0:
            f=1
            print("-------------------------------------------------------------------------")
            print("                           Hotel s.v.r.r grand    ")
            print("-------------------------------------------------------------------------")
            print("                            Menu Card")
            print("-------------------------------------------------------------------------")
            print("\n BEVARAGES                              26 Dal Fry................ 140.00")
            print("----------------------------------      27 Dal Makhani............ 150.00")
            print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")
            print(" 2  Masala Tea.............. 25.00")
            print(" 3  Coffee.................. 25.00      ROTI")
            print(" 4  Cold Drink.............. 25.00     ----------------------------------")
            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")
            print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")
            print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")
            print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")
            print(" 9  Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00      RICE") 
            print("                                       ----------------------------------")
            print(" SOUPS                                  33 Plain Rice.............. 90.00")
            print("----------------------------------      34 Jeera Rice.............. 90.00")
            print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")
            print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")
            print(" 13 Veg. Noodle Soup....... 110.00")
            print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")
            print(" 15 Veg. Munchow........... 110.00     ----------------------------------")
            print("                                        37 Plain Dosa............. 100.00")
            print(" MAIN COURSE                            38 Onion Dosa............. 110.00")
            print("----------------------------------      39 Masala Dosa............ 130.00")
            print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")
            print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")
            print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00")
            print(" 19 Palak Paneer........... 120.00")
            print(" 20 Chilli Paneer.......... 140.00      ICE CREAM")
            print(" 21 Matar Mushroom......... 140.00     ----------------------------------")
            print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")
            print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")
            print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00")
            print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
            print("Press 0 -to end ")
            ch=1
            while(ch!=0):
                 
                ch=int(input(" -> "))
                #here i am using if-elif conditions to assign item prices listed in menu card
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r=r+rs
                elif ch<=4 and ch>=2:
                    rs=25
                    r=r+rs
                elif ch<=6 and ch>=5:
                    rs=30
                    r=r+rs
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs
                elif ch<=10 and ch>=9:
                    rs=70
                    r=r+rs
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                    rs=110
                    r=r+rs
                elif ch<=19 and ch>=18:
                    rs=120
                    r=r+rs
                elif (ch<=26 and ch>=20) or ch==42:
                    rs=140
                    r=r+rs
                elif ch<=28 and ch>=27:
                    rs=150
                    r=r+rs
                elif ch<=30 and ch>=29:
                    rs=15
                    r=r+rs
                elif ch==33 or ch==34:
                    rs=90
                    r=r+rs
                elif ch==37:
                    rs=100
                    r=r+rs
                elif ch<=41 and ch>=39:
                    rs=130
                    r=r+rs
                elif ch<=46 and ch>=43:
                    rs=60
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ",r)
            #up to here i am updating prices according to menu card
            #now iam appending in rc list
            r=r+rc.pop(n)
            rc.append(r)
        else:
            pass
    if f==0:
        print("Invalid Customer Id:")
    n=int(input("Enter 0 to Back\n-->"))
    if n==0:
        home()
    else:
        exit()
def Payment():
     
    ph=str(input("Phone Number: "))
    global i
    f=0
     
    for n in range(0,i):
        if ph==phno[n] :
             
            # checks if payment is
            # not already done
             if p[n]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                  
                print("  1- Credit/Debit Card")
                print("  2- Paytm/PhonePe")
                print("  3- Using UPI")
                print("  4- Cash")
                x=int(input("-> "))
                print("\n  Amount: ",(price[n]*day[n])+rc[n])
                print("\n            Pay For S.v.r.r Grands")
                print("  (y/n)")
                ch=str(input("->"))
                 
                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("           Hotel AnCasa")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                    print(" Restaurant Charges: \t",rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)
                     
                    # pops room no. and customer id from list and 
                    # later assigns zero at same position
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n,0)
                    custid.insert(n,0)
                     
             else:
                 
                for j in range(n+1,i):
                    if ph==phno[j] :
                        if p[j]==0:
                            pass
                         
                        else:
                            f=1
                            print("\n\tPayment has been Made :)\n\n") 
    if f==0:    
        print("Invalid Customer Id")
         
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()
 
# RECORD FUNCTION 
def Record():
     
    # checks if any record exists or not
    if phno!=[]:
        print("        *** HOTEL RECORD ***\n")
        print("| Name        | Phone No.    | Address       | Check-In  | Check-Out     | Room Type     | Price      |")
        print("----------------------------------------------------------------------------------------------------------------------")
         
        for n in range(0,i):
            print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
         
        print("----------------------------------------------------------------------------------------------------------------------")
     
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
         
    else:
        exit()
        
            
            
home()
