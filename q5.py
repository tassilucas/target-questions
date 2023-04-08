
data = input("Digite a string a ser invertida: ")

def reverse_string(data):
    arr = list(data)
    start = 0
    end = len(arr) - 1

    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp

        start += 1
        end -= 1

    return ''.join(arr)

print(reverse_string(data))
