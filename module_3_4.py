def single_root_words(root_word: str, *other_words: list[str]):
    root_word = root_word.lower()
    same_words  = []
    for word in other_words:
        if word.count(root_word) > 0 or root_word.count(word.lower()) > 0:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
