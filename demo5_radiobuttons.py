import tkinter
import tkinter.messagebox

class KiloConverterGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()                 

        self.main_window.geometry('200x100')
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')\

        self.radio_var = tkinter.IntVar()  

        self.rb1 = tkinter.Radiobutton(self.top_frame,text="Option1",variable = self.radio_var,value = 10)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text="Option2",variable = self.radio_var,value = 20)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text="Option3",variable = self.radio_var,value = 30)

        #set initial value
        self.rb1.select()

        self.rb1.pack(side='top')
        self.rb2.pack(side='top')
        self.rb3.pack(side='top')


        self.okbutton = tkinter.Button(self.bottom_frame,text = 'Ok',command = self.show_choice)
        self.reset_button = tkinter.Button(self.bottom_frame,text = 'Reset', command = self.rb1.select)
        self.quit_button = tkinter.Button(self.bottom_frame,text = 'Quit',command = self.main_window.destroy)

      
        self.okbutton.pack(side='left')
        self.reset_button.pack(side='left')
        self.quit_button.pack(side='left')        


        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection",f"You have selected option {self.radio_var.get()}")

        

kilo_conv = KiloConverterGUI()

print("moving on.....")

