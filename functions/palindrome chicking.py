word = "racecar"

l = len(word)
palindrome_flag = True
for i in range(l):
    if word[i] != word[l-i-1]:
        palindrome_flag = False
        break
    else:
        palindrome_flag = True
if palindrome_flag:
    print("string is palindrome")
else:
    print("string is not palindrome")