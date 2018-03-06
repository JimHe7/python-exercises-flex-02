"""
#ex1 
for i in range (1,11):
    print(i)



#ex2
start = int(input("Start from: "))
end = int(input("End on "))

for i in range (start,end+1):
    print(i)


#ex3 
for i in range (1,11):
    if i % 2 !=0:
        print(i)



#ex4 / ex5
length = int(input("How big is the square? "))
for i in range(0,length):
    print("*"* length)



#ex 6
width = int(input("Width? "))
height = int(input("Height? "))

for h in range(0,height):
    if h == 0 or h == height-1:
        print("*"*width)
    else:
        space = " "*(max(0,width-2))
        print("*",space,"*",sep="")
        

"""
#ex 7 / ex8

# first X is at position equal to height, total length of every row is 2*height - 1
# number of rows = height
# for height = 4, first X is at position 4, three blanks
# so for height = h, row = 1, (h-1) blanks then 1 X then (h-1) blanks
# so for height = h, row = r, (h-r) blanks then (2r -1) X then (h-r) blanks

height = int(input("Height? "))

for r in range (1, height+1): 
    print(" "*(height-r),"*"*(2*r-1)," "*(height-r))
    
    
