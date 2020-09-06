from tkinter import *
root = Tk()
root.title("calC")

inp = Entry(root,width=45,borderwidth=3)
#inp.grid(row=0,column=0,columnspan=3,padx=3,pady=3)
inp.place(x=0,y=0,width=300,height=25)
##########

b1 = Button(root,text="1",padx=40,pady=20)
b2 = Button(root,text="2",padx=40,pady=20)
b3 = Button(root,text="3",padx=40,pady=20)
b4 = Button(root,text="4",padx=40,pady=20)
b5 = Button(root,text="5",padx=40,pady=20)
b6 = Button(root,text="6",padx=40,pady=20)
b7 = Button(root,text="7",padx=40,pady=20)
b8 = Button(root,text="8",padx=40,pady=20)
b9 = Button(root,text="9",padx=40,pady=20)
b0 = Button(root,text="0",padx=40,pady=20)
b_multiply =  Button(root,text="x",padx=40,pady=20)
b_subtract =  Button(root,text="-",padx=40,pady=20)
b_division =  Button(root,text="/",padx=40,pady=20)
b_equal =  Button(root,text="=",padx=40,pady=20)
b_add =  Button(root,text="+",padx=40,pady=20)
b_period = Button(root,text=".",padx=40,pady=20)
b_clear = Button(root,text="Clear",padx=30)
b_reset = Button(root,text="CE",padx=40,pady=20)


###########
b_clear.grid(row=0,column=3) 

b7.grid(row=1 ,column=0)
b8.grid(row=1 ,column=1)
b9.grid(row=1 ,column=2)
b_multiply.grid(row=1 ,column=3)

b4.grid(row=2 ,column=0)
b5.grid(row=2 ,column=1)
b6.grid(row=2 ,column=2)
b_subtract.grid(row=2 ,column=3)

b1.grid(row=3 ,column=0)
b2.grid(row=3 ,column=1)
b3.grid(row=3 ,column=2)
b_add.grid(row=3,column=3)


b_reset.grid(row=4,column=0)
b0.grid(row=4, column=1)
b_period.grid(row=4, column=2)
b_equal.grid(row=4, column=3)
root.mainloop()


