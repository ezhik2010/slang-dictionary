meme_dict = {
            "КРИНЖ": "что-то очень странное или стыдное",
            "ЛОЛ": "что-то очень смешное",
            "РОФЛ": "шутка",
            "ЩИЩ": "одобрение или восторг",
            "КРИПОВЫЙ": "страшный",
            "АГРИТЬСЯ": "злиться"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print(word, (" - это "), meme_dict[word])
else:
    print("Такого слова пока что в словаре нет")