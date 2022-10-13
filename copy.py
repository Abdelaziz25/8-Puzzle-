from tkinter import *

arr=[[1,0,2],[3,5,8],[4,6,7]]
arr_squares=[[],[],[]]
arr_numbers=[[],[],[]]
background_color="black"
foreground_color= "#0000C3"
foreground_2nd_color= "#EA047E"
empty_color="grey"
square_stroke=4
canvas_width=300
canvas_height=300
velocity = 0.05
square_length=100
moving_period=int((square_length+square_stroke)/velocity)

root = Tk()
root.minsize(height=500,width=900)
root.option_add('*Font', '20')



mylabel = Label(root, text='8 puzzle', fg=foreground_color, bg=background_color)
root.configure(background=background_color)
mylabel.pack()



def tab1():
  mylabel2 = Label(root, text='Choose one of the following three methods to solve the puzzle', fg=foreground_color, bg=background_color)
  mylabel2.pack()
  mylabel2.place(x=170, y=80)

  def tab2():
      mycanvas = Canvas(root, width=canvas_width+(square_stroke*3), height=canvas_height+(square_stroke*3),bd=0,highlightthickness=0, bg=empty_color)
      mycanvas.pack(pady=20)
      def move():
          ##right
          for i in range(moving_period):
              mycanvas.move(arr_squares[0][0], velocity, 0)
              mycanvas.move(arr_numbers[0][0], velocity, 0)
              mycanvas.update()
          """
          ##left
          for i in range(moving_period):
              mycanvas.move(arr_squares[0][0], -velocity, 0)
              mycanvas.move(arr_numbers[0][0], -velocity, 0)
              mycanvas.update()
          ##down
          for i in range(moving_period):
              mycanvas.move(arr_squares[0][0], 0, velocity)
              mycanvas.move(arr_numbers[0][0], 0, velocity)
              mycanvas.update()
          ##up
          for i in range(moving_period):
              mycanvas.move(arr_squares[0][0], 0, -velocity)
              mycanvas.move(arr_numbers[0][0], 0, -velocity)
              mycanvas.update()
          """

      y1=0
      for i in range (0,3):
          y = pow(2,i)*50+y1+square_stroke/2
          x1=0
          for j in range(0,3):
              if(arr[i][j]!=0):
                  #EA047E
                  x=pow(2,j)*50+x1+square_stroke/2
                  if(arr[i][j]%2==0):
                      arr_squares[i].append(mycanvas.create_rectangle(x - (square_length/2)+(j*square_stroke)  , y - (square_length/2)+(i*square_stroke) , x + (square_length/2)+(j*square_stroke) , y + (square_length/2)+(i*square_stroke) , outline=foreground_2nd_color, fill=background_color, width=square_stroke))
                      arr_numbers[i].append(mycanvas.create_text(x+(j*square_stroke) , y+(i*square_stroke) , text=arr[i][j], fill=foreground_2nd_color, font=('Helvetica 40 bold')))
                  else:
                      arr_squares[i].append(mycanvas.create_rectangle(x - (square_length/2)+(j*square_stroke) , y - (square_length/2)+(i*square_stroke) , x + (square_length/2)+(j*square_stroke) , y + (square_length/2)+(i*square_stroke) , outline=foreground_color, fill=background_color, width=square_stroke))
                      arr_numbers[i].append(mycanvas.create_text(x+(j*square_stroke) , y+(i*square_stroke) , text=arr[i][j], fill=foreground_color, font=('Helvetica 40 bold')))
              x1=50
          y1=50

      buttonmove = Button(root, text='next', command=move, bd =4, bg=background_color, fg=foreground_color, height=2, width=8)
      buttonmove.place(x=400, y=400)

      button1.destroy()
      button2.destroy()
      button3.destroy()
      mylabel2.destroy()
      def back():
          button4.destroy()
          mycanvas.destroy()
          buttonmove.destroy()
          tab1()

      button4=Button(root, text='Back', command=back, bg=background_color, fg=foreground_color, height=2, width=8)
      button4.place(x=100,y=300)


  button1 = Button(root, text='BFS', command=tab2, bg=background_color, fg=foreground_color, height = 2, width = 8)
  button1.place(x=100,y=250)
  button2 = Button(root, text='DFS', command=tab2, bg=background_color, fg=foreground_color, height=2, width=8)
  button2.place(x=400, y=250)
  button3 = Button(root, text='A*', command=tab2, bg=background_color, fg=foreground_color, height=2, width=8)
  button3.place(x=700, y=250)

tab1()
root.mainloop()
