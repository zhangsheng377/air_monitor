from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def print_contents(self, event):
        print "hi. contents of entry is now ---->", self.contents.get()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})

        self.contents = StringVar()
        self.contents.set("this is a variable")

        self.entrythingy = Entry()
        self.entrythingy.pack()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>',self.print_contents) #Enter

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()





root = Tk()
app = Application(master=root)
app.master.title("My Do-Nothing Application")
app.master.maxsize(1000, 400)
print "loop start"
app.mainloop()
print "loop end"
try:
    root.destroy()
except:
    print "end"
