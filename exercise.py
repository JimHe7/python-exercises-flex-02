#ex 1

name = input("What is your name?")
print("Hello,", name)

#ex 2
name = input("What is your name?")
print("Hello,", name.upper())
print("your name has".upper(),len(name),"LETTERS IN IT! AWESOME!")

#ex3
print("Please fill in the the blanks below:")
phrase = "'s favorite food is "
print("____(name)___",phrase,"____(food)___",sep="")

name = input("What is your name? ")
food = input("What is your favorite food? ")
print(name,phrase,food,sep="")

#ex4 works if entered line by line in terminal
week = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Sunday"}
day = int(input('Day (0-6)? '))
print(week[day])

#ex5
day = int(input('Day (0-6)? '))
if(day==0 or day==6):
    print("Sleep in")
else:
    print("Go to work")
    
#ex6
C = float(input("Temperature in C?"))
F = C *1.8 + 32
print(F,"F")

#ex7
total = float(input("Total Bill Amount? "))
level = input("Level of Service? ")
table = {"good":.2,"fair":.15,"bad":.1}
tip = table[level.lower()]*total
totalAmt = total + tip
print("Tip Amount:",'${:,.2f}'.format(tip))
print("Total Amount:",'${:,.2f}'.format(totalAmt))

#ex8
i = 1
while i < 11:
    print(i)
    i+=1


#ex9
coins = 0

print("You have",coins,"coins.")
response = input("Do you want another?")

while response !="no":
    coins +=1
    print("You have",coins,"coins.")
    response = input("Do you want another?")
    
print("Bye")