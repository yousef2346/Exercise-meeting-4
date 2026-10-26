"""
8.1:
Write a program that reads from the user 10 words. 
The program then should count and print the number of words that start with character ‘a’.

"""

#Old School way
a_counted_words=0

for i in range(10):
    x = str(input("Enter Your word => "))
    if x.startswith("a"):
        a_counted_words+=1




print(f"There's |{a_counted_words}| words that starts with 'a' ")

#-----------------------------------------------------------------------

#New School

a_words = []
a_count = None

for i in range(10):
    x = str(input("Enter Your word => "))
    if 'a' in x:
        a_words.append(x)
    
a_count=len(a_words)
print(f"There's |{a_count}| words that have 'a' in them")