def print_even_number(n: list):
    if len(n) == 0:
        return
    x = n[0]
    if x % 2 == 0:
        print(x)
    print_even_number(n[1:])
