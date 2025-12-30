# class Hero: 
#     #конструктор класса (self можно называть и по другому)
#     def __init__(self, name, lvl, hp):
#         #атрибуты класса
#         self.hero_name = name
#         self.lvl = lvl
#         self.hero_hp = hp
    
#     def action(self):
#         return f'(self.hero_name) base action!!'
    
# # #Объект/Экземпляр класса 
# kirito = Hero('Ardager', 100, 1000)
# asuna = Hero('Asuna', 99, 999)

# print(kirito.hero_name)
# print(asuna.hero_name)
# print(kirito.action())

class Hero: 
    #конструктор класса (self можно называть и по другому)
    def __init__(self, name, lvl, hp):
        #атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    
    def action(self):
        return f'{self.name} base action!!'
    
# #Объект/Экземпляр класса 
kirito = Hero('Ardager', 100, 1000)
asuna = Hero('Asuna', 99, 999)

print(kirito.name)
print(asuna.name)
print(kirito.action())

#print(type(float))


