first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(w) for w in first_strings if len(w) > 5]
second_result = [ (x,y) for x in first_strings for y in second_strings
                 if len(x) == len(y)]
third_result = {w:len(w) for w in first_strings + second_strings if len(w) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)