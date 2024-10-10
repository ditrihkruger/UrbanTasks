symbols = [',', '.', '=', '!', '?', ';', ':', '-']

class WordsFinder:
    __file_names: tuple[str]

    def __init__(self, *file_names):
        self.__file_names = file_names

    def get_all_words(self) -> dict[str, list[str]]:
        all_words = {}
        for file_name in self.__file_names:
            all_words[file_name] = []
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read()
                words = content.split()
                for word in words:
                    word.lower()
                    for symbol in symbols:
                        word = word.replace(symbol, '')
                    if word == '':
                        continue
                    all_words[file_name].append(word)
        return all_words

    def find(self, word: str) -> dict[str, int]:
        d = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, word_list in all_words.items():
            if word in word_list:
                d[file_name] = word_list.index(word) + 1
                continue
        return d

    def count(self, word: str) -> dict[str, int]:
        d = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, word_list in all_words.items():
            d[file_name] = word_list.count(word)
        return d


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

