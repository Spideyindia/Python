#Basic Print Statement
print("Abhishek, wrote this!")

#Comments-1
#Single line comments - #
'''
Multiline comments are not supported but can be mimicked\
using docs string (''' ''') 

To save multiple line string
'''

print("Abhishek, wrote this! x 2")

#Variables-2
varName = 'Abhishek'
varName2 = "Ghortale"
varName3 = "Abhishek is my friend!"

#Rules - Var(s) 
# 1. Numbers can't be used as beginning of var name (1varname)
# 2. Space can't be used between var name (var name)
# 3. Special Chars can't be used for naming vars (var$name) (Allowed _ (underscore))

#Naming conventions (camelCase, PascalCase, snake_case)
startsWithSmallThenEachWordFirstCharIsinCaps = 'value' #Camel case
AllWordsStartWithFirstCharCaps = 'value' #Pascal case
always_small_case_with_words_connected_using_underscore = 'value' #Snake Case

#Data types in Python
'''
variables stores data types 

int
float
complex
str
bool
'''
var1 = 11 # -12 , -23432, 0
print(type(var1)) #<class 'int'>

var2 = 1.5 # 3/2 , all written in p/q format or decimals
print(type(var2)) #<class 'float'>

var3 = '1.12' # 'something in quotes'
print(type(var3)) #<class 'str'>

var4 = 123j # only char 'j' is allowed : j stands for 'iota' complex maths symbol
print(type(var4)) #<class 'complex'>

var5 = "String could be stored using single or double quotes"

print(type(var5)) #<class 'str'>

var6 = 'a'
var7 = 'aaaaa'
var8 = "a"
var9 = "aaaaa"

var10 = True
# var11 = true  # Won't work
var12 = False
# var13 = false # Won't work

print(type(var10))
print(type(var12))