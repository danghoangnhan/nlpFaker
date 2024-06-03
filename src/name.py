import os
import random

class NameGenerator:
    correction_value = 2

    def __init__(self):
        self.fn_data = self.load_data(os.path.join( 'raw_data', 'firstname.dat'))
        self.ln_data = self.load_data(os.path.join('raw_data', 'lastname.dat'))

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = file.read()
        
        meta = {
            'maxWeight': 0,
            'scaledWeight': 0,
        }
        
        records = data.strip().split('\n')
        new_records = []
        for line in records:
            parts = line.split(' ')
            weight = int(parts[1])
            if meta['maxWeight'] < weight:
                meta['maxWeight'] = weight

            new_records.append({
                't': parts[0],
                'w': weight,
            })
        
        meta['scaledWeight'] = round(meta['maxWeight'] * self.correction_value)

        return {
            'meta': meta,
            'records': new_records,
        }

    def select_name(self, data):
        index = random.randint(0, len(data['records']) - 1)
        weight = data['records'][index]['w']
        chance = random.randint(1, data['meta']['scaledWeight'] - 1)

        if chance <= weight:
            return data['records'][index]['t']

        return self.select_name(data)

    def select_first_name(self):
        return self.select_name(self.fn_data)

    def select_last_name(self):
        return self.select_name(self.ln_data)

    def generate(self):
        first_name_seed = random.randint(1, 100)
        first_name = []

        if first_name_seed <= 95:
            for i in range(2):
                first_name.append(self.select_first_name())
        else:
            first_name.append(self.select_first_name())

        return self.select_last_name() + ''.join(first_name)
