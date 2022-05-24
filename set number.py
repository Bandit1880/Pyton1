price = float(input('Ввести цену -'))
fuel = float(input('Ввести расход -'))
r = float(input('Ввести (км) - '))
total = fuel / 100 * price * r *2
print('Summa =', total, 'UAH')