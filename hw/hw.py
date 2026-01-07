class Cars: 
    def __init__(self, name, engine_size, max_speed, weight):
        self.name = name
        self.engine_size = engine_size
        self.max_speed = max_speed
        self.weight = weight
    def action1 (self):
        return f'{self.engine_size} start engine!'
    def action2 (self):
        return f'{self.max_speed} maximum acceleration!'
    
honda_civic = Cars('Honda Civic', 1.6, '180 k/h', '1.2 tonns')
honda_accord = Cars('Honda Accord', 2.4, '210 k/h', '1.5 tonns')

print(honda_civic.name)
print(honda_accord.name)
print(honda_accord.action1())
print(honda_accord.action2())        