'''Simple calculator to perform basic arithmetic operations'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if (b==0):
        return "Error Can't divide with zero"
    else:
        return a/b
choice=1
while(choice):
    print("Select the operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Mulriplication")
    print("4.Division")
    ch=int(input("Enter your choice:"))
    if ch in [1,2,3,4]:
        first_number=int(input("Enter the first number:"))
        second_number=int(input("Enter the second number:"))
        if ch==1:
            print(first_number,"+",second_number,":",add(first_number,second_number))
        elif ch==2:
            print(first_number,"-",second_number,":",sub(first_number,second_number))
        elif ch==3:
            print(first_number,"*",second_number,":",mul(first_number,second_number))
        elif ch==4:
            print(first_number,"/",second_number,":",div(first_number,second_number))
        choice=int(input("Do you want to continue:YES(1)/NO(0):"))
        if choice !=1:
            break
    else:
        print("Invalid choice ")
    