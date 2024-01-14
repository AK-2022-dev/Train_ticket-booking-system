                                                           #RAILWAY RESERVATION SOFTWATRE#

#PATTERN PRINT....#

#PRINTING R#
for row in range(7):
    for col in range(5):
        if row==0 and (col in{0,1,2,3,4}):
            print("*",end="")
        elif(row in {0,1,2,4,5,6})and (col in {0}):              #printing R.B.S(railway booking software logo)#
            print("*",end="")
        elif(row in {0,1,2,3}) and (col in {4}):
            print("*",end="")
        elif row==3:
            print("*",end="")
        elif row==4 and col ==1:
            print("*",end="")
        elif row==5 and col==2:
            print("*",end="")
        elif row==6 and col==3:
            print("*",end="")
            
        else:
            print(" ",end="")
    print()

print(".............")
print()
#PRINTING B #
for row in range(7):
    for col in range(5):
        if row==0 and (col in{0,1,2,3,4}):
            print("*",end="")
        elif row==6 and(col in{0,1,2,3,4}):
            print("*",end="")
        elif(row in {0,1,2,4,5,6})and (col in {0,4}):
            print("*",end="")
        elif(row in {0,1,2,3}) and (col in {4}):
            print("*",end="")
        elif row==3 and (col in {0,1,2,3}):
            print("*",end="")
        else:
            print(" ",end="")
    print()

print(".............")
print()
#PRINTING S#
for row in range(7):
    for col in range(5):
        if row==0 and (col in{0,1,2,3,4}):
            print("*",end="")
        elif row==1 and col==0:
            print("*",end="")
        elif row==2 and col==0:
            print("*",end="")
        elif row==3 and (col in{0,1,2,3,4}):
            print("*",end="")
        elif row==4 and col==4:
            print("*",end="")
        elif row==5 and col==4:
            print("*",end="")
        elif row==6 and (col in {0,1,2,3,4}):
            print("*",end="")
        else:
            print(" ",end="")
    print()

print(".............")
print()


import os
import csv
print("This  software is a Railway Reservation System Program:  \nThe given menu will guide you through the various options available for various task that can performed using the software")
print("********************************************************************************************************************")
def addrecord():
    print("Book Ticket for the Passenger....:")
    print("======================================")
    f=open('passengers.csv','a',newline='\r\n')
    s=csv.writer(f)
    ticketno=int(input("Enter Passenger's Ticket Number = "))
    name=input("Enter Passenger's Name = ")
    depar=input("Enter Passenger's Departure Point = ")
    dest=input("Enter Passenger's Destination Point = ")
    mode=input("Enter passenger's payment mode = \n 1:ONLINE \n 2:CASH\n")
    rec=[ticketno,name,depar,dest,mode]
    s.writerow(rec)
    f.close()
    print("TICKET BOOKED SUCCESSFULLY..!!!!" )
    print()
    choice1=input("Do you want to book more tickets of the passenger...\n 1.YES \n 2.NO\n")
    print()
    for b in range(1):
        if choice1=="YES" or "yes":
            addrecord()
        else:
            break
        break   
    print()
    input("Press any key to continue..")


def modifyrecord():
    print("Modify a Record of Passenger:")
    print("===============================")
    f=open('passengers.csv','r',newline='\r\n')
    f1=open("temp.csv","w",newline="\r\n")
    f1=open("temp.csv","a",newline="\r\n")
    r=input('Enter the ticket-no of the passenger you want to modify: ')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("The Details of the  following passenger are : ")
            print()
            print("Ticket-no of the passenger = ",rec[0])
            print("Name of the passenger = ",rec[1])
            print("Departure point of the passenger =",rec[2])
            print("Destination point of the passenger = ",rec[3])
            print("Mode of payment of the passenger = ",rec[4])
            choice=input("Do you want to modify the following passenger's record\n1.Yes \n2.No\n")
            if choice=='yes' or choice=='YES':
                ticketno=int(input("Enter Passenger's Ticket Number = "))
                name=input("Enter Passenger's Name = ")
                depar=input("Enter Passenger's Departure Point = ")
                dest=input("Enter Passenger's Destination Point = ")
                pay=input("Enter passenger's payment mode = \n 1:ONLINE \n 2:CASH")
                rec=[ticketno,name,depar,dest,pay]
                s1.writerow(rec)
                print("Record of the Passenger Modified")
                break
           
        
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
            
    f.close()
    f1.close()
    os.remove("passengers.csv")
    os.rename("temp.csv","passengers.csv")
  
    input("Press any key to continue.....................")


def deleterecord():
    f=open('passengers.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter the ticket number of the passenger you want to delete :')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("Ticket-no = ",rec[0])
            print("Name = ",rec[1])
            print("Departure point = ",rec[2])
            print("Destination point = ",rec[3])
            print("Mode of payment = ",rec[4])
            choice=input("Do you want to delete this record(yes/no)")
            if choice=='yes' or choice=='YES':
                pass
                print("Record of the passenger is Deleted succesfully !!!!")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("passengers.csv")
    os.rename("temp.csv","passengers.csv")
    
    input("Press any key to continue....")


def search():
    print("Searching a passengers Record")
    print("===================")
    f=open('passengers.csv','r',newline='\r\n')  
    r=input('Enter the ticket number of the passenger you want to search for !!!')
    s=csv.reader(f)
    for rec in s:
        if rec[0]==r:
            print("Ticket-no = ",rec[0])
            print("Name = ",rec[1])
            print("Departure point = ",rec[2])
            print("Destination point = ",rec[3])
            print("Mode of payment = ",rec[4])
    f.close()
    print()
    input("Press any key to continue.....")

    
def viewall():
    print("List of all passengers that have booked ticket !!!!")
    print("====================================================")
    f=open('passengers.csv','r',newline='\r\n')  
    s=csv.reader(f)
    i=1
    for rec in s:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2],end="\t\t")
        print(rec[3],end="\t\t")
        print(rec[4],end="\t\t")
        i+=1
    f.close()
    print()
    input("Press any key to continue.........")



def foodfac():
    print("List of all the food combos available for the journey..........")
    print("==================================================================")
    f2=open("food.csv","r",newline="\r\n")
    s2=csv.reader(f2)
    a=1
    for recs in s2:
        print(recs[0],end="\t")
        print(recs[1],end="\t")
        print(recs[2],end="\t")
        print(recs[3],end="\t")
        print(recs[4],end="\t")
        a+=1
        print()
    print()
    choices=input("Enter the name of item...\n")
    print()
    for i in range(1):
        if choices=="100"or"200"or"300"or"400"or"500":
            print()
            print("ITEM ADDED ...")
            break
        else:
            break


def inventory():
    print("List of all the utilities items availablefor the journey........")
    print("==================================================================")
    f2=open("inventory.csv","r",newline="\r\n")
    s2=csv.reader(f2)
    a=1
    for recs in s2:
        print(recs[0],end="\t")
        print(recs[1],end="\t")
        print(recs[2],end="\t")
        print()
    print()
    choices=input("Enter the item name...\n")
    print()
    for i in range(1):
        if choices=="blanket"or"towel"or"pillow"or"soaps":
            print("Item Added....")
            break
        else:
            break
    
def fetch():
    print("TRAIN DETAILS ARE:-----------")
    op=open("details.txt","r",newline="\r\n")
    red=op.read()
    print("The Stats of the Train are  >>>>>>>>>>>>>>")
    print()
    print(red)



def totalprice():
    print("PRINTING THE TOTAL COST OF THE JOURNEY")
    ticket=int(input("Enter the Ticket Price---->\n"))
    inventory=int(input("Enter the price of Inventory item booked--->\n"))
    food=int(input("Enter the price of Food item booked------>\n"))
    total=ticket+inventory+food
    print("TOTAL PRICE OF THE JOURNEY----->\n",total)



def mainmenu():
    choice=0
    while choice!=10:
        print("\n")
        print("WELCOME TO THE MAIN MENU OF THE SOFTWARE !!!!!!")
        print()
        print("====================================================")
        print()
        print("1. BOOK NEW TICKET  OF THE PASSENGER ....")
        print()
        print("2. MODIFY ANY DETAILS IN THE TICKET OF THE PASSENGER.....") 
        print()
        print("3. DELETE ANY EXSISTING RECORD OF TICKET OF THE PASSENGER...")
        print()
        print("4. SEARCH FOR A PARTICULAR TICKET IN THE LIST....")
        print()
        print("5. PRINT LIST OF ALL THE CONFIRM PASSENGERS.....")
        print()
        print("6. DETAILS OF THE FOOD FACILITIES....")
        print()
        print("7. DETAILS OF THE INVENTORY ITEMS.....")
        print()
        print("8. FETCH ANY TRAIN DETAILS......")
        print()
        print("9. CALCULATE TOTAL PRICE OF THE JOURNEY.....")
        print()
        print("10. EXIT SOFTWARE.......")
        print()
        print("=====================================================")
        print()
        
        choice=int(input('Enter your choice from the given list:- \n'))
        if choice==1:
            addrecord()
        elif choice==2:
            modifyrecord()
        elif choice==3:
            deleterecord()
        elif choice==4:
            search()
        elif choice==5:
            viewall()
        elif choice==6:
            foodfac()
        elif choice==7:
            inventory()
        elif choice==8:
            fetch()
        elif choice==9:
            totalprice()
        elif choice==10:
            print()
            print("Software Terminated!...!!!")
            break

mainmenu()
