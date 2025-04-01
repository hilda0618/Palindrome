#Ms. Liu
#7th Grade Computer Science
# Palindrome program

word = input("Enter a word: ").lower()
reversed_word = ""

# Reverse the string using a loop
for char in word:
    reversed_word = char + reversed_word  # build it backwards

print("Reversed word:", reversed_word)

if word == reversed_word:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
