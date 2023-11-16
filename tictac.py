from tkinter import*
from tkinter import messagebox #pazinojumi. ietekumi.
mansLogs=Tk() #loga objekts
mansLogs.title("Tictactoe")

speletajsX=True #KURAM SPELETAJAM KARTA SPELET , LIKS KRUSTINUS
count=0 #Aizpildito rutinu skaits

def btnClick(button): #padod visu pogu
    global speletajsX,count#kādi mainīgie tiks izmantoti visaa programma
    if button["text"]==''and speletajsX==True:#spele x speletajs
        button["text"]="X"#maina uz X
        speletajsX=False
        count+=1#palielina rutinu skaitu
       
    elif button['text']==''and speletajsX==False: #mainās spēlētāji
        button['text']='O'
        speletajsX=True
        count+=1
       
    else:
        messagebox.showerror("Tictactoe","Šeit jau kāds ir uzlicis")
    return


btn1=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn1))
btn2=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn2))
btn3=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn3))
btn4=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn4))
btn5=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn5))
btn6=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn6))
btn7=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn7))
btn8=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn8))
btn9=Button(mansLogs,text='',width=6,height=3,font=("Helvica", 24),command=lambda:btnClick(btn9))



btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)



def checkWinner():
    global winner
    winner==False #noteiks ja bus neizskirts
    if (btn1["text"]=='X' and btn2["text"]=='X'and btn3["text"=='X'] or btn1["text"]=='X' and btn4["text"]=='X'and btn7["text"=='X']or btn1["text"]=='X' and btn5["text"]=='X'and btn9["text"=='X'] or btn2["text"]=='X' and btn5["text"]=='X'and btn8["text"=='X'] or btn3["text"]=='X' and btn5["text"]=='X'and btn7["text"=='X'] or btn3["text"]=='X' and btn6["text"]=='X'and btn9["text"=='X'] or btn4["text"]=='X' and btn5["text"]=='X'and btn6["text"=='X'] or btn7["text"]=='X' and btn8["text"]=='X'and btn9["text"=='X']):
        winner==True
       
        messagebox.showinfo("Tictactoe","SpeletajsX ir uzvarētājs")
    elif (btn1["text"]=='O' and btn2["text"]=='O'and btn3["text"=='O'] or btn1["text"]=='O' and btn4["text"]=='O'and btn7["text"=='O']or btn1["text"]=='O' and btn5["text"]=='O'and btn9["text"=='O'] or btn2["text"]=='O' and btn5["text"]=='O'and btn8["text"=='O'] or btn3["text"]=='O' and btn5["text"]=='O'and btn7["text"=='O'] or btn3["text"]=='O' and btn6["text"]=='O'and btn9["text"=='O'] or btn4["text"]=='O' and btn5["text"]=='O'and btn6["text"=='O'] or btn7["text"]=='O' and btn8["text"]=='O'and btn9["text"=='O']):
        winner==False
    
        messagebox.showinfo("Tictactoe","SpeletajsO ir uzvarētājs")
    elif count==9 and winner==False:
        messagebox.showinfo("Tictactoe","Neizšķirts")



mansLogs.mainloop()