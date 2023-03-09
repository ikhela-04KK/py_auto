from tkinter.ttk import Progressbar
from tkinter import*
from tkinter import ttk
# initialisation du programme tkinter
w = Tk()

# *  cette configuration permet de centrer au milieu de l'écran 
w.geometry('427x250')
w.resizable(False, False) 
width_of_window = 427
height_of_window = 250 
screen_width = w.winfo_screenwidth() # donne des informations sur l'écran actuel
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width /2) - (width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate)) # cette geometry est pour placer le widjet au centre de l'écran 

#*  faire la progress bar 
s=ttk.Style()
s.theme_use('clam')
s.configure("red.horizontal.TProgressbar",foreground='red', background="#4f4f4f")
progress=Progressbar(w,style="red.Horizontal.TProgressbar", orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=-10, y=235) # permet au chargement de donner l'effet d'avancer 

# cette progress est remplie d'information qu'il faut comprendre
# apprendre c'est quoi le threads 


#* la deuxieme fenêtre qui suit la bar de char 
def main_window():
    q=Tk()
    q.geometry('427x250')
    l1=Label(w,text="ADD TEXT HERE", fg='dark grey', bg=None)
    l=('Calibri (Body)',24,'bold')
    l1.config(font=l)
    l1.place(x=80,y=100)
    q.mainloop()

# la bar de chargement

def bar():
    l4 = Label(w, text='Loading...',fg='white', bg='#249794')
    lst4=('Fauna One',10)
    l4.configure(font=lst4)
    l4.place(x=0,y=210)

    import time
    for r, _ in enumerate(range(100)):
        progress['value'] = r
        w.update_idletasks() # c'est ça qui permet à la bar de s'afficher 
        time.sleep(0.03)
        '''
        ir=0
        for i in range(100):
            progress['value'] = r
            w.update_idletasks()
            time.sleep(0.03)
            r+=1
        '''
    w.destroy()
    main_window()

#adding frame

Frame(w,width=427,height=241,bg='#249794').place(x=0,y=0)
b1 = Button(w,width=10, height=1, text='Get Started', command=bar, border=0, fg='#243734')
b1.place(x=170,y=200)

#labels

l1 = Label(w, text="SPLASH", fg='white', bg="#249794")
lst1 = ('Cambria', 18)
l1.configure(font=lst1)
l1.place(x=50,y=30)

l2 = Label(w, text="SCREEN", fg='white', bg="#249794")
lst2 = ('Lovers Quarrel', 18 ,)
l2.configure(font=lst2)
l2.place(x=50,y=80)

l3 = Label(w, text="PROGRAMMED", fg='white', bg="#249794")
lst3 = ('Calibri (Body)', 13)
l3.configure(font=lst3)
l3.place(x=50,y=110)


s=ttk.Style()
s.theme_use('clam')
s.configure("red.horizontal.TProgressbar",foreground='red',background="#4f4f4f")
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=-10,y=235)

w.mainloop()
