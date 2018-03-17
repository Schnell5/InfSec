from tkinter import *
from quitter import Quitter


fields = 'Name', 'Job', 'Pay'


def fetch(variables):
    for variable in variables:
        print('Input => {0}'.format(variable.get()))


def makeform(root, fields):
    form = Frame(root)
    left = Frame(form)
    right = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    right.pack(side=RIGHT, fill=X, expand=YES)

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)
        ent = Entry(right)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        var.set('enter here')
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    Quitter(root).pack(side=RIGHT)
    root.mainloop()
