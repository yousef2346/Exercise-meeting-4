""" Write a program that reads words (“finish” to stop). The program then should count and
 print the number of words that start with character ‘a"""


user_input = str(input("Enter your word & 'finish to EXIT' => "))
a_counted_words = 0
while user_input != "finish":
    if user_input.startswith("a"):
        a_counted_words+=1

    user_input = str(input("Enter your word & 'finish to EXIT' => "))

print(f"There's {a_counted_words} words started with 'a'\n")
