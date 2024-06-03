import random
import pandas as pd

class AddressGenerator:
    def __init__(self):
        self.data = pd.read_csv('raw_data/address.csv', encoding='utf-16le')
        self.data[['all_types', 'addr_type', 'lane', 'alley', 'num', 'sub', 'floor', 'above_below', 'follow']] = self.data['Condition'].apply(self.parse_conditions).apply(pd.Series)
        
    
    def parse_conditions(self, conditions):
        # Initialize default types
        all_types = False
        addr_type = ''
        if '單全' in conditions:
            all_types = True
            addr_type = 'o'
        elif '雙全' in conditions:
            all_types = True
            addr_type = 'e'
        elif '連全' in conditions:
            all_types = True
            addr_type = 'c'
        elif '全' in conditions:
            all_types = True
        elif '單' in conditions:
            addr_type = 'o'
        elif '雙' in conditions:
            addr_type = 'e'
        elif '連' in conditions:
            addr_type = 'c'

        conditions = conditions.replace(' ', '').replace('全', '').replace('　', '').replace('連', '').replace('單全', '').replace('雙全', '').replace('雙', '').replace('單', '')
        conditions = conditions.split('至')[0] if '至' in conditions else conditions
        

        parts = conditions.split('巷')
        lane = int(parts[0]) if len(parts) > 1 else 0
        conditions = parts[1] if len(parts) > 1 else conditions
            
        parts = conditions.split('弄')
        alley = int(parts[0]) if len(parts) > 1 else 0
        conditions = parts[1] if len(parts) > 1 else conditions
        
        if '以上' in conditions:
                    above_below = 'g'
                    conditions = conditions.replace('以上', '')
        
        if '以下' in conditions:
            above_below = 'l'
            conditions = conditions.replace('以下', '')
        print(conditions)
        if '號' in conditions:
            parts = conditions.split('號')
            num = int(parts[0]) if len(parts) > 1 else 0
            conditions = parts[1] if len(parts) > 1 else conditions
            if '之' in conditions:
                parts = conditions.split('之')
                sub = int(parts[0]) if len(parts) > 1 else 0
                conditions = parts[1] if len(parts) > 1 else conditions

        parts = conditions.split('樓')
        floor = int(parts[0]) if len(parts) > 1 else 0
        conditions = parts[1] if len(parts) > 1 else conditions
            
        above_below = None
        
            
        follow = '及附號' in conditions or '含附號' in conditions
        conditions = conditions.replace('及附號', '').replace('含附號', '')
        num = sub = 0
        


        return all_types, addr_type, lane, alley, num, sub, floor, above_below, follow
        
    def select_road(self):
        return random.choice(self.addr_data)
    
    def select_numbers(self, min_val, max_val):
        return random.randint(min_val, max_val)
    
    def select_floor(self):
        floor = self.select_numbers(1, 24)
        return f'{floor}樓' if floor > 1 else ''
    
    def select_address(self, road):
        addr = [road['city'], road['dist'], road['road']]
        if not road['conditions']:
            addr.append(f'{self.select_numbers(1, 500)}號')
            addr.append(self.select_floor())
            return ''.join(addr)
        
        if road['conditions'][0]['lane']:
            addr.append(f"{road['conditions'][0]['lane']}巷")
        
        if road['conditions'][0]['alley']:
            addr.append(f"{road['conditions'][0]['alley']}弄")
        
        if road['conditions'][0]['sub']:
            addr.append(f"{self.select_numbers(1, 500)}之{self.select_numbers(1, 3)}號")
        else:
            addr.append(f"{self.select_numbers(1, 500)}號")
        
        addr.append(self.select_floor())
        return ''.join(addr)
    
    def generate(self):
        road = self.select_road()
        return self.select_address(road)
