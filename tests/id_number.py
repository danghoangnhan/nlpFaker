import sys
sys.path.append("./.")
from src.id_number import IDNumberGenerator
generator =  IDNumberGenerator()
print(generator.generate())