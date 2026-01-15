#!/usr/bin/python3

def filtering_data(a_dictionary):
    filtro = list(filter(lambda i: i['salary'] > 10000, employees))
    nomes = map(lambda p: p['name'], filtro)
    return list(nomes)


if __name__ == "__main__":
    employees = [
        {'name': 'João', 'age': 35, 'job': 'Manager', 'salary': 15000},
        {'name': 'Maria', 'age': 27, 'job': 'Director', 'salary': 8000},
        {'name': 'Pedro', 'age': 42, 'job': 'Diretor', 'salary': 20000},
        {'name': 'Ana', 'age': 31, 'job': 'Analyst', 'salary': 12000},
        {'name': 'Lucas', 'age': 29, 'job': 'Analyst', 'salary': 9000}
    ]

    high_salary_names = filtering_data(employees)

    print(high_salary_names)
