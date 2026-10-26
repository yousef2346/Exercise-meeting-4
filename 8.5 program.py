
"""
Write a program that reads from the user 10 words. 
The program then should find and print the shortest word.
"""

smallest_len = 1000
shortest_word = None
for i in range(10):
    x = input("Enter your word => ")
    if len(x) < smallest_len:
        smallest_len= len(x)
        shortest_word = x

print(f"The shortest word is '{shortest_word}'")

