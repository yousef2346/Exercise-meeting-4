x = int(input("Enter a positive number & 0 to EXIT => "))
array = []
even_count =0
odd_count =0

while x != 0:
    array.append(x)
    x = int(input("Enter a positive number & 0 to EXIT => "))


for i in array:
    if i % 2 ==0:
        even_count+=1
    else :
        odd_count+=1

print(f"\nYou have Entered |{even_count}| Even Numbers\nAnd |{odd_count}| Odd Numbers")