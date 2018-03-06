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



convert = {"A":"4", "E":"3", "G":"6", "I":"1", "O":"0", "S":"5", "T":"7"}
phrase = list(input("phrase?"))
l = len(phrase)
for i in range(0,l):
    if phrase[i] in convert.keys():
        phrase[i]=convert[phrase[i]]

phraseString = "".join(phrase)
print(phraseString)

"""

#e6

#use ascii code to cycle through alphabet 
# "a" is 97, "z" is 122
#at code 110 need to shift back to 97 since moving out of 26 letter range

code = []

for n in range(97,110):
    code.append(chr(n+13))
    
for k in range(110,123):
    code.append(chr(k-13))

#generate list of alphabet, combine both lists into a dictionary

alphabet = []
for a in range(97,123):
    alphabet.append(chr(a))

translator = dict(zip(code,alphabet))

phrase = list(input("phrase? "))
l = len(phrase)

for i in range(0,l):
    if phrase[i] in translator.keys():
        phrase[i]=translator[phrase[i]]

phraseString = "".join(phrase)
print(phraseString)