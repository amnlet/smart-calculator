from tkinter import *
from tkinter import ttk
import math

def inserir_valores(tecla):
    if tecla >= '0' or tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)

def operacoes(tecla):
    if tecla == '+' or tecla == '-' or tecla == '*' or tecla == '/':
        if tecla == '+':
            entrada1.set(entrada2.get() + '+')

        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')

        elif tecla == '*':
            entrada1.set(entrada2.get() + '*')

        entrada2.set('')
    
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def raiz():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def apagar():
    ini = 0
    final = len(entrada2.get()) #conta caracteres
    entrada2.set(entrada2.get()[ini: final-1])
def apagar_tudo():
    entrada1.set('')
    entrada2.set('')

def TemaEscuro(*args):
    estilos.configure('mainframe.TFrame', background='#010924')
    estilos_label1.configure('Label1.TLabel', foreground='#FFFFFF', background='#010924')
    estilos_label2.configure('Label2.TLabel', foreground='#FFFFFF', background='#010924')
    estilos_para_botoes.configure('Botoes_numeros.TButton', foreground='#FFFFFF', background='#00044A')
    estilos_para_botoes.map('Botoes_numeros.TButton', background=[('active', '#020A90')])
    estilos_para_apagar.configure('Botoes_apagar.TButton',foreground='#FFFFFF', background='#010924')
    estilos_para_apagar.map('Botoes_apagar.TButton', background=[('active', '#000AB1')])
    estilos_para_restante.configure('Botoes_restantes.TButton', foreground='#FFFFFF', background='#010924')
    estilos_para_restante.map('Botoes_restantes.TButton', background=[('active', '#000AB1')])

def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background='#DBDBDB')
    estilos_label1.configure('Label1.TLabel', foreground='#000000', background='#DBDBDB')
    estilos_label2.configure('Label2.TLabel', foreground='#000000', background='#DBDBDB')
    estilos_para_botoes.configure('Botoes_numeros.TButton', foreground='#000000', background='#FFFFFF')
    estilos_para_botoes.map('Botoes_numeros.TButton', background=[('active', '#B9B9B9')])
    estilos_para_apagar.configure('Botoes_apagar.TButton', foreground='#000000', background='#CECECE')
    estilos_para_apagar.map('Botoes_apagar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])
    estilos_para_restante.configure('Botoes_restantes.TButton', foreground='#000000', background='#CECECE')
    estilos_para_restante.map('Botoes_restantes.TButton', background=[('active', '#858585')])


root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Estilo da janela mainframe
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background='#DBDBDB')

#estilo dos Labels
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font='arial 15', anchor='e', background='#DBDBDB')

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font='arial 40', anchor='e', background='#DBDBDB')

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)


#Entradas de números
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style='Label1.TLabel')
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style='Label2.TLabel')
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))


#estilos para os botoes numerais e tambem os demais

estilos_para_botoes = ttk.Style()
estilos_para_botoes.configure('Botoes_numeros.TButton', background='#FFFFFF', width=5, font='arial 22', relief='flat')
estilos_para_botoes.map('Botoes_numeros.TButton', background=[('active', '#B9B9B9')])

estilos_para_apagar = ttk.Style()
estilos_para_apagar.configure('Botoes_apagar.TButton', background='#CECECE', width=5, font='arial 22', relief='flat')
estilos_para_apagar.map('Botoes_apagar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilos_para_restante = ttk.Style()
estilos_para_restante.configure('Botoes_restantes.TButton', background='#CECECE', width=5, font='arial 22', relief='flat')
estilos_para_restante.map('Botoes_restantes.TButton', background=[('active', '#858585')])


#Botoes de numerais
button0 = ttk.Button(mainframe, text='0', style='Botoes_numeros.TButton', command=lambda: inserir_valores('0'))
button1 = ttk.Button(mainframe, text='1', style='Botoes_numeros.TButton', command=lambda: inserir_valores('1'))
button2 = ttk.Button(mainframe, text='2', style='Botoes_numeros.TButton', command=lambda: inserir_valores('2'))
button3 = ttk.Button(mainframe, text='3', style='Botoes_numeros.TButton', command=lambda: inserir_valores('3'))
button4 = ttk.Button(mainframe, text='4', style='Botoes_numeros.TButton', command=lambda: inserir_valores('4'))
button5 = ttk.Button(mainframe, text='5', style='Botoes_numeros.TButton', command=lambda: inserir_valores('5'))
button6 = ttk.Button(mainframe, text='6', style='Botoes_numeros.TButton', command=lambda: inserir_valores('6'))
button7 = ttk.Button(mainframe, text='7', style='Botoes_numeros.TButton', command=lambda: inserir_valores('7'))
button8 = ttk.Button(mainframe, text='8', style='Botoes_numeros.TButton', command=lambda: inserir_valores('8'))
button9 = ttk.Button(mainframe, text='9', style='Botoes_numeros.TButton', command=lambda: inserir_valores('9'))

# botoes de apagar, parenteses e ponto.
button_apagar = ttk.Button(mainframe, text=chr(9003), style='Botoes_apagar.TButton', command=lambda: apagar())
button_apagar_tudo = ttk.Button(mainframe, text='C', style='Botoes_apagar.TButton', command=lambda: apagar_tudo())
button_parenteses1 = ttk.Button(mainframe, text='(', style='Botoes_restantes.TButton', command=lambda: inserir_valores('('))
button_parenteses2 = ttk.Button(mainframe, text=')', style='Botoes_restantes.TButton', command=lambda: inserir_valores(')'))
button_ponto = ttk.Button(mainframe, text='.', style='Botoes_restantes.TButton', command=lambda: inserir_valores('.'))

#botoes de operacao divisao, multiplicacao, soma, subtracao, igualdade, radiciacao
button_divisao = ttk.Button(mainframe, text=chr(247), style='Botoes_restantes.TButton', command=lambda: operacoes('/'))
button_multiplicacao = ttk.Button(mainframe, text='x', style='Botoes_restantes.TButton', command=lambda: operacoes('*'))
button_adicao = ttk.Button(mainframe, text='+', style='Botoes_restantes.TButton', command=lambda: operacoes('+'))
button_subtracao = ttk.Button(mainframe, text='-', style='Botoes_restantes.TButton', command=lambda: operacoes('-'))
button_igual = ttk.Button(mainframe, text='=', style='Botoes_restantes.TButton', command=lambda: operacoes('='))
button_raiz = ttk.Button(mainframe, text='√', style='Botoes_restantes.TButton', command=lambda: raiz())

#definir grid para parenteses, C e apagar
button_parenteses1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parenteses2.grid(column=1, row=2, sticky=(W, N, E, S))
button_apagar_tudo.grid(column=2, row=2, sticky=(W, N, E, S))
button_apagar.grid(column=3, row=2, sticky=(W, N, E, S))

#definir botoes 7, 8, 9 e divisao
button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_divisao.grid(column=3, row=3, sticky=(W, N, E, S))

#definir botoes 4, 5, 6 e multiplicacao
button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacao.grid(column=3, row=4, sticky=(W, N, E, S))

#definir botoes 1, 2, 3 e soma
button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_adicao.grid(column=3, row=5, sticky=(W, N, E, S))

#denifir botoes 0, ponto e menos
button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_ponto.grid(column=2, row=6, sticky=(W, N, E, S))
button_subtracao.grid(column=3, row=6, sticky=(W, N, E, S))

#definir botoes = e raiz
button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_raiz.grid(column=3, row=7, sticky=(W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)


root.bind('<KeyPress-e>', TemaEscuro)
root.bind('<KeyPress-c>', TemaClaro)

#app rodando abaixo
root.mainloop()