#A chocolate factory is packing chocolates into the packets. 
#The chocolate packets here represent an array 
#of N number of integer values.The task is to 
#find the empty packets(0) of chocolate and 
#push it to the end of the conveyor belt(array).
#Input :
#7– Value of N
#[4,5,0,1,0,0,5]

#Output:

#4 5 1 9 5 0 0

#code:

n=int(input("Enter size:"))

j=0
v=[0 for i in range(n)]
for i in range(n):
    a=int(input("please enter elements:"))
  
    if a!=0:
        v[j]=a
        j+=1
for i in v:
    print(i,end=" ")