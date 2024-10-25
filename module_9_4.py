first = 'Мама мыла раму'
second = 'Рамена мало было'

m = list(map(lambda x, y: x == y, first, second))
print(m)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as f:
            for data in data_set:
                f.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])