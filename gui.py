# -*- coding: utf-8 -*-
'''
Example tkinter/python3 GUI application.

This application showcases:
    - Buttons with associated functions
    - Packer
    - Messagebox
'''

import tkinter
from tkinter import messagebox


class App(tkinter.Frame):
    '''
    Spawn a frame with a few controls and embedded logical interconnection.
    '''

    def __init__(self, master=None):


        # Prefix system:
        #--------------------------------------
        # var_ -> A variable
        # el_  -> A form element, e.g. widget.

        tkinter.Frame.__init__(self, master)
        self.master.title("Meow application")

        self.var_message = tkinter.StringVar()
        self.var_message.set("Could you kindly feed me?")

        self.el_quit = tkinter.Button(
        # Leave the application.
              self
            , text = "Close"
            , command = self.quit
            , relief = "groove"
        )

        self.el_emit_message = tkinter.Button(
        # Run the logic that communicates information to the user.
              self
            , text = "Meow"
            , command = self.f_emit_message
        )

        self.el_define_message = tkinter.Entry(
        # Generate some information.
              self
            , textvariable = self.var_message
        )


        # This section controls placement of elements inside the view.
        #--------------------------------------------------------------
        self.pack()
        self.el_quit.pack({"side": "left"})
        self.el_emit_message.pack({"side": "left"})
        self.el_define_message.pack()

    def f_emit_message(self):
        '''
        Format and communicate information to the user.
        '''

        self.formatted_message = "Meow. {0}".format(self.var_message.get())
        messagebox.showinfo("Meow message", self.formatted_message)


def run():
    '''
    tkinter application runner boilerplate.
    '''
    view = tkinter.Tk()
    app = App(master=view)
    app.mainloop()
    view.destroy()


if __name__ == '__main__':
    run()

