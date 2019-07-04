a,b = map(int,input().split())  

for num in range(a+1,b):
    temp = num
    sum = 0
    while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10
    if num == sum:  
       print(num,end=" ")
    
