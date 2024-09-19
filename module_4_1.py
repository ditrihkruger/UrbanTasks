import fake_math
import true_math

result1 = fake_math.devide(69, 3)
result2: int = 0
try:
    result2 = fake_math.devide(3, 0)
except Exception as e:
    print(e)
    
result3 = true_math.devide(49, 7)

result4: int = 0
try:
    result4 = true_math.devide(15, 0)
except Exception as e:
    print(e)

print(result1)
print(result2)
print(result3)
print(result4)
