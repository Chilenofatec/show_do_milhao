# -*- coding: utf-8 -*-
from Tkinter import *
import pickle
import anydbm

class PergCadastro():

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

    def Voltar(self):
        self.toplevel.destroy()

    def Registro(self):
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
            print 'Preencha Com um Nível'
            self.preencha(1)
        if resp1 != '':
            if resp2 != '':
                if resp3 != '':
                    if resp4 !='':
                        if Perg != '':
                            arquivo = anydbm.open('dados_usuario','c')
                            
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

                            self.button = Button(self.frameButton, text = 'Não', command = self.Voltar)#!!!!#
                            self.button.pack(side = LEFT)
                            
##        m = 0
##        n = 0
##        o = 0
##        p = 0
##        q = 0
##        r = 0
        if nivel[0] == '0' or resp1 == '' or resp2 == '' or resp3 == '' or resp4 == '' or Perg == '':
            self.preencha(0)
            
##        if resp1 == '':
##            n = 3
##        if resp2 == '':
##            o = 9
##        if resp3 == '':
##            p = 10
##        if resp4 == '':
##            q = 16
##        if Perg == '':
##            r = 32

##        S = m+n+o+p+q+r
##
##        if S != 0:
##            self.preencha(S)
##            print S
            

    def denovo(self):
        self.toplevel.destroy()
        raiz = Tk(className = 'cadrastro')
        PergCadastro(raiz)
        raiz.mainloop()

    def preencha(self, n):
        self.toplevel = Tk(className = 'Inválido')
            
        self.container = Frame(self.toplevel)
        self.container.pack()

        if n == 0:
            self.outraLabel = Label(self.container, text = 'Preencha Todos Os Campos')
            self.outraLabel.pack(padx = 50, pady = 50)
            self.outraLabel.focus()
        if n == 1:
            self.outraLabel1 = Label(self.container, text = 'Preencha com um Nível')
            self.outraLabel1.pack()
            self.outraLabel1.focus()

##        if n == 1:
##            self.outraLabel1 = Label(self.container, text = 'Preencha com um Nível')
##            self.outraLabel1.pack()
##        if n == 3:
##            self.outraLabel2 = Label(self.container, text = 'Preencha com Uma Resposta 1')
##            self.outraLabel2.pack()
##        if n == 9:
##            self.outraLabel3 = Label(self.container, text = 'Preencha com Uma Resposta 2')
##            self.outraLabel3.pack()
##        if n == 10:
##            self.outraLabel4 = Label(self.container, text = 'Preencha com Uma Resposta 3')
##            self.outraLabel4.pack()
##        if n == 16:
##            self.outraLabel5 = Label(self.container, text = 'Preencha com Uma Resposta 4')
##            self.outraLabel5.pack()
##        if n == 32:
##            self.outraLabel6 = Label(self.container, text = 'Preencha com Uma Pergunta')
##            self.outraLabel6.pack()
##        if n == 4:
##            self.outraLabel1 = Label(self.container, text = 'Preencha com um Nível')
##            self.outraLabel1.pack()
##            
##            self.outraLabel2 = Label(self.container, text = 'Preencha com Uma Resposta 1')
##            self.outraLabel2.pack()
##        if n == 12:
##            self.outraLabel2 = Label(self.container, text = 'Preencha com Uma Resposta 1')
##            self.outraLabel2.pack()
##
##            self.outraLabel3 = Label(self.container, text = 'Preencha com Uma Resposta 2')
##            self.outraLabel3.pack()
##        if n == 19:
##            self.outraLabel3 = Label(self.container, text = 'Preencha com Uma Resposta 2')
##            self.outraLabel3.pack()
##
##            self.outraLabel4 = Label(self.container, text = 'Preencha com Uma Resposta 3')
##            self.outraLabel4.pack()
            
        self.botao = Button(self.container, text = 'OK', command = self.destroy)
        self.botao.pack()
        
    def destroy(self):
        self.toplevel.destroy()
            
            
        
    
raiz = Tk(className = 'cadrastro')
PergCadastro(raiz)
raiz.mainloop()
