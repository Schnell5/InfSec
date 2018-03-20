from tkinter import *


root = Tk()

def hello(event):
    print('Got tag event')

text = Text()
text.config(font=('courier', 16, 'normal'))
text.config(width=20, height=12)
text.pack(fill=BOTH, expand=YES)
text.insert(END, 'This is\n\nthe meaning\n\nof life.\n\n')

btn = Button(text, text='Spam', command=lambda: hello(0))
btn.pack()
text.window_create(END, window=btn)
text.insert(END, '\n\n')
imgfile = '/Users/ekantysev/Desktop/Programming/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images/lpython_sm_ad.gif'
img = PhotoImage(file=imgfile)
text.image_create(END, image=img)

text.tag_add('demo', '1.5', '1.7')
text.tag_add('demo', '3.0', '3.3')
text.tag_add('demo', '5.3', '5.7')
text.tag_config('demo', background='purple')
text.tag_config('demo', foreground='white')
text.tag_config('demo', font=('times', 16, 'underline'))
text.tag_bind('demo', '<Double-1>', hello)
root.mainloop()

