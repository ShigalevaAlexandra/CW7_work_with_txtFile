def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length_words = len(max(words, key=len))

        sought_words = [
            word for word in words if len(word) == max_length_words
        ]

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print("\n Самое длинное слово из файла article.txt: \n", longest_words('File_txt/article.txt'))