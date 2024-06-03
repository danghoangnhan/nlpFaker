import random
import os

class MobileGenerator:
    def __init__(self):
        self.data = self.load_data(os.path.join('raw_data', 'mobile.dat'))
    def load_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
        
        records = data.split('\n')
        records.pop()  # Remove the last empty record if it exists
        return records
    
    def select_first_number(self):
        index = random.randint(0, len(self.data) - 1)
        return self.data[index]
    
    def select_numbers(self, num):
        nums = [str(random.randint(0, 9)) for _ in range(num)]
        return ''.join(nums)
    
    def generate(self, area, total_number):
        result = str(area) if area else ''
        result += self.select_first_number()
        result += self.select_numbers(total_number - len(result))
        return result
