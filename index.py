from tkinter import *
from tkinter import ttk
from PIL import  Image, ImageTk
from dados import*


cor_preta="#444466"
cor_branca="#feffff"
cor_azul="#6f9fbd"
cor_valor="#38576b"
cor_letra="#403d3d"
cor_vermelha="#ef5350"
#funcao trocar pokemon
def trocar_pokemon(i):
    global imagem_pokemon, pokemon_imagem
    
    #trocar cor do fundo frame
    frame_pokemon['bg']=pokemon[i]['tipo'][3]
    
    #tipo de pokemon
    pokemon_nomme['text']=i
    pokemon_nomme['bg']= pokemon[i]['tipo'][3]
    pokemon_tipo['text']=pokemon[i]['tipo'][1]
    pokemon_tipo['bg']= pokemon[i]['tipo'][3]
    pokemon_id['text']=pokemon[i]['tipo'][0]
    pokemon_id['bg']=pokemon[i]['tipo'][3]
    
    
    imagem_pokemon=pokemon[i]['tipo'][2]
    #imagem pokemon

    imagem_pokemon= Image.open(imagem_pokemon)
    imagem_pokemon= imagem_pokemon.resize((238,238))
    imagem_pokemon= ImageTk.PhotoImage(imagem_pokemon)

    pokemon_imagem=Label(frame_pokemon,image=imagem_pokemon,fg=cor_branca,bg=pokemon[i]['tipo'][3])
    pokemon_imagem.place(x=60,y=50)
#sobrepor
    pokemon_tipo.lift()
#status
    pokemon_hp['text']=pokemon[i]['status'][0]
    pokemon_ataque['text']=pokemon[i]['status'][1]
    pokemon_defesa['text']=pokemon[i]['status'][2]
    pokemon_velocidade['text']=pokemon[i]['status'][3]
    pokemon_total['text']=pokemon[i]['status'][4]
    
    pokemon_habilidade['text']=pokemon[i]['habilidades'][0]
    pokemon_habilidade_2['text']=pokemon[i]['habilidades'][1]
    
#janelas
janela=Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=cor_branca)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=272)

style=ttk.Style(janela)
style.theme_use("clam")

#frame
frame_pokemon= Frame(janela, width=550,height=290,relief='flat')
frame_pokemon.grid(row=1,column=0)

pokemon_nomme=Label(frame_pokemon,text='',relief='flat',anchor=CENTER,font=('Fixedsys 20'),fg=cor_branca)
pokemon_nomme.place(x=12,y=15)


pokemon_tipo=Label(frame_pokemon,text='',relief='flat',anchor=CENTER,font=('Ivy 10 bold'),bg=cor_branca,fg=cor_branca)
pokemon_tipo.place(x=12,y=50)

pokemon_id=Label(frame_pokemon,text='',relief='flat',anchor=CENTER,font=('Ivy 10 bold'),bg=cor_branca,fg=cor_branca)
pokemon_id.place(x=12,y=75)


#status
pokemon_status=Label(janela,text='Status',relief='flat',anchor=CENTER,font=('Verdana 20'),bg=cor_branca,fg=cor_preta)
pokemon_status.place(x=15,y=310)
#hp
pokemon_hp=Label(janela,text='HP:300',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=cor_branca,fg=cor_letra)
pokemon_hp.place(x=15,y=360)
#Ataque
pokemon_ataque=Label(janela,text='Ataque:600',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=cor_branca,fg=cor_letra)
pokemon_ataque.place(x=15,y=385)
#defesa
pokemon_defesa=Label(janela,text='Defesa:500',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=cor_branca,fg=cor_letra)
pokemon_defesa.place(x=15,y=410)
#velocidade
pokemon_velocidade=Label(janela,text='Velocidade:300',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=cor_branca,fg=cor_letra)
pokemon_velocidade.place(x=15,y=435)
#total
pokemon_total=Label(janela,text='Total:1.700',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=cor_branca,fg=cor_letra)
pokemon_total.place(x=15,y=460)

#habilidade
pokemon_status=Label(janela,text='Habilidades',relief='flat',anchor=CENTER,font=('Verdana 20'),bg=cor_branca,fg=cor_preta)
pokemon_status.place(x=180,y=310)
#hp
pokemon_habilidade=Label(janela,text='Choque do trovão',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=cor_branca,fg=cor_letra)
pokemon_habilidade.place(x=195,y=360)
#Ataque
pokemon_habilidade_2=Label(janela,text='Cabeçada',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=cor_branca,fg=cor_letra)
pokemon_habilidade_2.place(x=210,y=385)


#botoes pokemon

imagem_pokemon_1= Image.open('img/cabeca-pikachu.png')
imagem_pokemon_1= imagem_pokemon_1.resize((40,40))
imagem_pokemon_1= ImageTk.PhotoImage(imagem_pokemon_1)

butao_pokemon_1=Button(janela,command=lambda:trocar_pokemon('Pikatchu'),image=imagem_pokemon_1,text='Pikatchu',width=150,compound=LEFT,padx=5,relief='raised',font=('Verdana 12'),overrelief=RIDGE,anchor=NW,bg=cor_branca,fg=cor_preta)
butao_pokemon_1.place(x=375,y=10)

imagem_pokemon_2= Image.open('img/cabeca-bulbasaur.png')
imagem_pokemon_2= imagem_pokemon_2.resize((40,40))
imagem_pokemon_2= ImageTk.PhotoImage(imagem_pokemon_2)

butao_pokemon_2=Button(janela,command=lambda:trocar_pokemon('Bulbasaur'),image=imagem_pokemon_2,text='Bulbasaur',width=150,compound=LEFT,padx=5,relief='raised',font=('Verdana 12'),overrelief=RIDGE,anchor=NW,bg=cor_branca,fg=cor_preta)
butao_pokemon_2.place(x=375,y=65)

imagem_pokemon_3= Image.open('img/cabeca-charmander.png')
imagem_pokemon_3= imagem_pokemon_3.resize((40,40))
imagem_pokemon_3= ImageTk.PhotoImage(imagem_pokemon_3)

butao_pokemon_3=Button(janela,command=lambda:trocar_pokemon('Charmander'),image=imagem_pokemon_3,text='Charmander',width=150,compound=LEFT,padx=5,relief='raised',font=('Verdana 12'),overrelief=RIDGE,anchor=NW,bg=cor_branca,fg=cor_preta)
butao_pokemon_3.place(x=375,y=120)

imagem_pokemon_4= Image.open('img/cabeca-dragonite.png')
imagem_pokemon_4= imagem_pokemon_4.resize((40,40))
imagem_pokemon_4= ImageTk.PhotoImage(imagem_pokemon_4)

butao_pokemon_4=Button(janela,command=lambda:trocar_pokemon('Dragonite'),image=imagem_pokemon_4,text='Dragonite',width=150,compound=LEFT,padx=5,relief='raised',font=('Verdana 12'),overrelief=RIDGE,anchor=NW,bg=cor_branca,fg=cor_preta)
butao_pokemon_4.place(x=375,y=175)

imagem_pokemon_5= Image.open('img/cabeca-gengar.png')
imagem_pokemon_5= imagem_pokemon_5.resize((40,40))
imagem_pokemon_5= ImageTk.PhotoImage(imagem_pokemon_5)

butao_pokemon_5=Button(janela,command=lambda:trocar_pokemon('Gengar'),image=imagem_pokemon_5,text='Gengar',width=150,compound=LEFT,padx=5,relief='raised',font=('Verdana 12'),overrelief=RIDGE,anchor=NW,bg=cor_branca,fg=cor_preta)
butao_pokemon_5.place(x=375,y=230)

imagem_pokemon_6= Image.open('img/cabeca-gyarados.png')
imagem_pokemon_6= imagem_pokemon_6.resize((40,40))
imagem_pokemon_6= ImageTk.PhotoImage(imagem_pokemon_6)

butao_pokemon_6=Button(janela,command=lambda:trocar_pokemon('Gyarados'),image=imagem_pokemon_6,text='Gyarados',width=150,compound=LEFT,padx=5,relief='raised',font=('Verdana 12'),overrelief=RIDGE,anchor=NW,bg=cor_branca,fg=cor_preta)
butao_pokemon_6.place(x=375,y=285)

import random

Lista_pokemon=['Dragonite','Gyarados','Charmander','Bulbasaur','Gengar','Pikatchu']
pokemon_escolhido=random.sample(Lista_pokemon,1)

trocar_pokemon(pokemon_escolhido[0])


janela.mainloop()




