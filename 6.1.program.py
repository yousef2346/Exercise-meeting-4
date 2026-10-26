array1 = []
x = eval(input("Enter a positive number & (0 to Exit)"))

while x!=0:
    array1.append(x)
    x = eval(input("Enter a positive number & (0 to Exit)"))

maximum_value= max(array1)
minimum_value = min(array1)

print(f"The Maximum integer is {maximum_value}\nThe Minimum value is {minimum_value}")

