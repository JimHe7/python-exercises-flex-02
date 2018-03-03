
# ex1 
list2 = [2,3,4,1,3,-1,0,-5]


sum = 0
for i in range (0,len(list)):
    sum +=list2[i]
    
print(sum)


#ex 2 

print(max(list2))

#ex3 

print(min(list2))

#ex4
for i in range (0,len(list2)):
    if list2[i] % 2 == 0:
        print(list2[i])
        


#ex5
for i in range (0,len(list2)):
    if list2[i] > 0:
        print(list2[i])
        


#ex6
list2 =[]
for i in range (0,len(list)):
    if list[i] > 0:
        list2.append(list[i])
        
print(list2)



#ex7
factor = 3
list3 = []
for i in range (0,len(list)):
    list3.append(list[i]*3)

print(list3)



#ex8
vector1 = [13,4,3,2,4]
vector2 = [3,4,5,6,32]
vector3 = []
for i in range (0,len(vector1)):
    vector3.append(vector1[i]+vector2[i])
    
print(vector3)


#ex9
matrix1 = [[1,3],[2,4]]
matrix2 = [[5,2],[1,0]]
matrix3 = []
temp = []
for i in range (0,len(matrix1)):
    
    temp=[]
    
    for k in range (0,len(matrix1[0])):
        temp.append(matrix1[i][k]+matrix2[i][k])
    matrix3.append(temp)

print(matrix3)

#ex10

matrix1 = [[1,3,4,13,1],[2,4,4,1,2],[1,2,3,4,5]]
matrix2 = [[5,2,4,45,3],[1,0,41,3,1],[4,4,3,2,1]]
matrix3 = []
temp = []
for i in range (0,len(matrix1)):
    
    temp=[]
    
    for k in range (0,len(matrix1[0])):
        temp.append(matrix1[i][k]+matrix2[i][k])
    matrix3.append(temp)

print(matrix3)


#ex 11 A out of order
list1 = [1,2,3,5,5,5,5,3,1,2,3,4]
set1 = set(list1)
out = list(set1)
print(out)


#ex 11 B same order
list1 = [1,2,3,5,5,5,5,3,1,2,3,4]
unique =[]

for i in list1:
    if i in unique:
        pass
    else:
        unique.append(i)
print(unique)
