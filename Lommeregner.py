from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Lommeregner")
        self.master.geometry("215x231")
        self.pack()
        self.model_init()
        self.controller_init()
        self.view_init()

# Model init, der opretter variabler for størrelsen af knapperne
    def model_init(self):
        self.button_width = 7
        self.button_height = 2

# controller init, der laver alle knapperne og giver dem navne
    def controller_init(self):
        self.Button1 = Button(self, text="1", width=self.button_width, height=self.button_height)
        self.Button1.bind("<Button-1>", self.view_tal1)

        self.Button2 = Button(self, text="2", width=self.button_width, height=self.button_height)
        self.Button2.bind("<Button-1>", self.view_tal2)

        self.Button3 = Button(self, text="3", width=self.button_width, height=self.button_height)
        self.Button3.bind("<Button-1>", self.view_tal3)

        self.Button4 = Button(self, text="4", width=self.button_width, height=self.button_height)
        self.Button4.bind("<Button-1>", self.view_tal4)

        self.Button5 = Button(self, text="5", width=self.button_width, height=self.button_height)
        self.Button5.bind("<Button-1>", self.view_tal5)

        self.Button6 = Button(self, text="6", width=self.button_width, height=self.button_height)
        self.Button6.bind("<Button-1>", self.view_tal6)

        self.Button7 = Button(self, text="7", width=self.button_width, height=self.button_height)
        self.Button7.bind("<Button-1>", self.view_tal7)

        self.Button8 = Button(self, text="8", width=self.button_width, height=self.button_height)
        self.Button8.bind("<Button-1>", self.view_tal8)

        self.Button9 = Button(self, text="9", width=self.button_width, height=self.button_height)
        self.Button9.bind("<Button-1>", self.view_tal9)

        self.Button0 = Button(self, text="0", width=self.button_width, height=self.button_height)
        self.Button0.bind("<Button->", self.view_tal0)


        self.Button_lig = Button(self, text="=", width=self.button_width-3, height=self.button_height+self.button_height+1)
        self.Button_lig.bind("<Button->", self.model_beregn)

        self.Button_plus = Button(self, text="+", width=self.button_width-3, height=self.button_height+self.button_height+1)
        self.Button_plus.bind("<Button->", self.view_tal_plus)

        self.Button_minus = Button(self, text="-", width=self.button_width-3, height=self.button_height)
        self.Button_minus.bind("<Button->", self.view_tal_minus)

        self.Button_gange = Button(self, text="*", width=self.button_width, height=self.button_height)
        self.Button_gange.bind("<Button->", self.view_tal_gange)

        self.Button_division = Button(self, text="/", width=self.button_width, height=self.button_height)
        self.Button_division.bind("<Button->", self.view_tal_division)

        self.Button_clear = Button(self, text="C", width=self.button_width, height=self.button_height)
        self.Button_clear.bind("<Button->", self.view_clear)

        self.Button_start_parantes = Button(self, text=")", width=self.button_width-4, height=self.button_height)
        self.Button_start_parantes.bind("<Button->", self.view_tal_slut_parantes)

        self.Button_slut_parantes = Button(self, text="(", width=self.button_width-4, height=self.button_height)
        self.Button_slut_parantes.bind("<Button->", self.view_tal_start_parantes)

        self.Button_punktum = Button(self, text=".", width=self.button_width, height=self.button_height)
        self.Button_punktum.bind("<Button->", self.view_tal_punktum)

        self.view_button_placering()

# view init der placerer alle knapperne i bestemt rækkefølge i et grid
    def view_button_placering(self):
        self.Button1.grid(row=3, column=0)
        self.Button2.grid(row=3, column=1)
        self.Button3.grid(row=3, column=2)
        self.Button4.grid(row=4, column=0)
        self.Button5.grid(row=4, column=1)
        self.Button6.grid(row=4, column=2)
        self.Button7.grid(row=5, column=0)
        self.Button8.grid(row=5, column=1)
        self.Button9.grid(row=5, column=2)
        self.Button0.grid(row=6, column=1)

        self.Button_lig.grid(row=5, column=3, rowspan=2)
        self.Button_plus.grid(row=3, column=3, rowspan=2)
        self.Button_minus.grid(row=1, column=3)
        self.Button_gange.grid(row=1, column=2)
        self.Button_division.grid(row=1, column=1)
        self.Button_clear.grid(row=1, column=0)
        self.Button_start_parantes.grid(row=6, column=0, sticky="e")
        self.Button_slut_parantes.grid(row=6, column=0, sticky="w")
        self.Button_punktum.grid(row=6, column=2)

# view init der laver en entry og placerer den øverst
    def view_init(self):
        self.number_bar = Entry(self, width=35, justify="center")
        self.number_bar.grid(row=0, column=0, columnspan=10)

# view inits, der skriver tal og tegn i entryen for hver knap
    def view_tal1(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "1")

    def view_tal2(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "2")

    def view_tal3(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "3")

    def view_tal4(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "4")

    def view_tal5(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "5")

    def view_tal6(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "6")

    def view_tal7(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "7")

    def view_tal8(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "8")

    def view_tal9(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "9")

    def view_tal0(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "0")

    def view_tal_plus(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "+")

    def view_tal_minus(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "-")

    def view_tal_gange(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "*")

    def view_tal_division(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "/")

    def view_tal_start_parantes(self, event):
        self.number_bar.insert(len(self.number_bar.get()), "(")

    def view_tal_slut_parantes(self, event):
        self.number_bar.insert(len(self.number_bar.get()), ")")

    def view_tal_punktum(self, event):
        self.number_bar.insert(len(self.number_bar.get()), ".")

# view init der fjerner alt tekst i entryen
    def view_clear(self, event):
        self.number_bar.delete(0, "end")

# model init, der beregner entryen
    def model_beregn(self, event):
        self.udregning = eval(self.number_bar.get())
        self.view_vis_beregning()

# view init, der sætter svaret ind i entryen
    def view_vis_beregning(self):
        self.number_bar.delete(0, "end")
        self.number_bar.insert(0, (self.udregning))



root = Tk()
app = Window(root)
root.mainloop()
