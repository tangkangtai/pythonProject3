
#----------if语句---------
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

print('END')

#-----------------------
if age >= 18:
    print('adult')

if age < 18:
    print('teenage')

if not age >= 18:
    print('teenager')

#-------------------
if age >= 19:
    print('adult')
else:
    print('teenager')

#----------
if age >= 18:
    print('adult')
else:
    if age >= 6:
        print('teenager')
    else:
        print('kid')

#--------------
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
elif age >= 3:
    print('kid')
else:
    print('baby')

#-----------------