import random

class IDNumberGenerator:
    def __init__(self):
        self.areas = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z', 'I', 'O'
        ]
    
    def select_area_number(self):
        return random.choice(self.areas)
    
    def select_gender(self):
        percentage = random.randint(1, 1000)
        if percentage > 995:
            return 7
        return random.randint(1, 2)
    
    def generate_serial_number(self):
        return [random.randint(0, 9) for _ in range(7)]
    
    def get_area_nums(self, area):
        area_num = self.areas.index(area) + 10
        return [int(x) for x in str(area_num)]
    
    def figure_checksum(self, id_arr):
        weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # Modified to include weights for all digits
        sum_total = sum([a * b for a, b in zip(id_arr, weights)])
        return (10 - (sum_total % 10)) % 10
    
    def generate(self):
        area = self.select_area_number()
        gender = self.select_gender()
        serial = self.generate_serial_number()
        arr = self.get_area_nums(area) + [gender] + serial
        result = [area, str(gender)] + [str(x) for x in serial]
        result.append(str(self.figure_checksum(arr)))
        return ''.join(result)

# Example use of the IDNumberGenerator
generator = IDNumberGenerator()
print(generator.generate())
