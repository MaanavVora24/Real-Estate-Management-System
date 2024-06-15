import mysql.connector as mys
mc = mys.connect(host='localhost',user='root',passwd='12345')
cur=mc.cursor()
from prettytable import PrettyTable

def CreateLandRecord():
  cur.execute("use real_estate_management")
  cur.execute("create table land_record(Plot_Number int primary key,Address varchar(60),Residential_Area varchar(60),Area_sqft_ float,Sale_Price float,Rent_or_Lease_Price float,Status varchar(20) default 'Available')")      
  mc.commit()
def CreateSaleRecord():
  cur.execute("use real_estate_management")
  cur.execute("create table sale_record(Dealing_Number int primary key,Customer_Name varchar(60),Customer_Contact_Number bigint,Date_Of_Agreement date,Plot_Number int,Sale_Price float)")
  mc.commit()
def CreateRentRecord():
  cur.execute("use real_estate_management")
  cur.execute("create table rent_record(Dealing_Number int primary key,Customer_Name varchar(60),Customer_Contact_Number bigint,Date_Of_Agreement date,Date_Of_Termination date,Plot_Number int,Rent_Price float)")
  mc.commit()
def CreateLeaseRecord():
  cur.execute("use real_estate_management")
  cur.execute("create table lease_record(Dealing_Number int primary key,Customer_Name varchar(60),Customer_Contact_Number bigint,Date_Of_Agreement date,Plot_Number int,Number_Of_Months_Of_Agreement int,Lease_Total float)")
  mc.commit()

def insertland():
 ch='YES'
 while(ch.upper()=='YES'):
  cur.execute("select * from land_record")
  record=cur.fetchall()
  if record==[]:
    e=100
  else:
    e=record[-1][0]+1
  print("The Plot Number is",e)
  d=input("Enter the Address")
  x=input("Enter the Residential Area")
  dp=float(input("Enter the Area(sq.ft)"))
  s=input("Enter the Sale Price")
  if s=='':
    s="NULL"
  else:
    s=int(s)
  j=input("Enter the Rent/Lease Price")
  if j=='':
    j="NULL"
  else:
    j=int(j)
  jk="Available"
  print("The entered record is this,")
  print("%20s"%'Plot Number',"%30s"%'Address',"%20s"%'Residential Area',"%20s"%'Area(sq.ft)',"%20s"%'Sale Price',"%20s"%'Rent/Lease Price')
  print("         ==============================================================================================================================")
  print("%20s"%e,"%30s"%d,"%20s"%x,"%20s"%dp,"%20s"%s,"%20s"%j)
  sat=input("Are you satisfied with the given details?(Yes/No)")
  if sat.lower()=="yes":
      cur.execute("insert into land_record values(%s,'%s','%s',%s,%s,%s,'%s')"%(e,d,x,dp,s,j,jk))
  ch=input("Do you want to add more records?(Yes/No):")
 mc.commit()
 
def insertsale():
 ch='y'
 while(ch.upper()=='Y'):
  cur.execute("select * from sale_record")
  record=cur.fetchall()
  if record==[]:
    e=100000
  else:
    e=record[-1][0]+1
  print("The Dealing Number is",e)
  d=input("Enter the Customer Name")
  dp=int(input("Enter Customer Contact Number"))
  s=input("Enter the Date Of Agreement(yyyy-mm-dd)")
  j=int(input("Enter Plot Number"))
  cur.execute("select * from land_record")
  record=cur.fetchall()
  for rec in record:
      if rec[0]==j:
          jk=rec[4]
  print("The Sale Price is:",jk)
  print("The entered record is this,")
  print("%20s"%'Dealing Number',"%30s"%'Customer Name',"%25s"%'Customer Contact Number',"%20s"%'Date Of Agreement',"%20s"%'Plot Number',"%20s"%'Sale Price')
  print(" ===============================================================================================================================================")
  print("%20s"%e,"%30s"%d,"%25s"%dp,"%20s"%s,"%20s"%j,"%20s"%jk)
  sat=input("Are you satisfied with the given details?(Yes/No)")
  if sat.lower()=="yes":
    cur.execute("insert into sale_record values(%s,'%s',%s,'%s',%s,%s)"%(e,d,dp,s,j,jk))
    mc.commit()
    y="Unavailable"
    c="update land_record set Status='%s' where Plot_Number=%s "
    c2=(y,j)
    cur.execute(c%c2)
    mc.commit()
  ch=input("Do you want to add more records?(y/n):")
  
def insertrent():
 ch='y'
 while(ch.upper()=='Y'):
  cur.execute("select * from rent_record")
  record=cur.fetchall()
  if record==[]:
    e=200000
  else:
    e=record[-1][0]+1
  print("The Dealing Number is",e)
  d=input("Enter the Customer Name")
  dp=int(input("Enter Customer Contact Number"))
  s=input("Enter the Date Of Agreement(yyyy-mm-dd)")
  z="0000-00-00"
  j=int(input("Enter Plot Number"))
  cur.execute("select * from land_record")
  record=cur.fetchall()
  for rec in record:
      if rec[0]==j:
          jk=rec[5]
  print("The Rent Price is:",jk)
  print("The entered record is this,")
  print("%20s"%'Dealing Number',"%30s"%'Customer Name',"%25s"%'Customer Contact Number',"%20s"%'Date Of Agreement',"%20s"%'Plot Number',"%20s"%'Rent Price')
  print(" ===============================================================================================================================================")
  print("%20s"%e,"%30s"%d,"%25s"%dp,"%20s"%s,"%20s"%j,"%20s"%jk)
  sat=input("Are you satisfied with the given details?(Yes/No)")
  if sat.lower()=="yes":
    cur.execute("insert into rent_record values(%s,'%s',%s,'%s','%s',%s,%s)"%(e,d,dp,s,z,j,jk))
    mc.commit()
    y="Unavailable"
    c="update land_record set Status='%s' where Plot_Number=%s "
    c2=(y,j)
    cur.execute(c%c2)
    mc.commit()
  ch=input("Do you want to add more records?(y/n):")
  
def insertlease():
 ch='y'
 while(ch.upper()=='Y'):
  cur.execute("select * from lease_record")
  record=cur.fetchall()
  if record==[]:
    e=300000
  else:
    e=record[-1][0]+1
  print("The Dealing Number is",e)
  d=input("Enter the Customer Name")
  dp=int(input("Enter Customer Contact Number"))
  s=input("Enter the Date Of Agreement(yyyy-mm-dd)")
  j=int(input("Enter Plot Number"))
  cur.execute("select * from land_record")
  record=cur.fetchall()
  for rec in record:
      if rec[0]==j:
          k=rec[5]
  print("The Lease(per month)is:",k)
  x=int(input("Enter the Number of Months Of Agreement"))
  jk=k*x
  print("The Total Lease is:",jk)
  print("The entered record is this,")
  print("%20s"%'Dealing Number',"%25s"%'Customer Name',"%25s"%'Customer Contact Number',"%20s"%'Date Of Agreement',"%15s"%'Plot Number',"%30s"%'No.of Months Of Agreement',"%20s"%'Total Lease')
  print(" =================================================================================================================================================================================")
  print("%20s"%e,"%25s"%d,"%25s"%dp,"%20s"%s,"%15s"%j,"%30s"%x,"%20s"%jk)
  sat=input("Are you satisfied with the given details?(Yes/No)")
  if sat.lower()=="yes":
    cur.execute("insert into lease_record values(%s,'%s',%s,'%s',%s,%s,%s)"%(e,d,dp,s,j,x,jk))
    mc.commit()
    y="Unavailable"
    c="update land_record set Status='%s' where Plot_Number=%s "
    c2=(y,j)
    cur.execute(c%c2)
    mc.commit()
  ch=input("Do you want to add more records?(y/n):")
  
def Rent_Module():
  d=input("Enter the Residential Area to search:")
  l,j=eval(input(("Enter the price range to search(Lower limit,Upper limit):"))) 
  q="select * from land_record where Residential_Area='{}'and Status='Available' and Rent_or_Lease_Price between {} and {}".format(d,1,j)
  cur.execute(q)
  dt=cur.fetchall()
  if len(dt)!=0:
      x=PrettyTable()
      x.field_names=['Plot Number','Address','Area(sq.ft)','Rent Price']
      for r in dt:
          x.add_row([r[0],r[1],r[3],r[5]])
      print(x)
  else:
      print("Sorry no data found")

def Lease_Module():
  d=input("Enter the Residential Area to search:")
  l,j=eval(input(("Enter the price range to search(Lower limit,Upper limit):")))
  n=int(input("Enter the Number of Months of Agreement:"))
  q="select * from land_record where Residential_Area='{}'and Status='Available' and Rent_or_Lease_Price between {} and {}".format(d,1,j)
  cur.execute(q)
  dt=cur.fetchall()
  if len(dt)!=0:
      x=PrettyTable()
      x.field_names=['Plot Number','Address','Area(sq.ft)','Lease Price(per month)','Total lease']
      for r in dt:
          x1=r[5]*n
          x.add_row([r[0],r[1],r[3],r[5],x1])
      print(x)
  else:
      print("Sorry no data found")

def Sale_Module():
  d=input("Enter the Residential Area to search:")
  l,j=eval(input(("Enter the price range to search(Lower limit,Upper limit):"))) 
  q="select * from land_record where Residential_Area='{}'and Status='Available' and Sale_Price between {} and {}".format(d,1,j)
  cur.execute(q)
  dt=cur.fetchall()
  if len(dt)!=0:
      x=PrettyTable()
      x.field_names=['Plot Number','Address','Area(sq.ft)','Sale Price']
      for r in dt:
          x.add_row([r[0],r[1],r[3],r[4]])
      print(x)
  else:
      print("Sorry no data found")

def Available_land_Module():
  q="select * from land_record where Status='Available'" 
  cur.execute(q)
  dt=cur.fetchall()
  if len(dt)!=0:
      x=PrettyTable()
      x.field_names=['Plot Number','Address','Residential Area','Area(sq.ft)','Sale Price','Rent/Lease Price']
      for r in dt:
          x.add_row([r[0],r[1],r[2],r[3],r[4],r[5]])
      print(x)
  else:
      print("Sorry no data found")

def delete():
  while True:
    i=int(input('Which category of records do you want to delete?  1.Land records 2.Sale records 3.Rent records 4.Lease records 5.Exit'))
    if i==1:
      q="select * from land_record"
      cur.execute(q)
      dt=cur.fetchall()
      if len(dt)!=0:
        x=PrettyTable()
        x.field_names=['Plot Number','Address','Residential Area','Area(sq.ft)','Sale Price','Rent/Lease Price','Status']
        for r in dt:
            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
        print(x)
      s=int(input("enter plot no you want to delete"))
      q='delete from land_record where Plot_Number={}'.format(s)
      cur.execute(q)
      mc.commit()
    if i==2:
      q="select * from sale_record"
      cur.execute(q)
      dt=cur.fetchall()
      if len(dt)!=0:
           x=PrettyTable()
           x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Sale Price']
           for r in dt:
                   x.add_row([r[0],r[1],r[2],r[3],r[4],r[5]])
           print(x)
      s=int(input("enter dealing no you want to delete"))
      q='delete from sale_record where Dealing_Number={}'.format(s)
      cur.execute(q)
      mc.commit()
    if i==3:
      q="select * from rent_record"
      cur.execute(q)
      dt=cur.fetchall()
      if len(dt)!=0:
           x=PrettyTable()
           x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Date Of Termination','Plot Number','Rent Price']
           for r in dt:
                   x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
           print(x)
      s=int(input("enter dealing no you want to delete"))
      q='delete from rent_record where Dealing_Number={}'.format(s)
      cur.execute(q)
      mc.commit()
    if i==4:
      q="select * from lease_record"
      cur.execute(q)
      dt=cur.fetchall()
      if len(dt)!=0:
        x=PrettyTable()
        x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Number Of Months Of Agreement','Lease Total']
        for r in dt:
                   x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
        print(x)
      s=int(input("enter dealing no you want to delete"))
      q='delete from lease_record where Dealing_Number={}'.format(s)
      cur.execute(q)
      mc.commit()
    if i==5:
      break

def termination():
      q="select * from rent_record where Date_Of_Termination = '0000-00-00'"
      cur.execute(q)
      dt=cur.fetchall()
      if len(dt)!=0:
           x=PrettyTable()
           x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Rent Price']
           for r in dt:
                   x.add_row([r[0],r[1],r[2],r[3],r[5],r[6]])
           print(x)
      print("")
      s=int(input("Enter the dealing number you want to end the contract"))
      si=int(input("Enter the corresponding plot number"))
      kk=input("Enter the Date Of Termination(yyyy-mm-dd)")
      print("Successful")
      print("")
      y="Available"
      h="update land_record set Status='{}' where Plot_Number={}".format(y,si)
      cur.execute(h)
      mc.commit()
      q="update rent_record set Date_Of_Termination='{}' where Dealing_Number={}".format(kk,s)
      cur.execute(q)
      mc.commit()
      
def performance():
    while True:
        x=int(input('''Would you like to generate
                1)Yearly performance report
                2)Monthly performance report
                    [Press 0 to exit]'''))
        print("")
        if x==1:
            c=int(input('''1)Display the performance for a particular year
2)Display the performance of multiple years '''))
            if c==2:
                price1=price2=price3=0
                n1=n2=n3=0
                a=input("Enter the starting year: ")
                b=input("Enter the end year: ")
                p=a+"-01-01"
                t=b+"-12-31"
                print("*****SALES*****")
                q="select * from sale_record where Date_Of_Agreement between '{}' and '{}'".format(p,t)
                cur.execute(q)
                dt=cur.fetchall()                
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Sale Price']
                    for r in dt:
                        x.add_row([r[0],r[1],r[2],r[3],r[4],r[5]])
                        price1=price1+r[5]
                        n1+=1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n1)
                print("Income generated from sale is ",price1)

                print("*****RENT*****")
                q="select * from rent_record where Date_Of_Agreement between '{}' and '{}'".format(p,t)
                cur.execute(q)
                dt=cur.fetchall()                
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Date Of Termination','Plot Number','Rent Price','No.of Months','Total Rent']
                    for r in dt:
                        print("Dealing Number:",r[0],"Customer Name:",r[1],"Customer Contact Number:",r[2],"Date Of Agreement:",r[3],"Date Of Termination",r[4])
                        nom=int(input("Enter the number of months of rent for the above: "))
                        tot=r[6]*nom
                        price2=price2+tot
                        n2+=1
                        x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6],nom,tot])
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n2)
                print("Income generated from rent is ",price2)

                print("*****LEASE*****")
                q="select * from lease_record where Date_Of_Agreement between '{}' and '{}'".format(p,t)
                cur.execute(q)
                dt=cur.fetchall()                
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','No.of Months Of Agreement','Total Lease']
                    for r in dt:
                        x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
                        price3=price3+r[6]
                        n3+=1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n3)
                print("Income generated from lease is ",price3)
                print("")
                print("THE TOTAL DEALS ARE: ",n1+n2+n3)
                print("TOTAL INCOME GENERATED IS: ",price1+price2+price3)
            if c==1:
                price1=price2=price3=0
                n1=n2=n3=0
                h=input("Enter the year: ")
                print("*****SALES*****")
                q="select * from sale_record"
                cur.execute(q)
                dt=cur.fetchall()                
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Sale Price']
                    for r in dt:
                        j=str(r[3])
                        if j[0:4]==h:
                            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5]])
                            price1=price1+r[5]
                            n1+=1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n1)
                print("Income generated from sale is ",price1)

                print("*****RENT*****")
                q="select * from rent_record"
                cur.execute(q)
                dt=cur.fetchall()                
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Date of Termination','Plot Number','Rent Price','No.of Months','Total Rent']
                    for r in dt:
                        j=str(r[3])
                        if j[0:4]==h:
                            print("Dealing Number:",r[0],"Customer Name:",r[1],"Customer Contact Number:",r[2],"Date Of Agreement:",r[3],"Date Of Termination",r[4])
                            nom=int(input("Enter the number of months of rent for the above: "))
                            tot=r[6]*nom
                            price2=price2+tot
                            n2+=1
                            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6],nom,tot])
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n2)
                print("Income generated from rent is ",price2)

                print("*****LEASE*****")
                q="select * from lease_record"
                cur.execute(q)
                dt=cur.fetchall()                
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','No.of Months Of Agreement','Total Lease']
                    for r in dt:
                        j=str(r[3])
                        if j[0:4]==h:
                            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
                            price3=price3+r[6]
                            n3+=1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n3)
                print("Income generated from lease is ",price3)
                print("")
                print("THE TOTAL DEALS ARE: ",n1+n2+n3)
                print("TOTAL INCOME GENERATED IS: ",price1+price2+price3)
        if x==2:
            d=input("Which year are you interested in? ")
            c=int(input('''1)Display the performance for a particular month
2)Display the performance of multiple months '''))
            if c==2:
                price1=price2=price3=0
                n1=n2=n3=0
                a=input("Enter the starting month(mm): ")
                b=input("Enter the end month(mm): ")
                if b in ["01","03","05","07","08","10","12"]:
                    c="-31"
                elif b=="02":
                    c="-28"
                else:
                    c="-30"
                p=d+"-"+a+"-01"
                t=d+"-"+b+c
                print("*****SALES*****")
                q="select * from sale_record where Date_Of_Agreement between '{}' and '{}'".format(p,t)
                cur.execute(q)
                dt=cur.fetchall()
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Sale Price']
                    for r in dt:
                        x.add_row([r[0],r[1],r[2],r[3],r[4],r[5]])
                        price1=price1+r[5]
                        n1=n1+1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n1)
                print("Income generated from sale is ",price1)

                print("*****RENT*****")
                q="select * from rent_record where Date_Of_Agreement between '{}' and '{}'".format(p,t)
                cur.execute(q)
                dt=cur.fetchall()
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Date Of Termination','Plot Number','Rent Price','No.of Months','Total Rent']
                    for r in dt:
                        print("Dealing Number:",r[0],"Customer Name:",r[1],"Customer Contact Number:",r[2],"Date Of Agreement:",r[3],"Date Of Termination",r[4])
                        nom=int(input("Enter the number of months of rent for the above: "))
                        tot=r[6]*nom
                        price2=price2+tot
                        n2+=1
                        x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6],nom,tot])
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n2)
                print("Income generated from rent is ",price2) 

                print("*****LEASE*****")
                q="select * from lease_record where Date_Of_Agreement between '{}' and '{}'".format(p,t)
                cur.execute(q)
                dt=cur.fetchall()
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','No.of Months Of Agreement','Total Lease']
                    for r in dt:
                        x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
                        price3=price3+r[6]
                        n3=n3+1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n3)
                print("Income generated from lease is ",price3)
                print("")
                print("THE TOTAL DEALS ARE: ",n1+n2+n3)
                print("TOTAL INCOME GENERATED IS: ",price1+price2+price3)
            if c==1:
                price1=price2=price3=0
                n1=n2=n3=0
                h=input("Enter the month(mm): ")
                print("*****SALES*****")
                q="select * from sale_record"
                cur.execute(q)
                dt=cur.fetchall()                
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Sale Price']
                    for r in dt:
                        j=str(r[3])
                        if j[0:7]==d+"-"+h:
                            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5]])
                            price1=price1+r[5]
                            n1+=1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n1)
                print("Income generated from sale is ",price1)

                print("*****RENT*****")
                q="select * from rent_record"
                cur.execute(q)
                dt=cur.fetchall()               
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Date of Termination','Plot Number','Rent Price']
                    for r in dt:
                        j=str(r[3])
                        if j[0:7]==d+"-"+h:
                            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
                            price2=price2+r[6]
                            n2+=1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n2)
                print("Income generated from rent is ",price2)

                print("*****LEASE*****")
                q="select * from lease_record"
                cur.execute(q)
                dt=cur.fetchall()               
                if len(dt)!=0:
                    x=PrettyTable()
                    x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','No.of Months Of Agreement','Total Lease']
                    for r in dt:
                        j=str(r[3])
                        if j[0:7]==d+"-"+h:
                            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
                            price3=price3+r[6]
                            n3+=1
                    print(x)
                else:
                    print("Sorry no data found")
                print("The number of deals are ",n3)
                print("Income generated from lease is ",price3)
                print("")
                print("THE TOTAL DEALS ARE: ",n1+n2+n3)
                print("TOTAL INCOME GENERATED IS: ",price1+price2+price3)
        if x==0:
            break
          
def displayland():
  while True:  
    i=int(input('which category of records do you want to see?  1.land records 2.sale records 3.rent records 4.lease records 5.Exit'))
    if i==1:
      q="select * from land_record"
      cur.execute(q)
      dt=cur.fetchall()
      print(dt)
      if len(dt)!=0:
        x=PrettyTable()
        x.field_names=['Plot Number','Address','Residential Area','Area(sq.ft)','Sale Price','Rent/Lease Price','Status']
        for r in dt:
            x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
        print(x)
    if i==2:
      q="select * from sale_record"
      cur.execute(q)
      dt=cur.fetchall()
      if len(dt)!=0:
           x=PrettyTable()
           x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Sale Price']
           for r in dt:
                   x.add_row([r[0],r[1],r[2],r[3],r[4],r[5]])
           print(x)
    if i==3:
      q="select * from rent_record"
      cur.execute(q)
      dt=cur.fetchmany()
      print(dt)
      if len(dt)!=0:
           x=PrettyTable()
           x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Date Of Termination','Plot Number','Rent Price']
           for r in dt:
                   x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
           print(x)
    if i==4:
      q="select * from lease_record"
      cur.execute(q)
      dt=cur.fetchone()
      print(dt)
      if len(dt)!=0:
        x=PrettyTable()
        x.field_names=['Dealing Number','Customer Name','Customer Contact Number','Date Of Agreement','Plot Number','Number Of Months Of Agreement','Lease Total']
        for r in dt:
                   x.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
        print(x)            
    if i==5:
      break

    

print("                                                                              R E A L  E S T A T E  M A N A G E M E N T ")
print("                                                                        =====================================================")
print("")
dtb=input("                                                 ENTER 0 TO SETUP A NEW DATABASE ON THE DEVICE, IF ALREADY EXISTS PRESS ANY OTHER KEY TO PROCEED ")
print("")
if dtb=="0":
        cur.execute("create database real_estate_management")
        mc.commit
        CreateSaleRecord()
        CreateRentRecord()
        CreateLeaseRecord()
        CreateLandRecord()
cur.execute("use real_estate_management")
mc.commit
print("WELCOME TO REAL ESTATE MANAGEMENT SYSTEM...")
print("")
while True:
    user=int(input('''    1-->USER LOGIN
    2-->ADMIN LOGIN
    3-->EXIT '''))
    print("")
    if user==2:
        while True:
         k=int(input('''(Press 0 to go back)
ENTER ADMIN PASSWORD: '''))
         print("")
         if k==0:
             break
         if k==1:
            print("")                                 
            while True:
             print("   WELCOME ADMINISTRATOR!!")
             print("")
             print(" 1. Make a new entry")
             print(" 2. View existing records")
             print(" 3. Delete records"      )
             print(" 4. End agreement(For Rent)")
             print(" 5. View Available plots")
             print(" 6. Search for a suitable property")
             print(" 7. View Performance")
             print(" 8. Go back")             
             print("")
             s=int(input("What do you wish to do? "))
             print("")                             
             if s==1:
                d=int(input('''Which entry would you like to make?
1.Land record
2.Sale record
3.Rent record
4.Lease record '''))
                print("")
                if d==1:
                    insertland()
                if d==2:
                    insertsale()
                if d==3:  
                    insertrent()
                if d==4:
                     insertlease()
                if type(s)is int:
                    continue

             if s==2:
                displayland()
                if type(s)is int:
                    continue

             if s==3:
               delete()

             if s==4:
               termination()

             if s==5:
                  Available_land_Module()
                  if type(s)is int:
                      continue
             if s==6:
                d=int(input('''Which type of property are you interested in?
1.Property for SALE
2.Property for RENT
3.Property for LEASE '''))
                print("")
                if d==1:
                    Sale_Module()
                if d==2:
                    Rent_Module()
                if d==3:  
                    Lease_Module()
                if type(s)is int:
                    continue

             if s==7:
               performance()               
               
             if s==8:
                break
             
    if user==1:
        while True:
         k=int(input('''(Press 0 to go back)
ENTER USER PASSWORD: '''))
         print("")
         if k==0:
             break
         if k==2004:             
             while True:
               print("   WELCOME TO OUR AGENCY!!")
               print("")
               print(" 1. View Available plots" )
               print(" 2. Search for a suitable property")
               print(" 3. Go back" )
               print("")
               s=int(input("What do you wish to do? "))
               print("")                
               if s==1:
                  Available_land_Module()
                  if type(s)is int:
                      continue
               if s==2:
                d=int(input('''Which type of property are you interested in?
1.Property for SALE
2.Property for RENT
3.Property for LEASE '''))
                print("")
                if d==1:
                    Sale_Module()
                if d==2:
                    Rent_Module()
                if d==3:  
                    Lease_Module()
                if type(s)is int:
                    continue
               if s==3:
                  break
    if user==3:
        break






  












































