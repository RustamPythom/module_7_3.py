class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for fileName in self.file_names:
            with open (fileName, 'r', encoding= 'utf-8' ) as file:
                content = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(i, '')
                words = content.split()
                all_words[fileName] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for fileName, words in all_words.items():
            if word.lower() in words:
                result[fileName] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for fileName, words in all_words.items():
            result[fileName] = words.count(word.lower())
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


