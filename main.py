from tkinter import *
from functools import partial

"""
            arquivo e opções
        [       display     ]
btns:   Clear, mr, div, 
        7, 8, 9, multiplicar
        4, 5, 6, menos
        1, 2, 3, mais
         , 0,  , igual
"""
class App:
    def __init__(self, master=None):
        def rows():
            # ROW 1
            self.clearBtn = Button(self.buttonFrame, text="CLEAR", font=("Verdana", 16, "bold"), bg="white", fg="black",
                                command=lambda: self.limpar())
            self.clearBtn.grid(row=0, column=0, sticky=W+E, columnspan=2)

            self.clearBtn = Button(self.buttonFrame, text="MR", font=("Verdana", 16, "bold"), bg="white", fg="black",
                                command=lambda: self.inputValue("(MR)"))
            self.clearBtn.grid(row=0, column=2, sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="/", font=("Verdana", 16, "bold"), bg="white", fg="black",
                                command=lambda: self.inputValue("/"))
            self.clearBtn.grid(row=0, column=3, sticky=W+E)

            # ROW 2
            self.clearBtn = Button(self.buttonFrame, text="7", font=("Verdana", 16), bg="white", fg="black",
                                command=lambda: self.inputValue("7"))
            self.clearBtn.grid(row=1, column=0, sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="8", font=("Verdana", 16), bg="white", fg="black",
                                command=lambda: self.inputValue("8"))
            self.clearBtn.grid(row=1, column=1, sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="9", font=("Verdana", 16), bg="white", fg="black",
                                command=lambda: self.inputValue(9))
            self.clearBtn.grid(row=1, column=2, sticky=W+E)
            self.oitoBtn = Button(self.buttonFrame, text="*", font=("Verdana", 16, "bold"), bg="white", fg="black",
                                command=lambda: self.inputValue("*"))
            self.oitoBtn.grid(row=1, column=3, sticky=W+E)

            # ROW 3
            self.clearBtn = Button(self.buttonFrame, text="4", font=("Verdana", 16), bg="white", fg="black", 
                               command=lambda: self.inputValue("4"))
            self.clearBtn.grid(row = 2, column=0,sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="5", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.inputValue("5"))
            self.clearBtn.grid(row = 2, column=1,sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="6", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.inputValue("6"))
            self.clearBtn.grid(row = 2, column=2,sticky=W+E)
            self.oitoBtn = Button(self.buttonFrame, text="-", font=("Verdana", 16, "bold"), bg="white", fg="black", 
                               command=lambda: self.inputValue("-"))
            self.oitoBtn.grid(row = 2, column=3,sticky=W+E)

            # ROW 4
            self.clearBtn = Button(self.buttonFrame, text="1", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.inputValue("1"))
            self.clearBtn.grid(row = 3, column=0,sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="2", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.inputValue("2"))
            self.clearBtn.grid(row = 3, column=1,sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="3", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.inputValue("3"))
            self.clearBtn.grid(row = 3, column=2,sticky=W+E)
            self.oitoBtn = Button(self.buttonFrame, text="+", font=("Verdana", 16, "bold"), bg="white", fg="black", 
                                command=lambda: self.inputValue("+"))
            self.oitoBtn.grid(row = 3, column=3,sticky=W+E)

            # ROW 5
            self.clearBtn = Button(self.buttonFrame, text="<-", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.backspace(), width=1)
            self.clearBtn.grid(row = 4, column=0,sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text="0", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.inputValue("0"), width=1)
            self.clearBtn.grid(row = 4, column=1,sticky=W+E)
            self.clearBtn = Button(self.buttonFrame, text=".", font=("Verdana", 16), bg="white", fg="black", 
                                command=lambda: self.inputValue("."), width=1)
            self.clearBtn.grid(row = 4, column=2,sticky=W+E)
            self.oitoBtn = Button(self.buttonFrame, text="=", font=("Verdana", 16, "bold"), bg="white", fg="black", 
                                  command=lambda: self.calcula(), width=1)
            self.oitoBtn.grid(row = 4, column=3,sticky=W+E)


        self.root = Tk()
        self.root.title("Minha Calculadora")
        self.root.geometry("+100+100")
        self.root.wm_resizable(0, 0)
        
        self.titulo = Label(self.root, text="Calculator", font=("Verdana", 16))
        self.titulo.pack(padx=100, pady=10)

        self.visorValue = StringVar(self.root, value="")
        self.visor = Entry(self.root, font=("Verdana", 16), background="light blue", state=DISABLED
                            ,borderwidth=5, textvariable=self.visorValue, justify=RIGHT)
        self.visor.pack(padx=8, pady=5, fill="x")

        self.buttonFrame = Frame(self.root,)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.columnconfigure(2, weight=1)
        self.buttonFrame.columnconfigure(3, weight=1)
        rows()
        self.buttonFrame.pack(fill='both', padx=8)
        
        self.root.mainloop()
        
    def inputValue(self, valor):
        visor = self.visorValue.get()
        self.visorValue.set(visor + f"{valor}")


    def char_check(self, visor):
        for char in visor:
            if char in "+-*/":
                return True
        return False


    def rec_resolve(self, visor):
        def rec_pegaValor(vetor, comeco, depois=False):
            # print(comeco)
            if 0 > comeco or comeco >= len(vetor):
                return ""

            if vetor[comeco] in "0123456789.-":
                if depois:
                    if vetor[comeco] == "-" and not vetor[comeco-1] in "*/":
                        return ""
                    return vetor[comeco] + rec_pegaValor(vetor, comeco + 1, depois)

                if vetor[comeco] == "-":
                    return vetor[comeco]
                return rec_pegaValor(vetor, comeco-1, depois) + vetor[comeco]

            if vetor[comeco] not in "+*/":
                raise ValueError
            return ""

        # (OLHE PARA CA) tudo começa aqui
        i1 = 0
        if "*" in visor and "/" in visor:
            
            a = visor.index("/")
            b = visor.index("*")
            
            if a > b:
                i1 = 1
            
        if "/" in visor and i1 == 0:
            i = visor.index("/")
            part1 = rec_pegaValor(visor, i-1)
            part2 = rec_pegaValor(visor, i+1, True)
            
            inicio = i - len(part1)
            fim = i + len(part2) + 1

            part1 = float(part1)
            part2 = float(part2)
            # executar a operação com as partes
            resultado = part1 / part2
                        
            # substituir no local.
            visor = visor[:inicio] + str(resultado) + visor[fim:]
            
            visor = self.rec_resolve(visor)

        elif "*" in visor : # se o char for uma operação de * ou /
            i = visor.index("*")
            part1 = rec_pegaValor(visor, i-1)
            part2 = rec_pegaValor(visor, i+1, True)
            
            inicio = i - len(part1)
            fim = i + len(part2) + 1

            part1 = float(part1)
            part2 = float(part2)
            # executar a operação com as partes
            resultado = part1 * part2
                        
            # substituir no local.
            visor = visor[:inicio] + str(resultado) + visor[fim:]
            
            visor = self.rec_resolve(visor)

        elif "+" in visor : # se o char for uma operação de * ou /
            i = visor.index("+")
            part1 = rec_pegaValor(visor, i-1)
            part2 = rec_pegaValor(visor, i+1, True)
            
            inicio = i - len(part1)
            fim = i + len(part2) + 1

            part1 = float(part1)
            part2 = float(part2)
            # executar a operação com as partes
            resultado = part1 + part2
                        
            # substituir no local.
            visor = visor[:inicio] + str(resultado) + visor[fim:]
            
            visor = self.rec_resolve(visor)

        elif "-" in visor : # se o char for uma operação de * ou /
            i = visor.index("-")
            part1 = rec_pegaValor(visor, i-1)
            part2 = rec_pegaValor(visor, i+1, True)
            
            if part1 != "":
                # As vezes o menos não é a operação mas sim o indicativo do numero negativo
                inicio = i - len(part1)
                fim = i + len(part2) + 1

                part1 = float(part1)
                part2 = float(part2)

                # executar a operação com as partes
                resultado = part1 - part2
                            
                # substituir no local.
                visor = visor[:inicio] + str(resultado) + visor[fim:]
                visor = self.rec_resolve(visor)
        
        return visor 

    def calcula(self):
        # self.visorValue.set(eval(visor)) # versão preguiçosa
        
        visor = self.visorValue.get()
        try:
            resultado = self.rec_resolve(visor)
            print(resultado)
            try:
                # int() sozinho pega so a parte inteira
                resultado = float(resultado)
                resto = resultado % 10
                if resto < 0:
                    resultado = int(resultado)

            except ValueError:
                self.visorValue.set("Operação invalida")
                
            self.visorValue.set(f"{resultado}")
        except ZeroDivisionError:
                    self.visorValue.set("Bad Division")
        except ValueError:
            self.visorValue.set("Operação invalida")
                    
    def limpar(self):
        self.visorValue.set("")

    def backspace(self):
        visor = self.visorValue.get()
        self.visorValue.set(visor[:-1])



App()
