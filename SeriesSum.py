def SeriesSum(n):
    return n*(n+1)//2 

n=int(input("Enter the value of n: "))

sum_result=SeriesSum(n)

print("The sum of the series 1 to",n,"is: ",sum_result)
