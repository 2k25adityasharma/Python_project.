print("Enter 1 to add student ")
print("Enter 2 to view student ")
print("Enter 3 to searchid ")
print("Enter 4 to Update ")
print("Enter 5 to Delete ")
print("Enter 6 to Exit ")

while True:
    try:
         n = int(input("Type 1,2,3,4,5,6 :-"))
    except Exception as err:
        print("Eroor:",err)
        continue
   
    # add a student 
    if n==1:
        try:
            st_id = int(input("enter id :-"))
        except Exception as err:
            print("Eror: ",err)
            continue
        
        with open("Student.txt",'r') as c :
            f=0
            for i in c:
                line =i.split()
                if line[0]==str(st_id):
                    
                    f=1
                    break
                
        if f==1:
            print("Alredy")
               
        else:    
            name = input("enter name :-")
            with open("Student.txt",'a') as f :
                     f.write(f'{st_id} {name} \n')
     
       
        
    elif n==2:
        try:
            with open("Student.txt",'r') as r:
                print(r.read())
        except Exception as err:
                    print("error:",err) 
    elif n==3:
        with open("Student.txt",'r') as s:
            
            search=input("Enter student to search by id :-")
            f=0
            for i in s:
                part = i.split()
               
                if part[0]==search:
                    print(" ".join(part[1:]))
                    f=1
            if f==0:    
                print("not found")
                
    elif n==4:
        students=[]
        f=0
        with open("Student.txt",'r') as u:
            update= input("which id u wnat to update :")
            for i in u:
                part=i.split()
                if part[0]==update:
                    f=1
                    try:
                    
                        what =int(input("Press 1 for id update \nPress 2 for name update"))
                    except Exception as err:
                        print("Error:-",err)    
                        continue
                    if what==1:
                        to = input("type id :-")
                        part[0]=to
                    elif what==2:
                        to =input("enter name:-")
                        part=part[0:1]
                        part.append(to)
                students.append(" ".join(part))      
                  
        if f==0:
            print("invalid id")    
        else:
            
            with open("Student.txt",'w') as u:
               for i in students:
                   u.write(i+ "\n") 
                   
                   
            print("Student updated successfully!")           
        
            
    
    
      
    elif n == 5:
        students = []
        f = 0

        delete_id = input("Enter ID to delete: ")

        with open("Student.txt", "r") as u:
            for i in u:
                part = i.split()
 
                if part[0] == delete_id:
                    f = 1
                    continue

                students.append(" ".join(part))

        if f == 0:
            print("Invalid ID")
        else:
            with open("Student.txt", "w") as u:
                for student in students:
                    u.write(student + "\n")

            print("Student deleted successfully!")
         
    elif n==6:
        print("Exit...")
        break
    
    else:
        print("Please enter a number from 1 to 6")


    
         
