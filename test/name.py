import sys
sys.path.append('./.')
from src.name import NameGenerator
generator = NameGenerator()
print(generator.generate())