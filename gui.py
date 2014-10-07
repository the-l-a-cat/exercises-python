

import tkinter


class App(tkinter.Frame):

    def __init__(self, master=None):

        tkinter.Frame.__init__(self, master)
        self.master.title("Meow application")

        self.var_meowMessage = tkinter.StringVar()
        self.var_meowMessage.set("Could you kindly feed me?")

        self.frame_control = tkinter.Frame(
              self
        )

        self.frame_messages = tkinter.Frame(
              self
        )

        self.frame_control.el_quit = tkinter.Button(
              self
            , text = "Close"
            , command = self.quit
            , relief = "groove"
        )

        self.frame_control.el_emit_message = tkinter.Button(
              self
            , text = "Meow"
            , command = self.f_emit_message
        )

        self.frame_messages.el_define_message = tkinter.Entry(
              self
            , textvariable = self.var_meowMessage
        )

        self.pack()
        self.frame_control.pack()
        self.frame_messages.pack()
        self.frame_control.el_quit.pack({"side": "left"})
        self.frame_control.el_emit_message.pack({"side": "left"})
        self.frame_messages.el_define_message.pack()

    def f_emit_message(self):
        print("Meow. {0}".format(self.var_meowMessage.get()))


view = tkinter.Tk()
app = App(master=view)


app.mainloop()
view.destroy()
