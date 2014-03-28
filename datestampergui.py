#!/usr/bin/python
# -*- coding utf-8 -*-

# print("Hello World")

# """
# ZetCode Tkinter tutorial

# This script shows a simple window
# on the screen.

# autho: Jan Bodnar
# last modified: January 2011
# website: www.zetcode.com
# """

# from Tkinter import Tk, Frame, BOTH

# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent, background="white")

#         self.parent = parent

#         self.initUI()

#     def initUI(self):

#         self.parent.title("Date Stamper")
#         self.pack(fill=BOTH, expand=1)

# def main():

#     root = Tk()
#     root.geometry("1000x400+300+300")
#     app = Example(root)
#     root.mainloop()


# if __name__== '__main__':
#     main()










# import Tkinter, tkFileDialog, Tkconstants 
# from Tkinter import * 
# dirtext='Select your pictures folder'
# filetext= 'Select your watermark file'
# def openFile():
#     filename = tkFileDialog.askopenfilename(parent=root,initialdir='/home/',title=filetext , filetypes=[('image files', '.png')]) ## filename not filehandle
#     filebut["text"]= str(filename) if filename else filetext
# def openDirectory():
#     dirname = tkFileDialog.askdirectory(parent=root, initialdir='/home/', title=dirtext) 
#     dirbut["text"] = str(dirname) if dirname else dirtext
# root = Tk() 
# root.title('Watermark Image Processing 1.0b')
# #Options for buttons
# button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
# #Define asking directory button
# dirbut= Button(root, text = dirtext, fg = 'black', command= openDirectory)
# dirbut.pack(**button_opt) ## must pack separately to get the value to dirbut
# #Define asking watermark file button
# filebut = Button(root, text = filetext, fg = 'black', command= openFile)
# filebut.pack(**button_opt)
# root.mainloop()




"""
ZetCode Tkinter tutorial

This program draws three
rectangles filled with different
colors.

author: Jan Bodar
last modified: January 2011
website: www.zetcode.com
"""

from Tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Colors")        
        # self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 80, 
            outline="#fb0", fill="#fb0")
        canvas.create_rectangle(150, 10, 240, 80, 
            outline="#f50", fill="#f50")
        canvas.create_rectangle(270, 10, 370, 80, 
            outline="#05f", fill="#05f")            
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("400x100+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  
