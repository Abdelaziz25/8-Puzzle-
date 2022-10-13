from tkinter import *
root = Tk()
root.minsize(height=500,width=900)
root.option_add('*Font', '20')
mylabel = Label(root,text='8 puzzle')
mylabel.pack()
arr=[[1,0,2],[3,5,8],[4,6,7]]
def tab1():
  mylabel2 = Label(root, text='Choose one of the following three methods to solve the puzzle')
  mylabel2.pack()
  mylabel2.place(x=170, y=80)

  def tab2():
      mycanvas = Canvas(root, width=300, height=300, bg="wheat")
      mycanvas.pack(pady=20)
      y1=0
      for i in range (0,3):
          y = pow(2,i)*50+y1
          x1=0
          for j in range(0,3):
             if(arr[i][j]!=0):
                 x=pow(2,j)*50+x1
                 mycanvas.create_text(x, y, text=arr[i][j], fill="blue", font=('Helvetica 15 bold'))
             x1=50
          y1=50
      mycanvas.create_line(0,100,300,100,fill="black")
      mycanvas.create_line(0, 200, 300, 200, fill="black")
      mycanvas.create_line(100, 0, 100, 300, fill="black")
      mycanvas.create_line(200, 0, 200, 300, fill="black")
      button1.destroy()
      button2.destroy()
      button3.destroy()
      mylabel2.destroy()
      def back():
          button4.destroy()
          mycanvas.destroy()
          tab1()
      button4=Button(root, text='Back', command=back, bg="black", fg="white", height=2, width=8)
      button4.place(x=100,y=300)
  button1=Button(root,text='BFS',command=tab2,bg="black",fg="white",height = 2, width = 8)
  button1.place(x=100,y=250)
  button2 = Button(root, text='DFS', command=tab2, bg="black", fg="white", height=2, width=8)
  button2.place(x=400, y=250)
  button3 = Button(root, text='A*', command=tab2, bg="black", fg="white", height=2, width=8)
  button3.place(x=700, y=250)

tab1()
root.mainloop()
