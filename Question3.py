## Write a Python program to count the number of even and odd numbers from a series of numbers.


a=0
b=0

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    if int(i)%2==0:
        a+=1
    else:
        b+=1
print('no. of even numbers--->',a)
print('no. of odd numbers--->',b)