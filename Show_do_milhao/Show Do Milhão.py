# -*- coding: utf-8 -*-

from Tkinter import *
import anydbm
import random

class Janela ():
    def __init__(self, toplevel):
        self.toplevel = toplevel
        
        self.framePrinc = Frame(toplevel, relief = GROOVE)
        self.framePrinc.pack(pady = 199, padx = 199)                                           ##frame principal

        self.label = Label(self.framePrinc, text = 'Show Do Milhão', font = ('Verdana','24','bold'))
        self.label.pack(anchor = N, pady = 10)

        self.framePicture = Frame(self.framePrinc)
        self.framePicture.pack(pady = 10, side = LEFT)

        self.frameBotao = Frame(self.framePrinc)
        self.frameBotao.pack()                   ##frame encima da principal, cada coisa pode ter sua frame, para ficar dividido
        
        self.botao = Button(self.frameBotao, text = 'Cadastro de Novo Jogador', command = self.cadastro, padx = 10, font = ('bold'))
        self.botao.pack(anchor = W)

        self.botao2 = Button(self.frameBotao, text = 'Já sou Cadastrado', padx = 10,command = self.usuarios, font = ('bold'))
        self.botao2.pack(anchor = W)

        self.botao3 = Button(self.frameBotao, text = 'Cadastro de Perguntas', command = self.registaPergunta, font = ('bold'))
        self.botao3.pack(anchor = W)

        self.botao4 = Button(self.frameBotao, text = 'Jogar Com As Minhas Perguntas', command = self.jogarPerguntas, font = ('bold'))
        self.botao4.pack(anchor = W)
        

    def cadastro(self):  #gera a tela de cadastro de usuário
        self.toplevel.destroy()
        raiz = Tk(className = 'Cadastro de Usuário')
        pop = nome(raiz)
        raiz.mainloop()
        
    def usuarios(self):	#Gera a lista de usuários já cadastrados
        self.toplevel.destroy()
        raiz = Tk(className = 'Usuários')
        lista(raiz)
        raiz.mainloop()
        
    def registaPergunta(self): #Exibe o 'Registrador de perguntas'
        self.toplevel.destroy()
        raiz = Tk(className = 'Registrador de Perguntas')
        PergCadastro(raiz)
        raiz.mainloop()

    def jogarPerguntas(self):	#Inicia o jogo com as perguntas que voce cadastrou
        self.toplevel.destroy()
        raiz = Tk(className = 'Show Do Milhão')
        jogo(raiz, '100')
        raiz.mainloop()



        
class nome ():	#Realiza o Cadrasto do usuário
    def __init__(self, toplevel):
        self.toplevel = toplevel
        
        self.framePrinc = Frame(toplevel)
        self.framePrinc.pack()

        self.frame1 = Label(self.framePrinc, text = 'Cadastro de Usuário', font = ('Ubuntu', '12','bold'))
        self.frame1.pack()
        self.frame1.focus()
        
        self.frame2 = Frame(self.framePrinc)
        self.frame2.pack(pady = 10)

        self.nomeCampo = Label(self.frame2, text = 'Nome: ',font = ('Verdana','12','bold'))
        self.nomeCampo.pack(side = LEFT)

        self.frameBotao = Frame(self.framePrinc)
        self.frameBotao.pack(pady = 20)

        self.nome = Entry(self.frame2)
        self.nome.pack(side = LEFT)
        self.nome.focus()

        self.botao = Button(self.frameBotao, text = 'Enviar')
        self.botao.pack()
        self.botao.bind("<Button-1>", self.botaoClick)

    def botaoClick(self, evento):
        usuario = self.nome.get()
        usuario = usuario.encode('utf - 8')#iso-8859-1 (transforma a string de unicode para utf8)
        
        arquivo = anydbm.open('misc', 'c')
        arquivo[usuario] = usuario
        arquivo['current'] = usuario #grava  o usuário como como corrente
        arquivo.close()
        self.toplevel.destroy()
        raiz = Tk(className = 'Show Do Milhão')
        jogo(raiz, '0')
        raiz.mainloop()




        
class lista():		#Exibe uma lista com os jogadores já existentes apartir de um banco de dados
    def __init__(self, toplevel):
        self.toplevel = toplevel

        self.frame1 = Frame(toplevel)
        self.frame1.pack(padx = 80, pady = 20)

        self.frameError = Frame(toplevel)
        self.frameError.pack(pady = 50, padx = 80)

        self.frameRadio = Frame(self.frame1)
        self.frameRadio.pack(side = BOTTOM)

        try:
            self.valorRadio = IntVar()
            arquivo = anydbm.open('misc', 'r')
            chaves = arquivo.keys()
            tamanho = len(chaves)
            if len(chaves) == 1:
                self.label = Label(self.frameError, text = 'ERRO', font = ('Ubuntu','24','bold'))
                self.label.pack(side = TOP)
            
                self.button = Button(self.frameError, text = 'Não Existem Usuários Cadastrados',font = ('Ubuntu', '12'), command = self.Back)
                self.button.pack(side = BOTTOM)
            
            for p in range(0, tamanho):
                k = chaves[p]
                l = arquivo[k]
                if k == 'nivel' or k == 'money' or k == 'current':
                    pass
                else:
                    self.radio = Radiobutton(self.frameRadio, text = l , value = p, variable = self.valorRadio, command = self.vc, indicator = FALSE)
                    self.radio.pack(anchor = W)
            self.valorRadio.set(0)
            arquivo.close()
        except:						#Lida com o fato de não existir Usuários, criando uma nova tela
            self.label = Label(self.frameError, text = 'ERRO', font = ('Ubuntu','24','bold'))
            self.label.pack(side = TOP)
            
            self.button = Button(self.frameError, text = 'Não Existem Usuários Cadastrados',font = ('Ubuntu', '12'), command = self.Back)
            self.button.pack(side = BOTTOM)
            
    def vc (self):
        self.toplevel.destroy()
        
        current = self.valorRadio.get()
        
        arquivo = anydbm.open('misc', 'c')
        chaves = arquivo.keys()  #Armazena as chaves do banco de dados, sempre em ordem
        usuario = chaves[current]
        arquivo['current'] = usuario
        arquivo.close()
                
        raiz = Tk(className = 'Show Do Milhão')
        jogo(raiz, '0')
        raiz.mainloop()
        
    def Back(self):  # Acão do botao do Erro, volta para a tela inicial
        self.toplevel.destroy()
        raiz  = Tk(className = 'Painel Principal')
        Janela(raiz)
        raiz.mainloop()
        



        
class jogo ():  #Inicia o a tela com perguntas e várias respostas (Tela de Jogo)
    def __init__(self, toplevel, nivel):
        
        self.toplevel = toplevel
        self.nivel = nivel

        self.frameError = Frame(toplevel)
        self.frameError.pack(pady = 50, padx = 80)
        
        if nivel =='100' or nivel == '101' or nivel == '102' or nivel == '103' or nivel == '104' or nivel == '105':
            n = '1'
            arquivo = anydbm.open('misc', 'c')    #'if' para o modo de jogo 'Perguntas do usuario'
            arquivo['nivel'] = nivel
            usuario = 'Teste'
            arquivo.close()
            
        if nivel == '0':
            n = '0'
            nivel = '1'
            arquivo = anydbm.open('misc', 'w')
            arquivo['nivel'] = nivel
            usuario = arquivo['current']
            arquivo.close()
                             
        if nivel != '0'and nivel !='100'and nivel != '101' and nivel != '102' and nivel != '103' and nivel != '104' and nivel != '105':
            n = '0'
            arquivo = anydbm.open('misc', 'c')
            arquivo['nivel'] = nivel
            usuario = arquivo['current']
            arquivo.close()
        
        self.framePrinc = Frame(toplevel)
        self.framePrinc.pack(pady = 40, padx = 40)

        self.labelMoney = Label(self.framePrinc, text = 'MONEY')
        self.labelMoney.pack(side = RIGHT, anchor = N)
        
        self.labelPlayer = Label(self.framePrinc, text = usuario)
        self.labelPlayer.pack(side = RIGHT,anchor = NW)
        
        self.frameAjuste = Frame(self.framePrinc)
        self.frameAjuste.pack(side = BOTTOM, pady = 20)

        
        self.perg1(nivel, n)
    def perg1 (self, nivel, n):
        #Escolhe numeros aleatorios para perguntas do mesmo nivel
        if nivel == '1':
            D = random.randint(1, 4)
        if nivel == '2':
            D = random.randint(5, 9)
        if nivel == '3':
            D = random.randint(10, 14)
        if nivel == '4':
            D = random.randint(15, 19)
        if nivel == '5':
            D = random.randint(20, 21)
            
        if n == '0':
            P = anydbm.open('dados' , 'r')

        
        if n == '1':   #Abre e trabalha com as perguntas cadastradas pelo usuario
            try:
                P = anydbm.open('dados_usuario' , 'r')
                l1 = []
                l2 = []
                l3 = []
                l4 = []
                l5 = []
                chaves = P.keys()
                tamanho = len(chaves)
                tamanho = (tamanho/5)+1
                for i in range(0, tamanho):
                    
                    A = 'P%iN' %i
                    B = A + '1'
                    
                    if B in chaves:
                        l1.append(B)
                        P1 = len(l1)
                        
                    C = A + '2'
                    
                    if C in chaves:                
                        l2.append(C)
                        P2 = len(l2)
                        
                    D = A + '3'
                    
                    if D in chaves:             
                        l3.append(D)
                        P3 = len(l3)
                        
                    E = A + '4'
                    
                    if E in chaves:                
                        l4.append(E)
                        P4 = len(l4)
                        
                    F = A + '5'
                    
                    if F in chaves:
                        l5.append(F)
                        P5 = len(l5)
                #Escolhe numeros aleatorios para perguntas do mesmo nivel, modo perguntas do jogador
                if nivel == '100':
                    nivel = '1'
                    D = random.randint(0, P1)
                if nivel == '101':
                    nivel = '2'
                    D = random.randint(P1-1, P2)
                if nivel == '102':
                    nivel == '3'
                    D = random.randint(P2-1, P3)
                if nivel == '103':
                    nivel = '4'
                    D = random.randint(P3-1, P4)
                if nivel == '104':
                    nivel = '5'
                    D = random.randint(P4-1, P5)
                    
            except:     #lida com o erro de não existirem perguntas cadastradas
                self.labelPlayer.destroy()
                self.labelMoney.destroy()
                self.frameAjuste.destroy()
                
                self.label = Label(self.frameError, text = 'ERRO', font = ('Ubuntu','24','bold'))
                self.label.pack(side = TOP)

                self.label = Label(self.frameError, text = 'Não Existem Perguntas Cadastrados', font = ('Ubuntu','16','bold'))
                self.label.pack(side = TOP)
                
                self.button = Button(self.frameError, text = 'OK',font = ('Ubuntu', '12'), command = self.naoExistePerguntas)
                self.button.pack(side = BOTTOM)
                
                
       	#Monta as perguntas, tanto do usuário, quanto as do banco principal
	
        Q = 'P%i' %D
        
        J = Q + 'N' + nivel
        
        if P.has_key(J):
            self.label = Label(self.framePrinc, text = P[J], font = ('Ubuntu', '12'))
            self.label.pack(anchor = W)
        self.valorRadio = IntVar()
        for j in range (1, 5):
            S = Q+'R'+'%i' %j      
            L = Q+'C'+'%i' %j
            if P.has_key(L): #Permite que só um radio button gere a pergunta certa
                self.quest = Radiobutton(self.framePrinc, text = P[L],value = j, variable = self.valorRadio, command = self.RespC)
                self.quest.pack(padx = 30, anchor  = W)
            if P.has_key(S):
                self.quest = Radiobutton(self.framePrinc, text = P[S],value = j, variable = self.valorRadio, command = self.RespE)
                self.quest.pack(padx = 30, anchor = W)
        P.close()
                
    def RespC(self): #'Aplaude' o jogador por ter acertado
        self.toplevel.destroy()
        raiz = Tk(className = 'Ceeeeerta Resposta')
        Certa(raiz)
        raiz.mainloop()
        
    def RespE(self):	#faz o jogador perder o jogo
        self.toplevel.destroy()
        raiz = Tk(className = 'Resposta Eeeeerrada')
        Errada(raiz)
        raiz.mainloop()
        
    def naoExistePerguntas(self): #Lida com o erro de não existirem perguntas cadastradas, volta ao Painel principal
        self.toplevel.destroy()
        raiz  = Tk(className = 'Painel Principal')
        Janela(raiz)
        raiz.mainloop()
                    
        



class Certa(): 	#parabeniza o usuário por ter acertado
    def __init__(self, toplevel):
        self.toplevel = toplevel
        
        self.frame1 = Frame(toplevel)
        self.frame1.pack(pady = 40, padx = 40)

        self.label = Label(self.frame1, text = 'Você Acertou', font = ('Ubuntu','24','bold'))
        self.label.pack(pady = 40, padx = 40)

        self.botao = Button(self.frame1, text = 'Para Próxima Pergunta', command = self.continuar)
        self.botao.pack()
        
    def continuar(self): #Sobe um nível de dificuldade ou faz o jogador ganhar o premio
        arquivo = anydbm.open('misc', 'w')
        nivel = arquivo['nivel']
    
        if nivel == '5' or nivel == '105' or nivel == '104':
            self.toplevel.destroy()
            raiz = Tk(className = '100.000.000,000')
            ganhou(raiz)
            raiz.mainloop()
            
        if nivel == str(nivel) or nivel == '100':
            nivel = int(nivel)
            nivel = nivel+1
            nivel = str(nivel)
            arquivo['nivel'] = nivel
            
        arquivo.close()
        
        self.toplevel.destroy()
        raiz = Tk(className = 'Show Do Milhão')
        jogo(raiz, nivel)
        raiz.mainloop()




        
class Errada():  #faz o jogador perder o jogo
    def __init__(self, toplevel):
        self.toplevel = toplevel
        
        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        self.label = Label(self.frame1, text = 'Você Perdeu', font = ('Ubuntu','24','bold'))
        self.label.pack()

        self.botao = Button(self.frame1, text = 'Nao vai receber Nada')
        self.botao.pack()

        self.button1 = Button(self.frame1, text = 'recomeçar', command = self.denovo)
        self.button1.pack()
        
    def denovo(self):
        self.toplevel.destroy()
        
        arquivo = anydbm.open('misc', 'r')
        
        if arquivo['nivel'] == '100' or arquivo['nivel'] == '101' or arquivo['nivel'] == '102' or arquivo['nivel'] == '103' or arquivo['nivel'] == '104' or arquivo['nivel'] == '105':
            raiz = Tk(className = 'Show Do Milhão')
            jogo(raiz, '100')
            raiz.mainloop()
            arquivo.close()
        else:
            raiz = Tk(className = 'Show Do Milhão')
            jogo(raiz, '0')
            raiz.mainloop()






class ganhou(): #Janela De Premio
    def __init__(self, toplevel):
        self.toplevel = toplevel

        self.frameP = Frame(toplevel)
        self.frameP.pack(padx = 199, pady = 199)

        self.label1 = Label(self.frameP, text = '1.000.000,00', font = ('Ubuntu','24','bold'))
        self.label1.pack()

        self.label2 = Label(self.frameP, text = 'É a quantia que você LEVA!')
        self.label2.pack()

        self.label3 = Label(self.frameP, text = 'Parabéns!')
        self.label3.pack()

        self.button1 = Button(self.frameP, text = 'recomeçar', command = self.denovo)
        self.button1.pack(side = LEFT)

        self.button2 = Button(self.frameP, text = 'Pontuação Geral', command = self.score) #ainda não implementado
        self.button2.pack(side = LEFT)

        self.button3 = Button(self.frameP, text = 'Sair', command = self.quit)
        self.button3.pack(side = LEFT)
        
    def score(self): #ainda não implementado
        pass
    
    def denovo(self): #volta ao painel inicial
        self.toplevel.destroy()
        raiz = Tk(className = 'Show Do Milhão')
        Janela(raiz)
        raiz.mainloop()
        
    def quit(self):
        self.toplevel.destroy()




        
class PergCadastro(): #Realiza o cadastro de perguntas do jogador
    
    def __init__(self, toplevel):

        self.toplevel = toplevel
        
        self.framePrinc = (toplevel)

        self.framePerg = Frame(self.framePrinc)
        self.framePerg.pack(padx = 10, pady = 10)

        self.labelPerg = Label(self.framePerg, text = 'Pergunta')
        self.labelPerg.pack(side = LEFT)

        self.EntradaPerg = Entry(self.framePerg)
        self.EntradaPerg.pack(side = LEFT)
        self.EntradaPerg.focus()

        self.frameList = Frame(self.framePrinc)
        self.frameList.pack(side = RIGHT)
        self.frameList.scrollarea = (10, 10, 10, 10)
        
        self.valorRadio = IntVar()
        
        for i in range (1, 5):
            
            self.frameEntrada = Frame(self.framePrinc)
            self.frameEntrada.pack()
            
            self.labelEntrada = Label(self.frameEntrada, text = 'Resposta %i'%i)
            self.labelEntrada.pack(side = LEFT, anchor = SW)
            
            if i == 1:
                self.Entrada1 = Entry(self.frameEntrada)
                self.Entrada1.pack(side = LEFT, anchor = W)
                
                self.radioButton1 = Radiobutton(self.frameEntrada, value = 1, variable = self.valorRadio)#, command = self.Registro)
                self.radioButton1.pack(side = LEFT)

                self.labelNivel = Label(self.frameList, text = 'Nível')
                self.labelNivel.pack(pady = 10)

                self.lista = Listbox(self.frameList, selectmode = SINGLE, width = 2, height = 6)
                self.lista.pack(pady = 10)
                self.lista.insert(1, 1)
                self.lista.insert(2, 2)
                self.lista.insert(3, 3)
                self.lista.insert(4, 4)
                self.lista.insert(5, 5)
                
            if i == 2:
                self.Entrada2 = Entry(self.frameEntrada)
                self.Entrada2.pack(side = LEFT, anchor = W)
                
                self.radioButton2 = Radiobutton(self.frameEntrada, value = 2, variable = self.valorRadio)
                self.radioButton2.pack(side = LEFT)
            if i == 3:
                self.Entrada3 = Entry(self.frameEntrada)
                self.Entrada3.pack(side = LEFT, anchor = W)
                
                self.radioButton3 = Radiobutton(self.frameEntrada, value = 3, variable = self.valorRadio)
                self.radioButton3.pack(side = LEFT)
            if i == 4:
                self.Entrada4 = Entry(self.frameEntrada)
                self.Entrada4.pack(side = LEFT, anchor = W)
                
                self.radioButton4 = Radiobutton(self.frameEntrada, value = 4, variable = self.valorRadio)
                self.radioButton4.pack(side = LEFT)

        self.valorRadio.set(1)

        self.labelExplicativa = Label(self.framePrinc, text = 'Marque Com a bolinha a opção certa')
        self.labelExplicativa.pack()
            
        self.frameButton = Frame(self.framePrinc)
        self.frameButton.pack(anchor = S)

        self.buttonEnviar = Button(self.frameButton, text = 'Enviar', command = self.Registro)
        self.buttonEnviar.pack(side = LEFT)

        self.buttonVoltar = Button(self.frameButton, text = 'Voltar', command = self.Voltar)
        self.buttonVoltar.pack(side = LEFT)

    def Registro(self): #pega as respostas e grava no banco de dados 'dados_usuario'
        Perg = self.EntradaPerg.get()
        a = self.valorRadio.get()
        resp1 = self.Entrada1.get()
        resp2 = self.Entrada2.get()
        resp3 = self.Entrada3.get()
        resp4 = self.Entrada4.get()
        nivel =  self.lista.curselection()
        try:
            H = nivel[0]
            H = int(H)
            H += 1
            H = str(H)
        except:
            self.preencha(1)
        if resp1 != '':
            if resp2 != '':
                if resp3 != '':
                    if resp4 !='':
                        if Perg != '':
                            arquivo = anydbm.open('dados_usuario','c') #aqui sao gravadas as perguntas do jogador
                            
                            tam = len(arquivo.keys())
                            tam = tam/5                      
                            G = 'P%i'%tam
                            Q = 'P%iN'%tam + H
                            arquivo[Q] = Perg
                            if a == 1:
                                arquivo[G + 'C1'] = resp1
                                arquivo[G + 'R2'] = resp2
                                arquivo[G + 'R3'] = resp3
                                arquivo[G + 'R4'] = resp4
                            if a == 2:
                                arquivo[G + 'R1'] = resp1
                                arquivo[G + 'C2'] = resp2
                                arquivo[G + 'R3'] = resp3
                                arquivo[G + 'R4'] = resp4
                            if a == 3:
                                arquivo[G + 'R1'] = resp1
                                arquivo[G + 'R2'] = resp2
                                arquivo[G + 'C3'] = resp3
                                arquivo[G + 'R4'] = resp4
                            if a == 4:
                                arquivo[G + 'R1'] = resp1
                                arquivo[G + 'R2'] = resp2
                                arquivo[G + 'R3'] = resp3
                                arquivo[G + 'C4'] = resp4
                                
                            arquivo.close()

                            self.buttonEnviar.destroy()

                            self.buttonVoltar.destroy()

                            self.label2 = Label(self.frameButton, text = 'Deseja Cadastrar Mais Perguntas')
                            self.label2.pack()

                            self.button = Button(self.frameButton, text = 'Sim', command = self.denovo)
                            self.button.pack(side = LEFT)

                            self.button = Button(self.frameButton, text = 'Não', command = self.Voltar)
                            self.button.pack(side = LEFT)

        if nivel[0] == '0' or resp1 == '' or resp2 == '' or resp3 == '' or resp4 == '' or Perg == '':
            self.preencha(0)
            
    def denovo(self): #permite cadastrar mais uma pergunta
        self.toplevel.destroy()
        raiz = Tk(className = 'cadrastro')
        PergCadastro(raiz)
        raiz.mainloop()

    def Voltar(self): #Volta ao painel principal
        self.toplevel.destroy()
        raiz  = Tk(className = 'Painel Principal')
        Janela(raiz)
        raiz.mainloop()

    def preencha(self, n): #Se algum campo estiver em branco, avisa o jogador
        self.toplevel2 = Tk(className = 'Inválido')
            
        self.container = Frame(self.toplevel)
        self.container.pack()

        if n == 0:
            self.outraLabel = Label(self.container, text = 'Preencha Todos Os Campos')
            self.outraLabel.pack(padx = 50, pady = 50)
            self.outraLabel.focus()
            
        if n == 1:
            self.outraLabel1 = Label(self.container, text = 'Preencha com um Nível')
            self.outraLabel1.pack(padx = 50, pady = 50)
            self.outraLabel1.focus()
            
        self.botao = Button(self.container, text = 'OK', command = self.destroy)
        self.botao.pack()
        
    def destroy(self):
        self.toplevel2.destroy()

        
raiz  = Tk(className = 'Painel Principal')
janus = Janela(raiz)
raiz.mainloop()
