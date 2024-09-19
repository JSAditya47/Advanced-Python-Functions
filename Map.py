num1 = [1, 2, 3]
num2 = [4, 5, 6]

result = map(lambda x, y: x + y, num1, num2)
print(list(result))



number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sq(n):
    return n * n

square = map(sq, number)
print(list(square))