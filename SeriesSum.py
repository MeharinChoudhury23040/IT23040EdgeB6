def SeriesSum(n):
    return n * (n + 1) // 2  # Using integer division to ensure the result is an integer

# Taking input from the keyboard
n = int(input("Enter the value of n: "))

# Calculating the sum using SeriesSum function
sum_result = SeriesSum(n)

# Displaying the result
print("The sum of the series 1 to" ,n, "is: ", sum_result)
