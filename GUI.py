from tkinter import *
from tkinter import messagebox

import Controller

class GUI:

    def __init__(self):
        self.isInput = False
        self.controller = Controller.Controller()
        self.arr = [[0,0,0],[0,0,0],[0,0,0]]
        self.method = "DFS"
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
        self.mycanvas2 = Canvas()


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
            self.isInput = False
            self.tab1()

        def input():
            print("i")
            toplabel.destroy()
            description.destroy()
            random.destroy()
            input.destroy()
            self.isInput = True
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
        self.arr = [[0,0,0],[0,0,0],[0,0,0]]



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
        self.mycanvas = Canvas(self.root, width=self.canvas_width + (self.square_stroke * 3), height=self.canvas_height + (self.square_stroke * 3),
                          bd=0, highlightthickness=0, bg=self.empty_color)
        self.mycanvas.pack(pady=20)

        y1 = 0
        self.inputEntries = []

        def search_for_index(x):
            for i in range(0, 3):
                for j in range(0, 3):
                    if(self.arr_numbers2[i][j].get()==x):
                        return i,j

        for i in range(0, 3):
            y = pow(2, i) * 50 + y1 + self.square_stroke / 2
            x1 = 0

            def callback(temp):
                print(temp)
                i,j = search_for_index(temp)
                if temp.isnumeric():
                    temp2 = int(temp)
                    if(temp2!=0):
                        self.inputEntries[i][j].configure({"background": "black"})
                        if temp2%2==1:
                            self.mycanvas.itemconfig(self.arr_squares2[i][j], outline=self.tile_fg_color)
                            self.inputEntries[i][j].configure({"fg": self.tile_fg_color})
                        else:
                            self.mycanvas.itemconfig(self.arr_squares2[i][j], outline=self.tile_2nd_fg_color)
                            self.inputEntries[i][j].configure({"fg": self.tile_2nd_fg_color})

                for i in range(0, 3):
                    for j in range(0, 3):
                        if(self.arr_numbers2[i][j].get()==""):
                            self.inputEntries[i][j].configure({"background": "white"})
                            self.mycanvas.itemconfig(self.arr_squares2[i][j], outline=self.tile_2nd_fg_color)
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
                x1 = 50
            y1 = 50

        for i in range(0, 3):
            for j in range(0, 3):
                if (self.arr_numbers2[i][j].get().isnumeric()):
                    self.inputEntries[i][j].configure({"background": "black"})
                    if int(self.arr_numbers2[i][j].get()) % 2 == 1:
                        self.mycanvas.itemconfig(self.arr_squares2[i][j], outline=self.tile_fg_color)
                        self.inputEntries[i][j].configure({"fg": self.tile_fg_color})
                    else:
                        self.mycanvas.itemconfig(self.arr_squares2[i][j], outline=self.tile_2nd_fg_color)
                        self.inputEntries[i][j].configure({"fg": self.tile_2nd_fg_color})



    def tab1(self):
        def back():
            self.mycanvas.destroy()
            BFS.destroy()
            DFS.destroy()
            As.destroy()
            backB.destroy()
            self.arr_squares = [[], [], []]
            self.arr_numbers = [[], [], []]
            if self.isInput:
                for i in range(3):
                    for j in range(3):
                        self.inputEntries[i][j].destroy()
                    self.arr_numbers2[i].clear()
                self.inputEntries = []
            self.home()
        def damage():
            BFS.destroy()
            DFS.destroy()
            As.destroy()
            backB.destroy()
            self.mycanvas.destroy()
            for i in range(3):
                self.arr_squares[i].clear()
            """
            if self.isInput:
                for i in range(3):
                    for j in range(3):
                        self.inputEntries[i][j].destroy()
                    self.arr_numbers2[i].clear()
                self.inputEntries = []
            """

        def search(s):
            self.method = s
            if self.isInput:
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

        if not self.isInput :  #random
            self.drawcanvas()
        else:
            self.drawtextInput()




    def tab2(self):

        self.drawcanvas()



        def back():
            self.mycanvas.destroy()
            self.arr_squares = [[], [], []]
            self.arr_numbers = [[], [], []]
            PRev.destroy()
            Auto.destroy()
            Next.destroy()
            backc.destroy()
            home.destroy()
            self.mycanvas2.destroy()
            self.tab1()
        def gotohome():
            self.mycanvas.destroy()
            self.arr_squares = [[], [], []]
            self.arr_numbers = [[], [], []]
            PRev.destroy()
            Auto.destroy()
            Next.destroy()
            backc.destroy()
            home.destroy()
            self.mycanvas2.destroy()
            self.arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            if self.isInput:
                for i in range(3):
                    for j in range(3):
                        self.inputEntries[i][j].destroy()
                    self.arr_numbers2[i].clear()
                self.inputEntries = []
            self.home()


        def buildTable():
            states = [[]]
            states = self.controller.getstates()
            self.mycanvas2 = Canvas(self.root, width=250,
                                    height=400,
                                    bd=0, highlightthickness=0, bg=self.background_color)
            self.mycanvas2.place(x=625, y=50)
            self.mycanvas2.create_line(130, 0, 130, 400, fill=self.empty_color, width=3)
            self.mycanvas2.create_line(0, 0, 0, 400, fill=self.empty_color, width=3)
            self.mycanvas2.create_line(250, 0, 250, 400, fill=self.empty_color, width=3)
            y1 = 0

            for i in range(0, 6):  # lines
                if (i != 0):
                    y1 = 100 + y1
                self.mycanvas2.create_line(0, y1, 250, y1, fill=self.empty_color, width=3)

            x2 = 62.5  # text
            y2 = 50
            x3 = 187.5
            for i in range(0, 4):
                self.mycanvas2.create_text(x2, y2, text=states[i][0], fill=self.foreground_color, width=118,
                                           font=("", 18))
                self.mycanvas2.create_text(x3, y2, text=states[i][1], fill=self.foreground_color, font=("", 22))
                y2 += 100

        def end():
            Auto.place_forget()
            Next.place_forget()
            home.place(x=400,y=375)
            buildTable()
            print("end")


        def returned():
            Auto.place(x=400, y=375)
            Next.place(x=700, y=375)
            home.place_forget()
            self.mycanvas2.destroy()
            print("returned")


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
            if self.counter<len(self.moves_arr):
                print("b5af 2nsaky")
                if self.counter==len(self.moves_arr)-1:
                    end()
                move(self.moves_arr[self.counter][0], self.moves_arr[self.counter][1],
                     self.moves_arr[self.counter - 1][0], self.moves_arr[self.counter - 1][1])
                self.counter += 1

                if self.counter == 2:
                    PRev.place(x=100, y=375)



        def previous():
            if(self.counter>1):
                if self.counter == len(self.moves_arr):
                    returned()
                move(self.moves_arr[self.counter - 2][0], self.moves_arr[self.counter- 2][1],
                    self.moves_arr[self.counter -1][0], self.moves_arr[self.counter -1 ][1])
                self.counter -= 1
                if self.counter == 1:
                    PRev.place_forget()


        def auto():
            while self.counter < len(self.moves_arr):
                next()


        PRev = Button(self.root, text='Prev', bg=self.background_color, command=previous,
                     fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        Auto = Button(self.root, text='Auto', bg=self.background_color, command=auto,
                     fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        Auto.place(x=400, y=375)
        Next = Button(self.root, text='Next', bg=self.background_color, command=next,
                    fg=self.foreground_color, height=2, width=8, font=("", 15), relief=RAISED)
        Next.place(x=700, y=375)

        backc = Button(self.root, text='Back',command=back, bg=self.background_color, fg=self.foreground_color,
                      height=2, width=8, font=("", 15), relief=RAISED)
        backc.place(x=100, y=50)
        home = Button(self.root, text='Home',command=gotohome, bg=self.background_color, fg=self.foreground_color,
                      height=2, width=8, font=("", 18), relief=RAISED)
        self.changeOnHover(PRev)
        self.changeOnHover(home)
        self.changeOnHover(Auto)
        self.changeOnHover(Next)
        self.changeOnHover(backc)


        self.controller.set_puzzle_for_agent(self.arr, 3, 3)
        self.controller.search(self.method)
        self.moves_arr = self.controller.getpath()
        self.counter = 1







