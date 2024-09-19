def test_function():
    def inner_function():
        print("Я в области видимости функции")

    inner_function()

test_function()
try:
    inner_function()
except Exception as e:
    print(e)
