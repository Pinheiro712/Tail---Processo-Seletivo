tipos = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fight", "Poison","Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon"]
#Carregando todos os tipos numa lista para montar uma matriz.


#fazendo um indice
Ind_tipo = {tipo: i for i , tipo in enumerate(tipos)}



#seguindo a matriz ficaria linha = atacante e coluna = atingido
#0.5 = Ataque nao foi efetivo
#1 = ataque normal
# 2 = super efetivo
# 0 = ataque nao teve efeito


matriz_ef =[[1,1,1,1,1,1,1,1,1,1,1,0.5,0,1], #normal
[1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5],#fogo,
[1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,],#Water,
[1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5],#Electric,
[1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5],#Grass,
[1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2],#Ice,
[2,1,1,1,1,2,1,0.5,1,0.5,0.5,2,0,1],#Fight,
[1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1],#Poison,
[1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,],#Ground,
[1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1],#Flying,
[1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1],#Psychic,
[1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1],#Bug,
[1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1],#Rock,
[0,1,1,1,1,1,1,1,1,1,2,1,1,2,1],#Ghost,
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]]#Dragon
#matriz com base na imagem


def batalha_pokemon(tipos):
    """
    Função principal que recebe o tipo do ataque e do atingido
    """
    atacante = tipos[0]
    atingido = tipos[1]
    i = Ind_tipo[atacante]
    j = Ind_tipo[atingido]


    #analisa a matriz
    efeito = matriz_ef[i][j]

 
    #Efeitos:
    if efeito == 0:
        return "O ataque não teve efeito."
    
    elif efeito == 0.5:
        return "Não foi muito efetivo..."
    
    elif efeito == 1:
        return "Ataque normal."
    
    elif efeito == 2:
        return "Super efetivo!"
    

