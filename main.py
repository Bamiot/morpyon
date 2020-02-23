from tkinter import *
from fonctions.morpion import morpion
from fonctions.AI import morpyon


m = morpion(player=1,finished=0)
window = Tk()

ia = morpyon(m.grid)

lb = Label(window, text='joueur rouge')
lb.grid(row=3, column=0)

selected = IntVar()
selected.set(2)
rad1 = Radiobutton(window, text='Player Vs Player', value=1, variable=selected)
rad1.grid(row=3, column=1)
rad2 = Radiobutton(window, text='Player Vs AI', value=2, variable=selected)
rad2.grid(row=3, column=2)


def upd_grid():
    if m.get_case(0,0) == 1: bt0.config(bg="red")
    elif m.get_case(0,0) == 2: bt0.config(bg="green")
    if m.get_case(0,1) == 1: bt1.config(bg="red")
    elif m.get_case(0,1) == 2: bt1.config(bg="green")
    if m.get_case(0,2) == 1: bt2.config(bg="red")
    elif m.get_case(0,2) == 2: bt2.config(bg="green")
    if m.get_case(1,0) == 1: bt3.config(bg="red")
    elif m.get_case(1,0) == 2: bt3.config(bg="green")
    if m.get_case(1,1) == 1: bt4.config(bg="red")
    elif m.get_case(1,1) == 2: bt4.config(bg="green")
    if m.get_case(1,2) == 1: bt5.config(bg="red")
    elif m.get_case(1,2) == 2: bt5.config(bg="green")
    if m.get_case(2,0) == 1: bt6.config(bg="red")
    elif m.get_case(2,0) == 2: bt6.config(bg="green")
    if m.get_case(2,1) == 1: bt7.config(bg="red")
    elif m.get_case(2,1) == 2: bt7.config(bg="green")
    if m.get_case(2,2) == 1: bt8.config(bg="red")
    elif m.get_case(2,2) == 2: bt8.config(bg="green")


def turn():
    if m.player == 1:
        m.player = 2
        lb.config(text='joueur vert') #aka j2
    elif m.player == 2:
        m.player = 1
        lb.config(text='joueur rouge') #aka j1


def if_finished():
    for i in range(3):
        for ii in range(3):
            if m.get_case(i, ii) == 0:
                return False
                break
    return True


def if_win():
    for i in range(3):
        if m.get_case(0,i) == m.get_case(1,i) == m.get_case(2,i) != 0:
            return True
    for i in range(3):
        if m.get_case(i,0) == m.get_case(i,1) == m.get_case(i,2) != 0:
            return True
    if m.get_case(0,0) == m.get_case(1,1) == m.get_case(2,2) != 0:
        return True
    elif m.get_case(2,0) == m.get_case(1,1) == m.get_case(0,2) != 0: return True
    else: return False


def win(player):
    if player == 1:
        lb.config(text="le joueur rouge a gagner")
    elif player == 2:
        lb.config(text="le joueur vert a gagner")


def clicked(x,y):
    if (m.get_case(x,y) == 0) and (m.finished == 0):
        m.set_case(x,y,m.player)
        upd_grid()
        m.print_grid()
        if if_win():
            win(m.player)
            m.finished = 1
        elif if_finished():
            lb.config(text="Egalité")
            m.finished = 1;
            pass
        else:
            if selected.get() == 1:
                turn()
            elif selected.get() == 2:
                turn()
                xy = ia.play(m.grid)
                m.set_case(xy[0],xy[1],m.player)
                upd_grid()
                m.print_grid()
                if if_win():
                    win(2)
                    m.finished = 1
                else : turn()
    elif m.finished == 1:

        exit()


def clicked0():
    clicked(0,0)


def clicked1():
    clicked(0,1)


def clicked2():
    clicked(0,2)


def clicked3():
    clicked(1,0)


def clicked4():
    clicked(1,1)


def clicked5():
    clicked(1,2)


def clicked6():
    clicked(2,0)


def clicked7():
    clicked(2,1)


def clicked8():
    clicked(2,2)


window.title("Morpyon")
window.geometry('450x510')

bt0 = Button(window, command=clicked0, bg="light blue")
bt0.grid(column=0, row=0, sticky="nwse")
bt1 = Button(window, command=clicked1, bg="light blue")
bt1.grid(column=1, row=0, sticky="nwse")
bt2 = Button(window, command=clicked2, bg="light blue")
bt2.grid(column=2, row=0, sticky="nwse")
bt3 = Button(window, command=clicked3, bg="light blue")
bt3.grid(column=0, row=1, sticky="nwse")
bt4 = Button(window, command=clicked4, bg="light blue")
bt4.grid(column=1, row=1, sticky="nwse")
bt5 = Button(window, command=clicked5, bg="light blue")
bt5.grid(column=2, row=1, sticky="nwse")
bt6 = Button(window, command=clicked6, bg="light blue")
bt6.grid(column=0, row=2, sticky="nwse")
bt7 = Button(window, command=clicked7, bg="light blue")
bt7.grid(column=1, row=2, sticky="nwse")
bt8 = Button(window, command=clicked8, bg="light blue")
bt8.grid(column=2, row=2, sticky="nwse")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(2, weight=1)



window.mainloop()