def check_plaindrome(word):
    l = len(word)
    for i in range(l):
        if word[i]!=word[l-i-1]:
            return False
    return True

print(check_plaindrome("python"))