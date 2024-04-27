values=[2,4,1,-3,-5,7]
negative_value=sum(i for i in values if i<0)
positive_value=sum(j for j in values if j%2==0)
#odd_values=sum(k for k in values if k%2 !=0)
print(negative_value)
print(positive_value)
#print(odd_value)