time = int(input('Введите время в секундах:'))

min = time // 60

chas = min // 60

sek = time % 60

min = min % 60

print(f"{chas:02}:{min:02}:{sek:02}")
