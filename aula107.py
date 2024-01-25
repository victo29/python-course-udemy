# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def equalize_lists(list_s, list_b):
    res = len(list_s) - len(list_b)
    new_list = list_b[:res]
    return new_list


def join_lists(cities, states):
    size_list_cities = len(cities)
    size_list_states = len(states)
    new_list = []
    if size_list_cities > size_list_states:
        cities = equalize_lists(states, cities)
    elif size_list_states > size_list_cities:
        states = equalize_lists(cities,states)
    
    for i in range(size_list_cities):
        tupla = (cities[i], states[i])
        new_list.append(tupla)
    return new_list

states = ['BA', 'SP', 'MG', 'RJ']
cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
print(join_lists(cities,states))