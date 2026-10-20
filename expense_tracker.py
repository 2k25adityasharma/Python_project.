#expense tracker 
expense=[]
while True:
    print("Press 1 for add expenses")
    print("Press 2 for view")
    print("Press 3 for Total_Ammount")
    print("Press 4 for Exit")
    
    try :
        check = int(input("chose between 1 to 4 :- "))
    except Exception as err:
        print("Type betwenn 1 to 4")
        continue
        

#Adding        
    
    if check ==1:
        date =input("Enter Date :- ")
        catagory =input("Enter catagory :- ")
        description =input("Enter description :- ")
        amount =float(input("Enter amount :- "))
        
        dict={"date":date,
              "catagory":catagory,
              "description":description,
              "amount":amount
              }
        expense.append(dict)
        print("                      ")
        print("Done Bro........Want to add more")
        print("                      ")
        
        
#check        
    elif check==2:
        if len(expense)==0:
            print("                      ")
            print("Nothing added bro")
            print("                      ")
        else:
            count =0
            for i in expense:
                print(f"{count}:-,Date:-{i["date"]},Catagory:-{i["catagory"]},Description:-{i["description"]},Amount:-{i["amount"]}")
                count+=1
# total        
    elif check==3:
        sum=0
        for i in expense:
            sum+=i["amount"]
        print("                      ")
        print("your total ammount is :- ",sum)    
        print("                      ")
        
        
        
#Exit    
    elif check==4:
        print("                      ")
        print("Exit.......")
        print("                      ")
        break
    
    else:
        print("                      ")
        print("choose among 1 to 4")
        print("                      ")
        continue
