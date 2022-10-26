from tkinter import *

arr=[[0,6,2],[3,5,8],[4,6,7]]
arr_squares=[[],[],[],[],[],[]]
arr_circles=[[],[],[],[],[],[]]
arr_pieces=[]
arr_numbers=[[],[],[]]
red="#a42b39"
background_color="black"
foreground_color= "#00008b"
foreground_2nd_color= "#EA047E"
empty_color="#312e2b"
square_stroke=4
canvas_width=700
canvas_height=600
velocity = 0.05
square_length=100
moving_period=int((square_length+square_stroke)/velocity)
moves_arr = [(0,0),(0,1),(1,1),(1,0),(0,0)]
col=[0,0,0,0,0,0,0]
counter = 1
scale =1.2
circle_scale = 12
root = Tk()
root.minsize(height=900,width=1500)
root.option_add('*Font', '20')
mylabel = Label(root, text='8 puzzle', fg=foreground_color, bg=background_color)
root.configure(background=background_color)
mylabel.pack()
color =True

def tab1():
  mylabel2 = Label(root, text='Choose one of the following three methods to solve the puzzle', fg=foreground_color, bg=background_color)
  mylabel2.pack()
  mylabel2.place(x=170, y=80)

  def tab2():
      mycanvas = Canvas(root, width=canvas_width+(square_stroke*3), height=canvas_height+(square_stroke*3),bd=0,highlightthickness=0, bg=empty_color)
      mycanvas.pack(pady=20)
      global counter

      def back():
          button4.destroy()
          mycanvas.destroy()
          buttonmove.destroy()
          tab1()

      def move(x_new,y_new ,x_old,y_old):
          x_difference=y_new-y_old
          y_difference=x_new-x_old
          for i in range(moving_period):
              mycanvas.move(arr_squares[x_old][y_old], velocity * x_difference, velocity * y_difference)
              mycanvas.move(arr_numbers[x_old][y_old], velocity * x_difference, velocity * y_difference)
              mycanvas.update()
          arr_squares[x_new][y_new] = arr_squares[x_old][y_old]
          arr_numbers[x_new][y_new] = arr_numbers[x_old][y_old]
          arr_squares[x_old][y_old] = 0
          arr_numbers[x_old][y_old] = 0

      def next():
          move( moves_arr[counter - 1][0] , moves_arr[counter - 1][1],
                moves_arr[counter][0] , moves_arr[counter][1])
          counter += 1

      def previous():
          move( moves_arr[counter][0] , moves_arr[counter][1],
                moves_arr[counter - 1][0] , moves_arr[counter - 1][1])
          counter -= 1

      def auto():
          while counter < len(moves_arr):
              next()
      def draw (i, j ):
          global color
          x = i * (2 + square_length)
          starx = i * (2 + square_length) + (20)
          y = (5-col[i]) * (2+square_length)
          stary = (5-col[i]) * (2+square_length) +(17)
          if(color):
              mycanvas.create_oval(x + 1, y + 1, x + (square_length) - 2, y + (square_length) - 2, fill=red,width="0")
              mycanvas.create_oval(x + circle_scale, y + circle_scale, x + (square_length) - circle_scale - 1,y + (square_length) - circle_scale - 1, fill="#80222d", outline="black",width="0", )
              mycanvas.create_polygon(starx + (25 * scale), stary + (2.5 * scale), starx + (10 * scale),
                                      stary + (49.5 * scale), starx + (47.5 * scale), stary + (19.5 * scale),
                                      starx + (2.5 * scale), stary + (19.5 * scale), starx + (40 * scale),
                                      stary + (49.5 * scale), fill="", outline=red, width="2")
          else:
              mycanvas.create_oval(x + 1, y + 1, x + (square_length) - 2, y + (square_length) - 2, fill="#e3c559",width="0")
              mycanvas.create_oval(x + circle_scale, y + circle_scale, x + (square_length) - circle_scale - 1,y + (square_length) - circle_scale - 1, fill="#c1bc2f", outline="black",width="0", )
              mycanvas.create_polygon(starx + (25 * scale), stary + (2.5 * scale), starx + (10 * scale),
                                      stary + (49.5 * scale), starx + (47.5 * scale), stary + (19.5 * scale),
                                      starx + (2.5 * scale), stary + (19.5 * scale), starx + (40 * scale),
                                      stary + (49.5 * scale), fill="", outline="#e3c559", width="2")
          color = not color
          col[i]+=1
      y1=0
      for i in range (0,6):
          y = i * (2+square_length)
          for j in range(0,7):
              x=j * (2+square_length)
              arr_squares[i].append(mycanvas.create_rectangle(x , y , x + (square_length) , y +(square_length) , outline=foreground_color, fill=foreground_color ,width = "2"))
              arr_circles[i].append(mycanvas.create_oval(x +1 , y +1 , x + (square_length) -2, y +(square_length) -2 ,fill="black" ,width = "0"))
              mycanvas.tag_bind(arr_circles[i][j],"<Button-1>",lambda x: draw(x.x//100,x.y//100))
      #mycanvas.move(arr_pieces[0], )
      button1.destroy()
      button2.destroy()
      button3.destroy()
      mylabel2.destroy()



  button1 = Button(root, text='BFS', command=tab2, bg=background_color, fg=foreground_color, height = 2, width = 8)
  button1.place(x=100,y=250)
  button2 = Button(root, text='DFS', command=tab2, bg=background_color, fg=foreground_color, height=2, width=8)
  button2.place(x=400, y=250)
  button3 = Button(root, text='A*', command=tab2, bg=background_color, fg=foreground_color, height=2, width=8)
  button3.place(x=700, y=250)

tab1()
root.mainloop()
