import random
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import os



answerkey =(4,
1,
4,
2,
1,
2,
4,
4,
4,
3,
2,
3,
1,
1,
3,
1,
1,
1,
2,
2,
3,
2,
3,
1,
1,
3,
1,
2,
4,
3,
3,
1,
3,
1,
4,
2,
2,
4,
2,
3,
2,
1,
2,
2,
1,
2,
4,
3,
3,
1,
2,
2,
3,
1,
3,
4,
2,
3,
4,
3,
4,
1,
1,
2,
2,
4,
1,
2,
3,
1,
2,
3,
4,
4,
4,
2,
4,
1,
4,
3,
3,
4,
1,
2,
1,
3,
3,
2,
4,
3,
3,
1,
3,
4,
1,
4,
4,
1,
2,
4,
4,
3,
3,
3,
3,
4,
2,
4,
2,
1,
3,
4,
3,
4,
1,
3,
3,
2,
1,
4,
)



def Runfor(times,numberofguesses,positive ,negative):
    if C2Var.get()==1:
        f = open('rawdata.txt', "w")
        f.close()
        f = open('rawdata.txt', "a")
    positiveperlist = [None]*times
    negativeperlist = [None]*times
    nofnegative = 0
    nofpositive = 0
    nofzero = 0
    positiveperlist[0] = 0
    negativeperlist[0] = 0
    for x in range(1,times):
        score=0
        rawresultlist=[]
        for i in range(0,numberofguesses):
            if (random.randint(1,4) == answerkey[i]):
                score+=positive
                if C2Var.get()==1:
                    rawresultlist.append(f"+{positive}")
            else:
                score-= abs(negative)
                if C2Var.get() ==1:
                    rawresultlist.append(f"-{abs(negative)}")
        if score==0:
            nofzero +=1
            nofpositive+=1
        elif score > 0:
            nofpositive += 1
        else:
            nofnegative +=1
        if C2Var.get() == 1:
            f.write(f"{str(score)}  {rawresultlist}\n")
        positiveper = (nofpositive/(x+1))*100
        negativeper = (nofnegative/(x+1))*100
        positiveperlist[x] = positiveper
        negativeperlist[x] = negativeper
    if C2Var.get()==1:
        f.close()

    print("No of negative results -",nofnegative)
    print("No of positive results -",nofpositive)
    print("No of zero results -", nofzero)
    Extra = tkinter.Toplevel(top)


    text5 = f"No of positive results -{nofpositive} \nAverage Probability of Positive results {round(positiveperlist[-1],4)}%"
    t5 = tkinter.Label(Extra, text=text5)
    t5.pack()

    spaceextra = tkinter.Label(Extra, text="")
    spaceextra.pack()

    text6 = f"No of negative results -{nofnegative} \nAverage Probability of Negative results {round(negativeperlist[-1],4)}%"
    t6 = tkinter.Label(Extra, text=text6)
    t6.pack()

    spaceextra = tkinter.Label(Extra, text="")
    spaceextra.pack()

    text7 = f"No of zero results -{nofzero}"
    t7 = tkinter.Label(Extra, text=text7)
    t7.pack()

    def b2command():
        os.startfile('rawdata.txt')

    b2 = tkinter.Button(Extra, text="View raw results", command=b2command)
    b2.pack()



    if C1Var.get() == 1:
        a = np.arange(0, times)
        plt.ylim(0, 100)
        plt.title("Percentage of +ve and -ve results")
        plt.ylabel("Percentage(%)")
        plt.xlabel("Times Simulation is run")
        plt.plot(a, positiveperlist, color="green", label="Positive Results")
        plt.plot(a, negativeperlist, color="red", label="Negative Results")
        plt.legend()
        plt.show()



top = tkinter.Tk()



top.title("Guess Simulator")

t1= tkinter.Label(top,text="Number of times you want to run this simulation-")
t1.pack()
e1 = tkinter.Entry(top)
e1.pack()

spacetop = tkinter.Label(top,text="")
spacetop.pack()

t2= tkinter.Label(top,text="Number of Guesses in each simulation-")
t2.pack()
e2 = tkinter.Entry(top)
e2.pack()

spacetop = tkinter.Label(top,text="")
spacetop.pack()

t3= tkinter.Label(top,text="Marks for correct answer-")
t3.pack()
e3 = tkinter.Entry(top,text="4")
e3.insert(0,"4")
e3.pack()

spacetop = tkinter.Label(top,text="")
spacetop.pack()

t4= tkinter.Label(top,text="Negative marking-")
t4.pack()
e4 = tkinter.Entry(top,text="-1")
e4.insert(0,"-1")
e4.pack()

spacetop = tkinter.Label(top,text="")
spacetop.pack()

C1Var = tkinter.IntVar()
c1 = tkinter.Checkbutton(top,text = "Draw Graph",variable =C1Var, onvalue=1, offvalue =0)
c1.pack()

C2Var = tkinter.IntVar()
c2 = tkinter.Checkbutton(top,text = "Generate raw results[WARNING-RESOURCE INTENSIVE]",variable =C2Var, onvalue=1, offvalue =0)
c2.pack()


spacetop = tkinter.Label(top,text="")
spacetop.pack()

def b1command():
    Runfor(int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()))


b1 = tkinter.Button(top,text="GO",command=b1command)
b1.pack()

top.mainloop()


