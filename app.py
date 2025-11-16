import math

# VARIABLES

st_cnt = 1000
print(st_cnt)

rating = 4.99
is_public = False

message = """
   Hello John,
     Its Pranav.....
"""


course  =  "Python"
print(len(course))

#STRINGS 

print(course[0:3])

#ESCAPE SEQ
#\"
#\'
#\\
#\n


#FORMAT STRINGS
f= 'Hello'
l= "India"

print(f+l)

full= f"{f}{l}"
print(full)

#STRING FUNCTIONS
a= "PRANAV"
print(a.upper())
a.title()

#TO REMOVE WHITESPACES
c= "  Hii"
print(c.strip())

print(a.find("PR")) #returns index
print("PR" in a) #returns boolean

#NUMBERS

n= 2+ 3j #Complex number

n=3.7
a= math.cos(0)
print(a)


