try:
    nome = input('Digite seu nome: \n')
    altura = float(input('Digite sua altura: \n'))
    peso = float(input('Digite seu peso: \n'))
    
    if altura <= 0 or peso <= 0:
        raise ValueError('Altura e peso devem ser maiores que zero. \n')
    
    imc = peso / (altura * altura) #Calcula o IMC

    #Informa o IMC e o classifica
    if imc < 16:
        print(f'{nome} você esta com Peso Muito Abaixo do Normal seu IMC é {imc:.2f}, Procure um médico. \n')

    elif 16 < imc <= 18.5:
        print(f'{nome} você esta com Peso Abaixo do Normal - seu IMC é {imc:.2f}, Procure um médico. \n')

    elif 18.5 < imc <= 25:
        print(f'{nome} você esta com Peso Normal - seu IMC é {imc:.2f}, Que bom que você está com o peso normal. \n')

    elif 25 < imc <= 30:
        print(f'{nome} você esta Sobrepeso - seu IMC é {imc:.2f}, Uma pré-obesidade. \n')

    elif 30 < imc <= 35:
        print(f'{nome} você esta com Obesidade grau I - seu IMC é {imc:.2f}, Procure um nutricionista e/ou endocrinologista. \n')

    elif 35 < imc < 40:
        print(f'{nome} você esta com Obesidade grau II - seu IMC é {imc:.2f}, Procure um nutricionista e/ou endocrinologista. \n')

    elif imc > 40:
        print(f'{nome} você esta com Obesidade grau III - seu IMC é {imc:.2f}, Procure um nutricionista e/ou endocrinologista. \n')

except ValueError as e:
    if str(e) == "could not convert string to float: 'altura'":
        print("A altura deve ser um número válido. Por favor, insira um valor numérico maior que 0 para a altura.") #traduzir o erro em pt-BR
    elif str(e) == "could not convert string to float: 'peso'":
        print("O peso deve ser um número válido. Por favor, insira um valor numérico maior que 0 para o peso.") #traduzir o erro em pt-BR
    else:
        print(f"Erro: {str(e)}. Por favor, insira valores válidos para altura e peso.") #traduzir o erro em pt-BR