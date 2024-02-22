
Nome_jogador = input("Digite o Nome do jogador: ")
Partidas_Ganhas = int(input("Digite quantas partidas vc ganhou: "))
derrotas = int(input("Digite quantas partidas perdeu: "))



i_Partidas = Partidas_Ganhas - derrotas

def classificar_jogador(i):
    if 0 <= i <= 10:
        return "FERRO"
    
    elif 11 <= i <=20:
        return "BRONZE"
    
    elif 21 <= i <=50:
        return "PRATA"
    
    elif 51 <= i <= 80:
        return "OURO"
    
    elif 81 <= i <= 90:
        return "PLATINA"
    
    elif 91 <= i <=100:
        return "ASCENDENTE"
    
    elif 101 <= i <=200:
        return "IMORTAL"
    
    elif i >= 250:
        return"RADIANTE"
    

if i_Partidas < 0 :
    print("O jogar ", Nome_jogador ,"esta Negativo em  ",i_Partidas," portanto não pode se classificar! ")

else:
    print("O jogar ", Nome_jogador ,"tem o saldo de ",i_Partidas,"Vitória está no nível ", classificar_jogador(i_Partidas))
