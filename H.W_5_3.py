import string

my_string = input('введи рядок')
my_string_1 = my_string.title()
print(my_string_1)
words = ""
for char in my_string_1:
    if char not in string.punctuation and char != " ":
        words += char
print(words)
hashtag_words = "#" + "".join(words)
if len(hashtag_words) > 140:
    hashtag_words = hashtag_words[:140]
print(hashtag_words)
