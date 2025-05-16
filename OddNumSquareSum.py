n=int(input("Enter number n: "))

total_sum=0
odd=1

for i in range(n):
    while odd<=n:
       total_sum+=odd**2
       odd+=2

print("Sum of all odd number's square is: ",total_sum)