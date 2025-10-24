X=int(input("X ga qiymat kiriting= "))

numbers=[]

for num in range(2, X+1):
    
    is_prime=True
    
    for now in range(2, num):
        if num % now == 0:
            is_prime=False
            
if is_prime:
    numbers.append(num)
    
print(numbers)