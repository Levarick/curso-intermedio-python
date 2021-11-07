def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
        num = input('Ingresa un número:')
        assert num.__contains__('-') == False, 'Debes ingresar un número positivo'
        assert num.isnumeric(), 'Debes ingresar un número'
        print(divisors(int(num)))
        print("Teminó mi programa")
if __name__ == '__main__':
    run()