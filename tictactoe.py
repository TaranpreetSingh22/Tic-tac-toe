from tkinter import *
from tkinter import messagebox

def main():
    win=Tk()

    w=400
    h=500

    ww=win.winfo_screenwidth()
    wh=win.winfo_screenheight()

    x=(ww/2)-(w/2)
    y=(wh/2)-(h/2)

    win.geometry('%dx%d+%d+%d'%(w,h,x,y))
    win.resizable(0,0)

    global first,col,textcol
    first='X'
    col='red'
    textcol='black'
    def write1():
        global first,col
        t1.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t1.cget('text')=='X':
            first='O'
            col='blue'  
        else:
            first='X'
            col='red'
    
        if (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='O') :
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='X') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='X') or 
            (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='X') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='X') or 
            (t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='X') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

    def write2():
        global first,col
        t2.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t2.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='X') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='X') or 
            (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='X') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):       
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

    def write3():
        global first,col
        t3.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t3.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t7.cget('text')=='X' and t5.cget('text')=='X' and t3.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='O' and t3.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='O') :
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='X') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='X') or 
            (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='X') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='X') or 
            (t3.cget('text')=='X' and t5.cget('text')=='O' and t7.cget('text')=='O') or (t3.cget('text')=='X' and t5.cget('text')=='X' and t7.cget('text')=='O') or (t3.cget('text')=='O' and t5.cget('text')=='X' and t7.cget('text')=='O') or (t3.cget('text')=='O' and t5.cget('text')=='O' and t7.cget('text')=='X') or (t3.cget('text')=='O' and t5.cget('text')=='X' and t7.cget('text')=='X') or (t3.cget('text')=='X' and t5.cget('text')=='O' and t7.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

    def write4():
        global first,col
        t4.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t4.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='X') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='X') or 
            (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='O') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='X') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

    def write5():
        global first,col
        t5.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t5.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t5.cget('text')=='X' and t7.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif ((t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t5.cget('text')=='O' and t7.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O') and t6.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='O') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='X') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='X') or 
            (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='X') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()


    def write6():
        global first,col
        t6.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t6.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='O') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='X') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='X') or 
            (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='X') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()


    def write7():
        global first,col
        t7.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t7.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t5.cget('text')=='X' and t3.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='O' and t3.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='X') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='X') or 
            (t7.cget('text')=='X' and t5.cget('text')=='O' and t3.cget('text')=='O') or (t7.cget('text')=='X' and t5.cget('text')=='X' and t3.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='X' and t3.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='O' and t3.cget('text')=='X') or (t7.cget('text')=='O' and t5.cget('text')=='X' and t3.cget('text')=='X') or (t7.cget('text')=='X' and t5.cget('text')=='O' and t3.cget('text')=='X') or 
            (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='X') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

    def write8():
        global first,col
        t8.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t8.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='X') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X') or 
            (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='X') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

    def write9():
        global first,col
        t9.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t9.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='O') :
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='X') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='X') or 
            (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='X') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='X') or 
            (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='X') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()



    t1=Button(win,width=15,height=10,command=write1)
    t1.grid(column=2,row=3,padx=(30,0))
    t2=Button(win,width=15,height=10,command=write2)
    t2.grid(column=3,row=3)
    t3=Button(win,width=15,height=10,command=write3)
    t3.grid(column=4,row=3)
    t4=Button(win,width=15,height=10,command=write4)
    t4.grid(column=2,row=4,padx=(30,0))
    t5=Button(win,width=15,height=10,command=write5)
    t5.grid(column=3,row=4)
    t6=Button(win,width=15,height=10,command=write6)
    t6.grid(column=4,row=4)
    t7=Button(win,width=15,height=10,command=write7)
    t7.grid(column=2,row=5,padx=(30,0))
    t8=Button(win,width=15,height=10,command=write8)
    t8.grid(column=3,row=5)
    t9=Button(win,width=15,height=10,command=write9)
    t9.grid(column=4,row=5)

    win.mainloop()

if __name__=="__main__":
    main()