def code(number: int) -> None:
    print(f"{number} - ", end="")
    deviders = []
    for devider in range(2, number+1):
        if number % devider == 0:
            deviders.append(devider)
    for i in range(1, deviders[-1] // 2 + deviders[-1] % 2):
        for devider in deviders:
            if devider // 2 < i:
                continue
            if (devider - i == i):
                continue
            print(i, devider - i, sep="", end="")
    print()

for i in range(3, 21):
    code(i)