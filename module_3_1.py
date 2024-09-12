calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string: str) -> tuple[int, str, str]:
    count_calls()
    return  (len(string), string.upper(), string.lower())

def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    for element in list_to_search:
        if not isinstance(element, str):
            continue
        other: str = element
        if other.upper() == string.upper():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)