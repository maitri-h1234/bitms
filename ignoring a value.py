# ignoring a value
a,_,c=(1,2,3) # a=1,b=3
print(a,_,c)


#ignoring multiple values
a,*_,b=(7,6,5,4,3,2,1)
print(a,b)