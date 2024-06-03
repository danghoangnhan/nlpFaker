import sys
sys.path.append("./.")
from src.mobile import MobileGenerator
generator =  MobileGenerator()
print(generator.generate(1,total_number=10))