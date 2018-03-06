phrase = "I like pie"

"""
#ex 1
print(phrase.upper())

#ex2
print(phrase.capitalize())


#ex3 
l = len(phrase)
p = list(phrase)
for i in range(l-1,-1,-1):
    print(p[i],end="")
    
    
#e4

"""

convert = {"A":"4", "E":"3", "G":"6", "I":"1", "O":"0", "S":"5", "T":"7"}
phrase = list(input("phrase?"))
l = len(phrase)
for i in range(0,l):
    if phrase[i] in convert.keys():
        phrase[i]=convert[phrase[i]]

phraseString = "".join(phrase)
print(phraseString)