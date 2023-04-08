
def in_fib(number):
    s = 0
    n = 1

    while True:
        term = s + n
        s = n
        n = term

        if term == number:
            return True

        if term > number:
            return False


def check(number):
    if in_fib(int(number)):
        print("Este número pertence a sequência de Fibonacci")
    else:
        print("Este número NÃO pertence a sequência de Fibonacci")

check(input("Digite um valor"))
