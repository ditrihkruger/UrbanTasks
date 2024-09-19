def calculate_structure_sum(structure: list):
    result = 0
    for data in structure:
        if isinstance(data, list) or isinstance(data, tuple):
            result += calculate_structure_sum(data)
        if isinstance(data, set):
            result += calculate_structure_sum(list(data))
        if isinstance(data, dict):
            result += calculate_structure_sum(list(data.keys()))
            result += calculate_structure_sum(list(data.values()))
        if isinstance(data, int):
            result += data
        if isinstance(data, str):
            result += len(data)
    return result

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
