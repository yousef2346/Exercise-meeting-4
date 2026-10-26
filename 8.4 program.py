"""
Write a program that reads from the user 10 words.
The program then should find and print the longest word.
"""
largest_len = int()
longest_word = None
for i in range(10):
    x = input("Enter your word => ")
    if len(x) > largest_len:
        largest_len = len(x)
        longest_word = x

print(f"The longst word is '{longest_word}'")

