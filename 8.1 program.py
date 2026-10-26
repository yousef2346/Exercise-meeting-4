


""" 
Write a program that reads from the user a sentence. 
the program should count the number of occurrences of hte character 'a' in the sentence.
"""

a_occurrence = 0
sentence = str(input("Enter Your sentence => "))
a_occurrence = sentence.count("a")
print(f"\nThere's |{a_occurrence}| a's in your sentence.")