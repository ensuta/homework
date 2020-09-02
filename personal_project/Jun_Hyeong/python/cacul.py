# 더하기
def add(x, y):
    return x + y

# 빼기
def subtract(x, y):
    return x - y

# 곱하기
def multiply(x, y):
    return x * y

# 나누기
def divide(x, y):
    return x / y


print("계산방식.")
print("1.덧셈")
print("2.뻴셈")
print("3.곱하기")
print("4.나누기")

while True:
    
    choice = input("선택택(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("첫번째 숫자:\n "))
        num2 = float(input("두번째 숫자:\n "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("값이 주어지지 않은")