def convert(type_pesos,dolar):
    pesos = input('Cuantos pesos '+ type_pesos +' tienes?: ')
    pesos = float(pesos)
    valor_dolar = dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')


menu = """
    Bienvenido al conversor de monedas 💰

    1- Pesos colombianos
    2- Pesos argentinos
    3- Pesos mexicanos

    Elige una opcion:
"""

opcion = input(menu)


if opcion == '1':
    convert('colombianos',3875)
elif opcion == '2':
    convert('argentinos',65)
elif opcion == '3':
    convert('mexicanos',24)
else:
    print('Ingrese una opcion correcta por favor')

