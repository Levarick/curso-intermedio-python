def run():
    my_list = [1, "Hello", True, 4.5]
    my_list = {"firstname": "Facundo", "lastname": "García"}
    square =  []
    for i in range(1, 101):
        if i % 3 != 0:
            square.append(i*i)

    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "García"},
        {"firstname": "Susana", "lastname": "García"},
        {"firstname": "Jose", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43],
    }

    

    for key, value in super_dict.items():
        print(key, '-', value)

    for item in super_list:
        print(item["firstname"], item["lastname"])

    for item in square:
        print(item)

    # List comprehensions
    quarter = [i for i in range(1, 100000) if (i % 9 == 0 and i % 6 == 0 and i % 4 == 0)]  

    quarter = { i: round(i**0.5, 2) for i in range (1,1001)}
    print(quarter)

if __name__ == '__main__':
    run()