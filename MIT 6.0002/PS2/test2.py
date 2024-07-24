# read the input
number = float(input("Input a number of gigabytes: "))
# compute the result, using multiple variables

mb = int(number%1*1024)
kb = int(number%1*1024%1*1024)
b = int(number%1*1024%1*1024%1*1024)
gb = int(number)

#gb =  int(number)
#mb = int((number - gb)*1024)

# output the result on one line (see examples)
print(number ,"GB =", gb ,"GB,", mb ,"MB,", kb ,"KB,", b ,"B")