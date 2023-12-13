horario = input("Digite as horas: ")

try:
    horario = int(horario)
    
    bom_dia = horario >= 0 and horario <= 11
    boa_tarde = horario >=12 and horario <= 17
    boa_noite = horario >=18 and horario <= 23

    if bom_dia:
        print("Bom dia")
    elif boa_tarde:
        print("Boa tarde")
    elif boa_noite:
        print("Boa noite")

except:
    print("Por favor digite apenas números inteiros")



