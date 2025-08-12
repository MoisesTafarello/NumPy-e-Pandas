import os
import numpy as np
os.system('cls')
array4d = np.random.randint(0, 100, (1, 3, 3, 3))

for i, bloco in enumerate(array4d):
    print(f"Bloco {i}:")
    print(bloco)
    print("----")

print("Média:", np.mean(array4d))
print("Mediana:", np.median(array4d))
print("Desvio padrão:", np.std(array4d))