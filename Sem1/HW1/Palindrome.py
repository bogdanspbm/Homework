def isPalindrome(word):
    for i in range(int(len(word) / 2) + 1):
        if word[i] != word[-i-1]:
            print('Not palindrome')
            return
    print('Palindrome')

isPalindrome(input('Enter word: ').lower())
