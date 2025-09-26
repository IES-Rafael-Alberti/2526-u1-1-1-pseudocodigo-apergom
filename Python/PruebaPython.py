print('Calculadora de salario en bruto')

horas=input('Introduzca el numero de horas: ')
while not horas.isdigit():
    horas=input('Introduzca un numero de horas valido: ')

cuota_hora = input('Introduzca sueldo por hora: ')
while not cuota_hora.isdigit():
    cuota_hora = input('Introduzca un numero valido: ')

horas=int(horas)
cuota_hora=int(cuota_hora)

salario_bruto= horas * cuota_hora

print(f'Usted ganara {salario_bruto}')
