def divisors(num):
    if num < 0:
        raise ValueError
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    try:
        num = int(input('Ingresa un número:'))
        print(divisors(num))
        print("temino mi programa")
    except ValueError:
        print("Debes ingresar un número positivo") 
if __name__ == '__main__':
    run()