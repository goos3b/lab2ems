cena_kg = float(input('Сколько стоит 1 кг конфет: '))

for skolko_kg in range(1, 11):
    kasse = cena_kg * skolko_kg
    print(f'{skolko_kg} кг -> {kasse:.2f} руб.')