
import random

# Considerei numeros inteiros para não bagunçar tanto
def gerador_faturamento():
    vetor = [random.randint(100, 1000) for _ in range(365)]
    
    # Considerando que o Brasil tem 52 finais de semana e 10 feirados nacionais
    # Totaliza-se 62 dias sem faturamento 
    aux_fat = [random.randint(0,365) for _ in range(62)]
    
    # Adicionando os dias sem faturamento ao vetor
    for dia in aux_fat:
        vetor[dia] = 0

    return vetor


def maior_valor(faturamento):
    maior = 0
    for num in faturamento:
        if num != 0:
            if num > maior:
                maior = num
    
    return maior

def menor_valor(faturamento):
    menor = 1000
    for num in faturamento:
        if num != 0:
            if num < menor:
                menor = num

    return menor



def media_faturamento(faturamento):
    total_valor = 0
    total_dias = 0
    media = 0.0

    for dia in faturamento:
        if dia!= 0:
            #total valor recebe o valor do dia e total_dia incrementa +1
            total_valor += dia
            total_dias += 1
    
    # Calcula a media dos dias que teve faturamento
    if total_dias != 0:
        media = total_valor / total_dias
        return media
    
    return media

# Dias de faturamento acima da media
def conta_dia_superior(faturamento, media):
    cont = 0
    for dia in faturamento:
        if dia!= 0 and dia > media:
            cont += 1

    return cont
    

# Resultados Esperados

faturamento = gerador_faturamento()

menor = menor_valor(faturamento)
maior = maior_valor(faturamento)

media = media_faturamento(faturamento)

cont_dias = conta_dia_superior(faturamento, media)


print(f'O menor valor de faturamento foi: {menor}')

print(f'O maior valor de faturamento foi: {maior}')

print(f'A média dos valores de faturamento foi: {media}')

print(f'Existem {cont_dias} dias com faturamento acima da média')