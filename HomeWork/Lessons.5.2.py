# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string
symbols=string.punctuation
test_value= ("Python Community","i like python community!","Should, I. subscribe? Yes!")

for current_value in test_value:
    current_value= current_value.title()
    new_string=""
    for ch in current_value:
        if ch not in symbols and ch != " ":
            new_string+=ch
    new_string=new_string[:140]
    print("#" + new_string)



