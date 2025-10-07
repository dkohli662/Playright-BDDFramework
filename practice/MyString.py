# strings are case senstivie thats is A and a are different and are immutable in nature their value
#can not be changes once assigned

str="Deepika Kohli" # index starts from 0
print(str)
print(str[1])
print(str[0:7]) # string slicing will print from 0 to 6
print(str[-1]) # navigates from back so will give last indexed value->i
str1="you are great"
print(str+str1) # concatanation of two strings

str3="Kohli"
print(str3 in str) # check whether str3 is present in str or not returns T or F

var=str.split(" ") # breaker should be giving between ""
print(var)
print(var[0])

## use strip to remove white blank spaces- will pass both side spaces
# lstrip will remove only left side spaces & rstrip will do same from right side

str4="    Great    "
print(str4.strip())
print(str4)
print(str4.lstrip())
print(str4.rstrip())