from random import randint
gramy = True


while gramy:

    podana = int(input('Zgadnij liczbe od 1 do 10: '))
    losowa = randint(1, 10)
    if podana == losowa:
        print('Wygrales!')
        gramy = False
    elif podana < losowa:
        print('Za mała')
    else:
        print('Za duża')