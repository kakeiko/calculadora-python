from tkinter import *
from tkinter import ttk

corTela = '#0d1b1f'
corFundo = '#5f686b'
corBotao = '#f5b400'
corTecla = '#ffffff'

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x313')
janela.config(bg=corFundo)



tela = Frame(janela, width=235, height=50, bg=corTela)
tela.grid(row=0, column=0)

fundo = Frame(janela, width=235, height=268, bg=corFundo)
fundo.grid(row=1, column=0)

allval = ''
valor = StringVar()

def inserir(event):
    global allval

    allval = allval + str(event)
    valor.set(allval)

def calcular():
    global allval

    resultado = eval(allval)
    valor.set(str(resultado))

def limpar():
    global allval

    allval = ''
    valor.set('')

appLabel = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=corTela, fg=corTecla)
appLabel.place(x=0, y=0)


#fileira um
b1 = Button(fundo, command= limpar, text='C', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(fundo, command = lambda: inserir('%'), text='%', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(fundo, command = lambda: inserir('/'), text='/', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

#fileira dois
b4 = Button(fundo, command = lambda: inserir('7'), text='7', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=53)
b5 = Button(fundo, command = lambda: inserir('8'), text='8', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=53)
b6 = Button(fundo, command = lambda: inserir('9'), text='9', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=53)
b13 = Button(fundo, command = lambda: inserir('*'), text='*', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=177, y=53)

#fileira tres
b7 = Button(fundo, command = lambda: inserir('4'), text='4', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=106)
b8 = Button(fundo, command = lambda: inserir('5'), text='5', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=59, y=106)
b9 = Button(fundo, command = lambda: inserir('6'), text='6', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=118, y=106)
b14 = Button(fundo, command = lambda: inserir('-'), text='-', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=177, y=106)

#fileira quatro
b10 = Button(fundo, command = lambda: inserir('1'), text='1', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=0, y=159)
b11 = Button(fundo, command = lambda: inserir('2'), text='2', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=59, y=159)
b12 = Button(fundo, command = lambda: inserir('3'), text='3', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=118, y=159)
b15 = Button(fundo, command = lambda: inserir('+'), text='+', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=159)

#fileira cinco
b16 = Button(fundo, command = lambda: inserir('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=212)
b17 = Button(fundo, command = lambda: inserir('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=212)
b18 = Button(fundo, command= calcular, text='=', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=212)




janela.mainloop()