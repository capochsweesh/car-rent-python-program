def main():


    marca_carros = ["BMW", "Audi", "Fiat", "Ford"]

    valor_dia_BMW = 100
    valor_dia_Audi = 120
    valor_dia_Fiat = 70
    valor_dia_Ford = 80
    valor_km_rodado = 0.60

    marca = input('Digite a marca (BMW, Audi, Fiat ou Ford): \n')

    if marca in marca_carros[0]:
        dias = float(input('Por quantos dias o BMW foi usado? \n'))

        km = float(input('Quantos quilômetros a BMW rodou? \n'))

        print('O valor a ser pago é de R$', dias * valor_dia_BMW + km * valor_km_rodado)
    elif marca in marca_carros[1]:
        dias = float(input('Por quantos dias o Audi foi usado? \n'))
        
        km = float(input('Quantos quilômetros o Audi rodou? \n'))

        print('O valor a ser pago é de R$', dias * valor_dia_Audi + km * valor_km_rodado)
    elif marca in marca_carros[2]:
        dias = float(input('Por quantos dias o Fiat foi usado? \n'))

        km = float(input('Quantos quilômetros o Fiat rodou? \n'))

        print('O valor a ser pago é de R$', dias * valor_dia_Fiat + km * valor_km_rodado)
    elif marca in marca_carros[3]:
        dias = float(input('Por quantos dias o Ford foi usado? \n'))

        km = float(input('Quantos quilômetros o Ford rodou? \n'))

        print('O valor a ser pago é de R$', dias * valor_dia_Ford + km * valor_km_rodado)
    else:
        print('Por favor digite uma das marcas citadas acima.')



if __name__ == "__main__":
    main()
    
