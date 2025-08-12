import numpy as np
vector = np.array([1, 2, 3, 4, 5])
print(vector)
print(vector[2])
#####################################################################
vector1 = np.zeros(5)
print(vector1)

vector2 = np.ones(5)# creamos un vectos de unos de tamaño 5
print(vector2)

vector3 = np.arange(1, 10)
print("rango", vector3)

vector4 = np.linspace(1, 10, 5)
print("linspace", vector4)

vector5 = np.random.rand(10)
print("random", vector5)

vector6 = np.random.randint(1, 10, 10)
print("random int", vector6)


"""
los vectores no son como las listas, no tienen un metodo
end() para agregar elementos
o tienen un metodo pop() para eliminar elementos, pero si tienen
metodo reshape() para cambiar la forma del vector, adicionalmente
despues creado no se puede cambiar la forma del vector"""


"""OPERACIONES BASICAS"""

# Suma de todos os elementos
print(np.sum(vector)) # 15

#promedio 

print(np.mean(vector))

#Max, Min

print(np.max(vector))
print(np.min(vector))

import numpy as np
print(np.__version__)