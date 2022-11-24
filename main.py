import random
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import os
from numerize import numerize

checkone=False
checktwo=False
def Runfor(times,numberofguesses,positive ,negative,options,multicorrect=False):
    n=0
    if multicorrect:
        n=options
    else:
        n=1
    answerkey = list((random.sample(range(1, options + 1), random.randint(1, n))) for _ in range(numberofguesses + 1))
    if C2Var.get()==1:
        f = open('rawdata.txt', "w")
        f.close()
        f = open('rawdata.txt', "a")
    if C1Var.get()==1:
        positivescorelist=[]
        negativescorelist=[]
        positiveperlist = []
        negativeperlist = []
        positiveperlist.append(0)
        negativeperlist.append(0)
        positivescorelist.append(0)
        negativescorelist.append(0)
    nofnegative = 0
    nofpositive = 0
    nofzero = 0
    scoresum=0
    scoremax=float('-inf')
    scoremin =float('inf')
    for x in range(times):
        score=0
        rawresultlist=[]
        for i in range(0,numberofguesses):
            if (random.sample(range(1, options + 1), random.randint(1, n))) == answerkey[i]:
                score+=positive
                if C2Var.get()==1:
                    rawresultlist.append(f"+{positive}")
            else:
                score-= abs(negative)
                if C2Var.get() ==1:
                    rawresultlist.append(f"-{abs(negative)}")
        if score==0:
            nofzero +=1

        elif score > 0:
            nofpositive += 1
        else:
            nofnegative +=1
        if C2Var.get() == 1:
            f.write(f"{str(score)}  {rawresultlist}\n")
        if score>scoremax:
            scoremax=score
        if score<scoremin:
            scoremin=score
        scoresum+=score
        positiveper = (nofpositive/(x+1))*100
        negativeper = (nofnegative/(x+1))*100
        if C1Var.get()==1:
            positivescorelist.append(nofpositive)
            negativescorelist.append(nofnegative)
            positiveperlist.append(positiveper)
            negativeperlist.append(negativeper)
    zeroper = (nofzero / times) * 100
    if C2Var.get()==1:
        f.write(f"\n\nAnswer Key - {answerkey}")
        f.close()

    Extra = tkinter.Toplevel(top)


    text5 = f"No of positive results -{nofpositive} \nAverage Probability of Positive results {round(positiveper,4)}%"
    t5 = tkinter.Label(Extra, text=text5)
    t5.pack()
    text7 = f"No of Zero results -{nofzero} \nAverage Probability of Positive results {round(zeroper,4)}%"
    t7 = tkinter.Label(Extra, text=text7)
    t7.pack()

    spaceextra = tkinter.Label(Extra, text="")
    spaceextra.pack()

    text6 = f"No of negative results -{nofnegative} \nAverage Probability of Negative results {round(negativeper,4)}%"
    t6 = tkinter.Label(Extra, text=text6)
    t6.pack()

    spaceextra = tkinter.Label(Extra, text="")
    spaceextra.pack()



    text8 = f"Average Score : {round(scoresum/times,2)}"
    t8 = tkinter.Label(Extra, text=text8)
    t8.pack()
    text9 = f"Minimum Score : {scoremin}"
    t9 = tkinter.Label(Extra, text=text9)
    t9.pack()
    text10 = f"Maximum Score : {scoremax}"
    t10 = tkinter.Label(Extra, text=text10)
    t10.pack()

    def b2command():
        os.startfile('rawdata.txt')

    b2 = tkinter.Button(Extra, text="View raw results", command=b2command)
    b2.pack()



    if C1Var.get() == 1:
        if multicorrect:
            p = 'Multicorrect'
        else:
            p='Single Correct'
        fig,((ax1,ax2),(ax4,ax3))= plt.subplots(2,2,figsize=(8,8))
        fig.suptitle(f'Graphical Representation of (+{positive},-{abs(negative)}) with {options} options,{p}')
        fig.set_size_inches(15,9)

        a = np.arange(0,times+1)
        z = [zeroper]*(times+1)

        items=(positiveper,negativeper,zeroper)
        labels=("Positive%","Negative%","Zero%")
        myexplode = [0.1, 0.1, 0.1]

        ax1.set_ylim(-5,105)
        ax2.set_ylim(-5, 105)
        ax1.set_xlabel("Times Simulation is Run")
        ax2.set_xlabel("Times Simulation is Run")
        ax4.set_xlabel("Times Simulation is Run")
        ax1.set_ylabel("% of results")
        ax4.set_ylabel("No of Scores")


        plt.subplots_adjust(left=0.07,
                            bottom=0.064,
                            right=0.967,
                            top=0.926,
                            wspace=0.12,
                            hspace=0.19)

        ax1.plot(a,positiveperlist,color='green',label=f"% of Positive results-{round(positiveper,3)}")
        ax1.plot(a,z,color="Blue",ls="dashed",label=f"% of Zero Results-{round(zeroper,3)}")
        ax2.plot(a,negativeperlist,color='red',label=f"% of Negative results-{round(negativeper,3)}")
        ax4.plot(a,positivescorelist,color='green',label='No of positive scores')
        ax4.plot(a,negativescorelist,color='red',label='No of negative scores')
        ax3.pie(items,labels=labels,explode=myexplode,shadow=True,autopct='%1.1f%%')



        ax1.legend()
        ax2.legend()
        ax4.legend()

        plt.show()



top = tkinter.Tk()



top.title("Guess Simulator")

t1= tkinter.Label(top,text="Number of times you want to run this simulation-")
t1.pack()
e1 = tkinter.Entry(top)
e1.pack()

updatelabel1 = tkinter.Label(top,text="",fg="red")
updatelabel1.pack()


spacetop = tkinter.Label(top,text="")
spacetop.pack()


t2= tkinter.Label(top,text="Number of Guesses in each simulation-")
t2.pack()
e2 = tkinter.Entry(top)
e2.pack()

updatelabel2=tkinter.Label(top,text="",fg="red")
updatelabel2.pack()

t3 = tkinter.Label(top,text='How many options in each question').pack()

rVar = tkinter.IntVar(None,"4")
r1 = tkinter.Radiobutton(top,text = "2",variable =rVar, value=2).pack()
r2 = tkinter.Radiobutton(top,text = "3",variable =rVar, value=3).pack()
r3 = tkinter.Radiobutton(top,text = "4",variable =rVar, value=4).pack()
r4 = tkinter.Radiobutton(top,text = "5",variable =rVar, value=5).pack()

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

C3Var = tkinter.BooleanVar()
c3 = tkinter.Checkbutton(top,text = "Multicorrect(Each option can have muliple options as answers)",variable =C3Var, onvalue=True, offvalue =False)
c3.pack()

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
    if checkone and checktwo:
        Runfor(int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()),rVar.get(),C3Var.get())


b1 = tkinter.Button(top,text="GO",command=b1command)
b1.pack()


def Updatetextfunction():
    global checkone
    global checktwo
    try:
        updatelabel1['text']= numerize.numerize(int(e1.get()))
        checkone=True

    except:
        updatelabel1['text']= "Please enter an integer"
        checkone = False

    try:
        updatelabel2['text']=int(e2.get())
        checktwo=True
    except:
         updatelabel2['text']= "Please enter an integer"
         checktwo=False
    top.after(500,Updatetextfunction)


Updatetextfunction()

top.mainloop()

