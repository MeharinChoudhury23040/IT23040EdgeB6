import sys

args=sys.argv[1:]
numbers=[int(num) for num in args]
    
result=0

for num in numbers:
    if num%2==0:
          result+=num**3

print("Sum of cubes of even numbers:",result)
