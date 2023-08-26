input_string = input("Enter a word: ")
is_palindrome = True

length = len(input_string)
for i in range(length // 2):
    if input_string[i] != input_string[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
