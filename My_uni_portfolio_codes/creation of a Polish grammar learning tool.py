# Плешивцева Ірина ЛАБ-5


import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import random
 




LARGEFONT =("Times New Roman", 20, "bold")
TEXTFONT = ("Times New Roman", 10)






class tkinterApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
         
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        self.frames = {}
 
        for F in (Page1, Page2):
 
            frame = F(container, self)
 
            self.frames[F] = frame
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(Page1)
 
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




 
class Page1(tk.Frame):


    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)
         
        lst = [("przypadek", "liczba pojedyncza", "liczba mnoga"),
                ("mianownik",'-∅','-y'),
                ("dopełniacz",'-a','-ów'),
                ("celownik",'-owi','-om'),
                ("biernik",'-a/-∅','-y'),
                ("narzędnik",'-em','-ami'),
                ("miejscownik", "-ie", "-ach"),
                ("wołacz", "-ie", "-y")]
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self, fg='red',
                               font=('Arial',10))
                self.e.grid(row=i, column=j, padx=5, pady=17)
                self.e.insert(END, lst[i][j])
        mylabel = ttk.Label(self, text="Плешивцева Ірина", font= LARGEFONT)
        mylabel.grid(row=0, column=3, padx=300)
        label = ttk.Label(self, text ="Граматична інформація", font = LARGEFONT)
        label.grid(row=1, column = 3, padx=250)
        label1 = Label(self, text="""
                                     Іменник - це змінна частина, що слугує для позначення назв предметів. Він має такі категорії, як рід,
                                     число, відміна. У польській мові відмінювання іменника залежить від останнього приголосного основи.
                                     """,
                        font= TEXTFONT)
        label1.grid(row=2, column = 3, padx=100)
        label3 = Label(self, text="""
                                     Як і в українській мові, у польській іменник має 7 відмінків. Зараз розглянемо закінчення іменників
                                     чоловічого роду, чия основа закінчується на твердий приголосний і в Н.в. однини має нульове закінчення.
                                     """,
                        font= TEXTFONT)
        label3.grid(row=3, column = 3, padx=100)
        label2 = Label(self, text="""
                                     Ознайомтеся із закінченнями в таблиці ліворуч, а потім перейдіть на сторінку з тестовим питанням.
                                     """,
                        font= TEXTFONT)
        label2.grid(row=4, column = 3, padx=100)


        button1 = ttk.Button(self, text ="Тестове питання",
        command = lambda : controller.show_frame(Page2), cursor="heart")
     
        button1.grid(row = 5, column = 3, padx = 10, pady = 10)
         
 
 
class Page2(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Тестове питання", font = LARGEFONT)
        label.grid(row = 0, column = 3, padx = 250)


        label1 = ttk.Label(self, text="Перекладіть на польську мову", font= TEXTFONT)
        label1.grid(row = 1, column = 3, padx = 250)


        label2 = ttk.Label(self, text="В Еви ще немає ноутбука.", font= TEXTFONT)
        label2.grid(row = 2, column = 3, padx = 250)


        word_singular_forms = {"ноутбук": "laptop (Mian)",
                               "ноутбука": "laptopa",
                               "ноутбуку": "laptopowi",
                               "ноутбук": "laptop (B)",
                               "ноутбуком": "laptopem",
                               "ноутбуці": "laptopie (Miej)",
                               "ноутбуку": "laptopie (W)"}
 
        my_var = tk.StringVar()
        wrong_answers = [value for key, value in word_singular_forms.items() if key != "ноутбука"]
        wrong_answers_question = random.sample(wrong_answers, 3)
        right_answer_question_variant = word_singular_forms.get("ноутбука")
        wrong_answers_question.append(right_answer_question_variant)
        random.shuffle(wrong_answers_question)


        def choose_answer():
            # global selection
            selection = tk.Label(self, text=f"Ви вибрали {str(my_var.get())}", font= TEXTFONT)
            answer_button = ttk.Button(self, text="Відповісти", cursor="cross", command=choose_answer)
            answer_button.grid(row= 9, column= 3, padx=10, pady=10)
            if selection['text'] == "Ви вибрали laptopa":
                tkinter.messagebox.showinfo("Перевірка відповіді", "Правильно!")
            else:
                tkinter.messagebox.showinfo("Перевірка відповіді", f"Ні, правильна відповідь {right_answer_question_variant}")
       
            selection.grid()
   
        rb1 = tk.Radiobutton(self, text=f"Ewa jeszcze nie ma {wrong_answers_question[0]}", variable=my_var, value=f"{wrong_answers_question[0]}", command=choose_answer)
        rb1.grid(row = 4, column = 3)
        rb2 = tk.Radiobutton(self, text=f"Ewa jeszcze nie ma {wrong_answers_question[1]}", variable=my_var, value=f"{wrong_answers_question[1]}", command=choose_answer)
        rb2.grid(row = 5, column = 3)
        rb3 = tk.Radiobutton(self, text=f"Ewa jeszcze nie ma {wrong_answers_question[2]}", variable=my_var, value=f"{wrong_answers_question[2]}", command=choose_answer)
        rb3.grid(row = 6, column = 3)
        rb4 = tk.Radiobutton(self, text=f"Ewa jeszcze nie ma {wrong_answers_question[3]}", variable=my_var, value=f"{wrong_answers_question[3]}", command=choose_answer)
        rb4.grid(row = 7, column = 3)




        button1 = ttk.Button(self, text ="Повернутися до граматики",
                            command = lambda : controller.show_frame(Page1), cursor="heart")
     


        button1.grid(row = 10, column = 3, padx = 10, pady = 10)






app = tkinterApp()
app.mainloop()
