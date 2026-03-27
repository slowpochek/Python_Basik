def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalpha())
    return cleaned == cleaned[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == True  # бо залишається "p"
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("OK")