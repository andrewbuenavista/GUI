from cgitb import text
import tkinter
import tkinter.messagebox

class AverageCalc:

    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.mainwindow.geometry('500x500')
        self.mainwindow.configure(bg = 'green')

        self.s1 = tkinter.Frame(self.mainwindow,bg='green')
        self.s2 = tkinter.Frame(self.mainwindow,bg='green') 
        self.s3 = tkinter.Frame(self.mainwindow,bg='green')
        self.a =tkinter.Frame(self.mainwindow,bg='green')

        self.s1.pack()
        self.s2.pack()
        self.s3.pack()
        self.a.pack()

        self.score1 = tkinter.Label(self.s1,text = "Enter the score for test 1: ",bg='green',fg="yellow")
        self.score2 = tkinter.Label(self.s2,text = "Enter the score for test 2: ",bg='green',fg='yellow')
        self.score3 = tkinter.Label(self.s3,text = "Enter the score for test 3: ",bg='green',fg='yellow')

        self.entry1 = tkinter.Entry(self.s1,width = 10,bg='green')
        self.entry2 = tkinter.Entry(self.s2,width = 10,bg='green')
        self.entry3 = tkinter.Entry(self.s3,width = 10,bg='green')

        self.average = tkinter.Label(self.a,text = 'Average:',bg='green',fg='yellow')
        
        self.avg_var = tkinter.StringVar()
        self.averagelabel = tkinter.Label(self.a,textvariable = self.avg_var,bg='green')

        self.score1.pack(side='left')
        self.entry1.pack(side='left')

        self.score2.pack(side='left')
        self.entry2.pack(side='left')
        
        self.score3.pack(side='left')
        self.entry3.pack(side='left')

        self.average.pack(side='left')
        self.averagelabel.pack(side='left')

        self.avgbutton = tkinter.Button(self.mainwindow,text = 'Average',command = self.calc,bg='green',fg='yellow')
        self.quitbutton = tkinter.Button(self.mainwindow,text = 'Quit', command = self.mainwindow.destroy,bg='green',fg='yellow')

        self.avgbutton.pack(side = 'left')
        self.quitbutton.pack(side = 'right')
        



        tkinter.mainloop()
    
    def calc(self):
        total = 0

        total += (float(self.entry1.get()) + float(self.entry2.get()) + float(self.entry3.get()))

        average = round((total/3),2)

        self.avg_var.set(average)


myScores = AverageCalc()