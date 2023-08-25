from random import randint
x = randint(0, 100)
r = 0

while True:
    try:
        y = float(input('Припусти ціле число(0-100): '))
        y = int(y) 
    except ValueError:
        print('Ти ввів не число!!!')
        continue


    if y > x:
        print('А от і ні, менше')

            
    elif y < x:
        print('А от і ні, більше')

    
    else:
        print('Неймовірно! Ти вгадав!')
        r += 1
        print(f'\nТвій рахунок - {r}')
        x = randint(0, 10)

