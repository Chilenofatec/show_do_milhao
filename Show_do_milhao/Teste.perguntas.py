# -*- coding: utf-8 -*-
import anydbm
import random

arquivo = anydbm.open('dados' , 'c')
arquivo['P1N1'] = 'Longbottom era o sobrenome de quem, nas séries de livros de Harry Potter?'
arquivo['P1C1'] = 'Neville'
arquivo['P1R2'] = 'Hermione'
arquivo['P1R3'] = 'Snape'
arquivo['P1R4'] = 'Dumbledore'

arquivo['P2N1'] = 'Qual Local que hoje se supõe onde foi o Nascimente de Jesus Cristo?'
arquivo['P2R1'] = 'Igreja da Penha'
arquivo['P2C2'] = 'Basílica da Natividade'
arquivo['P2R3'] = 'Natal'
arquivo['P2R4'] = 'Congo'

arquivo['P3N1'] = 'Göpfritz an der Wild é localizado aonde?'
arquivo['P3R1'] = 'Inglaterra'
arquivo['P3R2'] = 'Emirados Árabes'
arquivo['P3C3'] = 'Áustria'  
arquivo['P3R4'] = 'Brasil'

arquivo['P4N1'] = 'Complete: Eu me remexo muito, Eu me remexo muito, Eu me remexo...'
arquivo['P4C1'] = 'Muito!'
arquivo['P4R2'] = 'Pouco!'
arquivo['P4R3'] = 'Nem sempre!'
arquivo['P4R4'] = 'Constantemente!'

arquivo['P5N2'] = 'Nofollow É:'
arquivo['P5R1'] = 'Ato de Não seguir no Twitter'
arquivo['P5R2'] = 'Programa usado para não ter seguidores no Twitter'
arquivo['P5R3'] = 'Uma expressão para não ser seguido no Twitter'
arquivo['P5C4'] = 'Um atributo HTML'

arquivo['P6N2'] = 'No Campeonato Sul-Americano de futebol Sub-19 de 1964, foi consagrado campeão:'
arquivo['P6R1'] = 'Paraguai'
arquivo['P6C2'] = 'Uruguai'
arquivo['P6R3'] = 'Argélia'
arquivo['P6R4'] = 'Argentina'

arquivo['P7N2'] = 'No Filme “Indiana Jones No templo da perdição”,  as Pedras de Sankara são:'
arquivo['P7R1'] = 'Artefatos Para Abrir um vórtice temporal'
arquivo['P7R2'] = '500KG de cocaína pasteurizada'
arquivo['P7C3'] = 'Pedras místicas dadas pelo deus hindu Shiva'
arquivo['P7R4'] = 'O nome da pistola usada pelo Han Solo'

arquivo['P8N2'] = 'Em Lajes do Pico, nos Açores, encontra-se o povoado de:'
arquivo['P8R1'] = 'Ilha do Manuel'
arquivo['P8R2'] = 'Ilha do Medo'
arquivo['P8C3'] = 'Ribeira do meio'
arquivo['P8R4'] = 'Lajes de Embaixo'

arquivo['P9N2'] = 'No Concurso Miss Mundo 1975, a ganhadora foi:'
arquivo['P9R1'] = 'Um Travesti Maquiado'
arquivo['P9C2'] = 'Wilnelia Merced Cruz'
arquivo['P9R3'] = 'Kaiane Aldorino'
arquivo['P9R4'] = 'Todas ficavam feias em preto-e-branco'

arquivo['P10N3'] = 'Na ciência da computação, o caractere nulo  é um caractere da tabela ASCII que:'
arquivo['P10R1'] = 'Representa o forever alone'
arquivo['P10R2'] = 'Foi o primeiro a ser escrito por Charles Baggage'
arquivo['P10C3'] = 'Representa um espaço vazio'
arquivo['P10R4'] = 'Faz o programa ficar corrompido'


arquivo['P11N3'] = 'Kingdom City:'
arquivo['P11C1'] = 'Uma vila no estado americano de missouri'
arquivo['P11R2'] = 'Uma fase do Sonic'
arquivo['P11R3'] = 'Uma fase do Mário'
arquivo['P11R4'] = 'Um local bonito de se ver'

arquivo['P12N3'] = 'Uma tecnologia de proteção digital para CDs e DVDs É:'
arquivo['P12R1'] = 'K.O.N.F.I.A.N.Ç.A'
arquivo['P12C2'] = 'SecuROM'
arquivo['P12R3'] = 'Fita Crepe'
arquivo['P12R4'] = 'SecuTroll'

arquivo['P13N3'] = 'Um Site que é um MEME:'
arquivo['P13R1'] = 'http://www.zosima.com/'
arquivo['P13R2'] = 'http://www.ufrj.com.org'
arquivo['P13R3'] = 'http://www.trolface.com'
arquivo['P13C4'] = 'http://nyan.cat/'

arquivo['P14N3'] = 'Qual desses animais é vertebrado?'
arquivo['P14R1'] = 'Borboleta'
arquivo['P14R2'] = 'Barata'
arquivo['P14C3'] = 'Jacaré'
arquivo['P14R4'] = 'Minhoca'

arquivo['P15N4'] = 'linha 11 do metro de Moscovo também é referida como:'
arquivo['P15R1'] = 'Трусость и образования'
arquivo['P15R2'] = 'Не инвестировать в возобновляемые'
arquivo['P15R3'] = 'В один прекрасный день мы будем вторглись китайские'
arquivo['P15C4'] = 'Linha Kakhovskaia'

arquivo['P16N4'] = 'O Qutb Minar é o minarete de tijolo mais alto do mundo, exemplo de arquitetura:'
arquivo['P16C1'] = 'Indo-islâmica'
arquivo['P16R2'] = 'De alguém que gostava de empilhar tijolos'
arquivo['P16R3'] = 'Dos primos da áfrica'
arquivo['P16R4'] = 'Cimento Mauá, Melhor não há'

arquivo['P17N4'] = 'Jugular é algo pertecente...'
arquivo['P17C1'] = 'À garganta'
arquivo['P17R2'] = 'Aos pés'
arquivo['P17R3'] = 'Ao peito'
arquivo['P17R4'] = 'Ao vampiro'

arquivo['P18N4'] = 'Que outro nome também pode ser chamado uma farmácia:'
arquivo['P18R1'] = 'Farmacomania'
arquivo['P18R2'] = 'Perfumaria'
arquivo['P18R3'] = 'Remedista'
arquivo['P18C4'] = 'Drogaria'

arquivo['P19N4'] = 'Nos quadrinhos, Rorschach é:'
arquivo['P19R1'] = 'Quem vigia os watchman?'
arquivo['P19R2'] = 'Shang Tsung'
arquivo['P19C3'] = 'Walter Kovacs'
arquivo['P19R4'] = 'Doutor Manhattan'

arquivo['P20N5'] = 'Qual o nome da esposa de kaká, que é pastora da igreja renascer?'
arquivo['P20R1'] = 'Bruxa do 71'
arquivo['P20C2'] = 'Caroline Celico'
arquivo['P20R3'] = 'Gata Boralheira'
arquivo['P20R4'] = 'Gaviã Arqueira'

arquivo['P21N5'] = 'O que significa a expresão “Fogo de palha”?'
arquivo['P21R1'] = 'Fogo Forte'
arquivo['P21C2'] = 'Entusiasmo Passageiro'
arquivo['P21R3'] = 'Fúria repentina'
arquivo['P21R4'] = 'Tristeza Profunda'

arquivo['P22N5'] = ''
arquivo['P22'] = ''
arquivo['P22'] = ''
arquivo['P22'] = ''
arquivo['P22'] = ''

arquivo.close()

#LEITOR DE ENTRADAS (printa no Shell)

##entrada = anydbm.open('dados', 'r')
##for q in range(1 , 21):
##    Q = 'P%i'  %q
##    for j in range (1, 5):
##        J = Q + 'N%i' %j
##        if entrada.has_key(J):
##            print entrada[J]
##        S = Q +'R'+'%i' %j
##        L = Q +'C'+'%i' %j
##        if entrada.has_key(L):
##            print entrada[L]
##            
##        if entrada.has_key(S):
##            print entrada[S]


##entrada.close()
