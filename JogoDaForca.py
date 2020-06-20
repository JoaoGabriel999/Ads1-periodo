class cor:
    ROXO = '\033[1;35;48m'
    AZUL = '\033[1;34;48m'
    VERDE = '\033[1;32;48m'
    AMARELO = '\033[1;33;48m'
    VERMELHO = '\033[1;31;48m'
    BRANCO = '\033[1;30;48m'
    FIM = '\033[1;37;0m'
    X = "\33[1;36m"

Letras=[]
Posicoes=[]
vida=7
Jogadordavez=[]
Pontos=0
lPontos=[]

def pontos(Jogadordavez,vez):
    global vida
    global Pontos
    global lPontos
    vida=7
    lPontos[vez]=(Jogadordavez,Pontos+1)
    return lPontos


def erros(Jogadordavez):
    global vida
    vida -= 1
    print('Você errou {}, agora restam apenas {} vida/s'.format(Jogadordavez,vida))
    return vida

def getpalavra(Letras,Posicoes):
    Palavra=''
    Palavra=input(cor.ROXO+'Digite a palavra secreta: '+cor.FIM)
    Posicoes.clear()
    Letras.clear()
    for i in range(len(Palavra)):
        Letras.append(Palavra[i])
        Posicoes.append('_ ')
    return Palavra

def Chute(Letras,Posicoes,rPalavra):
    global vida
    chute=input(cor.VERMELHO+'Insira a letra desejada:'+cor.FIM)
    for i in range(len(Letras)): 
        if Letras[i]==chute and Posicoes[i]=='_ ':
            Posicoes[i]=chute
    if chute not in Letras:
        erros(Jogadordavez)
    ListaChute=''.join(Posicoes)
    print(cor.VERDE+'{}'.format(ListaChute)+cor.FIM)
    return ListaChute

def Partidas():
    global vida
    global Pontos
    global Jogadordavez
    global lPontos
    lJogadores=[]
    lPontos=['','']
    vez=0
    Jogador1=input('Jogador 1, Digite seu nome: ')
    Jogador2=input('Jogador 2, Digite seu nome: ')
    lJogadores.append(Jogador1)
    lJogadores.append(Jogador2)
    for iPartidas in range(0,3):
        print(cor.AZUL+'Inicio de jogo, jogador {} inicia'.format(lJogadores[vez])+cor.FIM)
        rPalavra=getpalavra(Letras,Posicoes)
        if vez==1:
            vez=0
        elif vez==0:
            vez=1  
        while True:
            print(cor.VERMELHO+'Jogador {} escolhe'.format(lJogadores[vez])+cor.FIM)
            Jogadordavez=lJogadores[vez]
            acertos=(Chute(Letras,Posicoes,rPalavra))
            if vida ==0:
                print(cor.VERMELHO+'Puts {}, você morreu'.format((lJogadores[vez])+cor.FIM))
                lPontos[vez]=(Jogadordavez,0)
                if vez==1:
                    vez=0
                    Jogadordavez=lJogadores[vez]
                    pontos(Jogadordavez,vez)
                    print(cor.AMARELO+'Parabens jogador {} você venceu a rodada'.format(lJogadores[vez])+cor.FIM)
                    vez=1
                    Jogadordavez=lJogadores[vez]
                    break
                elif vez==0:
                    vez=1 
                    Jogadordavez=lJogadores[vez]
                    pontos(Jogadordavez,vez)
                    print(cor.AMARELO+'Parabens jogador {} você venceu a rodada'.format(lJogadores[vez])+cor.FIM)
                    vez=0
                    Jogadordavez=lJogadores[vez]
                    break
            if '_ ' not in acertos:
                pontos(Jogadordavez,vez)
                print(cor.AMARELO+'Parabens jogador {} você venceu a rodada'.format(lJogadores[vez])+cor.FIM)
                if vez==1:
                    vez=0
                    Jogadordavez=lJogadores[vez]
                elif vez==0:
                    vez=1                   
                    Jogadordavez=lJogadores[vez]  
                break
        if iPartidas < 2:
            print(cor.VERDE+'Fim do {} round, iniciando o {}.'.format(iPartidas+1,iPartidas+2)+cor.FIM)
        else:
            print(cor.VERMELHO+'=-=-=-=-=-FIM DE JOGO=-=-=-=-=-'+cor.FIM)
            print(lPontos[vez][1]) 
            break
    return Jogadordavez,vez,lPontos
    
print(cor.VERMELHO+'=-=-=-=-=-Jogo da forca=-=-=-=-=-'+cor.FIM)
print(cor.AMARELO+'Jogadores:'+cor.FIM)
Partidas()

#Professor, a validação de jogador vencedor ta dando pau, mas o resto ta top
#Tentei incrementar um valor dentro da tupla mas nao consegui, ai a parte de modularização tbm nao deu boa
#fiz oque consegui :c
