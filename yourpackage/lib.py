def try_me(n):
    """Fibonacci !"""
    if n == 0 or n == 1:
        return 1
    else:
        return try_me(n-1) + try_me(n-2)

if __name__ == '__main__':
    print(f'Fibonacci for n=5 : {try_me(5)}')
