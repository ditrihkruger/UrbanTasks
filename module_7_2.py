def custom_write(file_name: str, strings: list[str]) -> dict:
    f = open(file_name, 'w', encoding = 'utf-8')
    strings_positions = {}
    strings_wrote_amount = 0
    for string in strings:
        strings_wrote_amount += 1
        strings_positions[strings_wrote_amount, f.tell()] = string
        f.write(string + '\n')
    f.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)