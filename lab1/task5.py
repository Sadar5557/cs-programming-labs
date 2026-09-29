distance = float(input('Введите расстояние в километрах'))
rashod = float(input('Введите расход топлива на 100км'))
price = float(input('Введите цену одного литра'))

toplivo = (distance * rashod) / 100

stoimost = toplivo * price

print("Топливо:" , f'{toplivo:.2f} л')
print("Стоимость:" ,f'{stoimost:.2f} руб')
