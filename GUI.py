from tkinter import *
from tkinter import messagebox

import Controller

class GUI:

    def __init__(self):
        self.controller = Controller.Controller()
        self.arr = []
        #moving
        self.arr_squares = [[], [], []]
        self.arr_numbers = [[], [], []]
        #input
        self.arr_squares2 = [[], [], []]
        self.arr_numbers2 = [[], [], []]
        self.background_color = "#242526"
        self.tile_bg_color = "black"
        self.tile_fg_color = "#0000C3"
        self.tile_2nd_fg_color = "#EA047E"
        self.foreground_color = "#1ab2ff"
        self.foreground_2nd_color = "#EA047E"
        self.empty_color = "grey"
        self.colorOnHover = "grey"
        self.square_stroke = 4
        self.canvas_width = 300
        self.canvas_height = 300
        self.velocity = 0.2
        self.square_length = 100
        self.moving_period = int((self.square_length + self.square_stroke) / self.velocity)
        self.root = Tk()
        self.root.minsize(height=500, width=900)
        self.root.option_add('*Font', '30')
        self.counter = 1
        self.moves_arr=[(0,0),(0,1),(1,1),(1,0),(0,0)]

    def changeOnHover(self, button):
        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=self.colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=self.background_color))

    def home(self):
        def random():
            self.arr = self.controller.createRandom()
            print(self.arr)
            toplabel.destroy()
            description.destroy()
            random.destroy()
            input.destroy()
            self.tab1()

        def input():
            print("i")
            toplabel.destroy()
            description.destroy()
            random.destroy()
            input.destroy()
            self.tab1()


        toplabel = Label(self.root, text='8 puzzle', fg=self.foreground_color, bg=self.background_color, font=("", 50))
        self.root.configure(background=self.background_color)
        toplabel.pack(pady=100)

        description = Label(self.root, text='Chose random for random arrangement or input to put it your self', fg=self.foreground_color, bg=self.background_color, font=("", 15))
        description.place(x=150 ,y=250)

        random = Button(self.root, text='Random', command=random, bg=self.background_color, fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        random.place(x=250, y=300)
        input = Button(self.root, text='input', command=input, bg=self.background_color, fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        input.place(x=550, y=300)

        self.changeOnHover(random)
        self.changeOnHover(input)
        self.arr = []



    def drawcanvas(self):
        self.mycanvas = Canvas(self.root, width=self.canvas_width + (self.square_stroke * 3), height=self.canvas_height + (self.square_stroke * 3),
                          bd=0, highlightthickness=0, bg=self.empty_color)
        self.mycanvas.pack(pady=20)

        y1 = 0
        for i in range(0, 3):
            y = pow(2, i) * 50 + y1 + self.square_stroke / 2
            x1 = 0
            for j in range(0, 3):
                if (self.arr[i][j] != 0):
                    # EA047E
                    x = pow(2, j) * 50 + x1 + self.square_stroke / 2
                    if (self.arr[i][j] % 2 == 0):
                        self.arr_squares[i].append(self.mycanvas.create_rectangle(x - (self.square_length / 2) + (j * self.square_stroke),
                                                                        y - (self.square_length / 2) + (i * self.square_stroke),
                                                                        x + (self.square_length / 2) + (j * self.square_stroke),
                                                                        y + (self.square_length / 2) + (i * self.square_stroke),
                                                                        outline=self.tile_2nd_fg_color,
                                                                        fill=self.tile_bg_color, width=self.square_stroke))
                        self.arr_numbers[i].append(
                            self.mycanvas.create_text(x + (j * self.square_stroke), y + (i * self.square_stroke), text=self.arr[i][j],
                                                 fill=self.tile_2nd_fg_color, font=('Helvetica 40 bold')))
                    else:
                        self.arr_squares[i].append(self.mycanvas.create_rectangle(x - (self.square_length / 2) + (j * self.square_stroke),
                                                                        y - (self.square_length / 2) + (i * self.square_stroke),
                                                                        x + (self.square_length / 2) + (j * self.square_stroke),
                                                                        y + (self.square_length / 2) + (i * self.square_stroke),
                                                                        outline=self.tile_fg_color, fill=self.tile_bg_color,
                                                                        width=self.square_stroke))
                        self.arr_numbers[i].append(
                            self.mycanvas.create_text(x + (j * self.square_stroke), y + (i * self.square_stroke), text=self.arr[i][j],
                                                 fill=self.tile_fg_color, font=('Helvetica 40 bold')))
                else:
                    self.arr_squares[i].append(0)
                    self.arr_numbers[i].append(0)

                x1 = 50
            y1 = 50


    def drawtextInput(self):
        self.arr = [[0,0,0],[0,0,0],[0,0,0]]
        self.mycanvas = Canvas(self.root, width=self.canvas_width + (self.square_stroke * 3), height=self.canvas_height + (self.square_stroke * 3),
                          bd=0, highlightthickness=0, bg=self.empty_color)
        self.mycanvas.pack(pady=20)

        y1 = 0
        self.inputEntries = []

        def search_for_index(x):
            for i in range(0, 3):
                for j in range(0, 3):
                    if(self.arr_numbers2[i][j].get()==x):
                        print(i)
                        print(j)
                        return i,j

        #e = Entry(self.mycanvas,width=3 , font=('Helvetica 40 bold'), justify='center',  fg=self.foreground_color, borderwidth=0)
        #e.place(x=216, y=25)
        for i in range(0, 3):
            y = pow(2, i) * 50 + y1 + self.square_stroke / 2
            x1 = 0

            def callback(temp):
                print(temp)
                temp2=int(temp)
                i,j = search_for_index(temp)
                self.inputEntries[i][j].configure({"background": "black"})
                if temp2%2==1:
                    self.mycanvas.itemconfig(self.arr_squares2[i][j], outline=self.tile_fg_color)
            self.inputEntries.append([])
            for j in range(0, 3):
                    self.arr_numbers2[i].append(StringVar())
                    self.inputEntries[i].append(Entry(self.mycanvas,width=3 , font=('Helvetica 40 bold'), justify='center',
                                                 fg=self.tile_fg_color, borderwidth=0, textvariable=self.arr_numbers2[i][j]))
                    self.inputEntries[i][j].place(x=7+104*j, y = 10+104*i, height= 85)

                    self.arr_numbers2[i][j].trace("w", lambda name, index, mode, sv=self.arr_numbers2[i][j]: callback(sv.get()))

                    x = pow(2, j) * 50 + x1 + self.square_stroke / 2
                    self.arr_squares2[i].append(self.mycanvas.create_rectangle(x - (self.square_length / 2) + (j * self.square_stroke),
                                                                        y - (self.square_length / 2) + (i * self.square_stroke),
                                                                        x + (self.square_length / 2) + (j * self.square_stroke),
                                                                        y + (self.square_length / 2) + (i * self.square_stroke),
                                                                        outline=self.tile_2nd_fg_color,
                                                                       fill=self.tile_bg_color, width=self.square_stroke))
                    """  
                    self.arr_numbers[i].append(
                         self.mycanvas.create_text(x + (j * self.square_stroke), y + (i * self.square_stroke), text=self.inputEntries[i][j].get(),
                                fill=self.foreground_2nd_color, font=('Helvetica 40 bold')))
                    """

                    x1 = 50
            y1 = 50

    def tab1(self):
        isInput = False
        def back():
            self.mycanvas.destroy()
            BFS.destroy()
            DFS.destroy()
            As.destroy()
            backB.destroy()
            if isInput:
                for i in range(3):
                    for j in range(3):
                        self.inputEntries[i][j].destroy()
                    self.arr_numbers2[i].clear()
            self.home()
        def damage():
            BFS.destroy()
            DFS.destroy()
            As.destroy()
            backB.destroy()
        def search(s):
            if isInput:
                isValid = True
                for i in range(3):
                    if isValid == False:
                        break
                    for j in range(3):
                        data =self.inputEntries[i][j].get()
                        if data == '':
                            self.arr[i][j] = 0
                        elif not data.isnumeric():
                            isValid = False
                            break
                        else:
                            self.arr[i][j] = int(data)

                if isValid:
                    isValid = self.controller.check(self.arr)
                    print(isValid)
                    if isValid:
                      damage()
                      self.tab2()
                if not isValid:
                    messagebox.showerror("Error", "Not Valid Input. Reenter the number")
            else:
                damage()
                self.tab2()





            print(s)
            print(self.arr)

        BFS = Button(self.root, text='BFS', bg=self.background_color, command=lambda:[search("BFS")], fg=self.foreground_color, height=2, width=8,font=("", 15), relief=RAISED)
        BFS.place(x=100, y=375)
        DFS = Button(self.root, text='DFS', bg=self.background_color, command=lambda:[search("DFS")], fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        DFS.place(x=400, y=375)
        As = Button(self.root, text='A*', bg=self.background_color, command=lambda:[search("As")], fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        As.place(x=700, y=375)
        backB = Button(self.root, text='Back', command=back, bg=self.background_color, fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        backB.place(x=100, y=50)
        self.changeOnHover(backB)
        self.changeOnHover(BFS)
        self.changeOnHover(DFS)
        self.changeOnHover(As)

        if len(self.arr) != 0 :  #random
            self.drawcanvas()
        else:
            isInput = True
            self.drawtextInput()




    def tab2(self):
        def home():
            self.mycanvas.destroy()
            PRev.destroy()
            Auto.destroy()
            Next.destroy()
            backc.destroy()
            self.home()


        def move(  x_old, y_old ,x_new, y_new):
            print(  x_old, y_old,"to" ,x_new, y_new,)
            x_difference = (y_new - y_old )
            y_difference = (x_new - x_old)
            for i in range(self.moving_period):
                self.mycanvas.move(self.arr_squares[x_old][y_old], self.velocity * x_difference, self.velocity * y_difference)
                self.mycanvas.move(self.arr_numbers[x_old][y_old], self.velocity * x_difference, self.velocity * y_difference)
                self.mycanvas.update()
            self.arr_squares[x_new][y_new] = self.arr_squares[x_old][y_old]
            self.arr_numbers[x_new][y_new] = self.arr_numbers[x_old][y_old]
            self.arr_squares[x_old][y_old] = 0
            self.arr_numbers[x_old][y_old] = 0

        def next():
            if(self.counter<len(self.moves_arr)):
                print("b5af 2nsaky")
                move(self.moves_arr[self.counter][0], self.moves_arr[self.counter][1],
                     self.moves_arr[self.counter - 1][0], self.moves_arr[self.counter - 1][1])
                self.counter += 1

        def previous():
            if(self.counter>1):
                move(self.moves_arr[self.counter - 2][0], self.moves_arr[self.counter- 2][1],
                    self.moves_arr[self.counter -1][0], self.moves_arr[self.counter -1 ][1])
                self.counter -= 1
        def auto():
            while self.counter < len(self.moves_arr):
                next()

        self.mycanvas.destroy()
        for i in range(3):
                self.arr_squares[i].clear()
        self.drawcanvas()

        PRev = Button(self.root, text='Prev', bg=self.background_color, command=previous,
                     fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        PRev.place(x=100, y=375)
        Auto = Button(self.root, text='Auto', bg=self.background_color, command=auto,
                     fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        Auto.place(x=400, y=375)
        Next = Button(self.root, text='Next', bg=self.background_color, command=next,
                    fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        Next.place(x=700, y=375)
        backc = Button(self.root, text='Home',command=home, bg=self.background_color, fg=self.foreground_color,
                       height=2, width=8, font=("", 15), relief=RAISED)
        backc.place(x=100, y=50)




