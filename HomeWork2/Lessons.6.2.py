import string

text = input("Enter two letters with hyphen: ")
start, end = text.split("-")
start = start.strip()
end = end.strip()
alphabet = string.ascii_letters
start_index = alphabet.index(start)
end_index = alphabet.index(end)
result = ""
if start_index <= end_index:

    for i in range(start_index, end_index + 1):
        result += alphabet[i]
else:
    for i in range(start_index, end_index - 1, -1):
        result += alphabet[i]
print(result)