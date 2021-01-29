from tkinter import*
import Maze
import StackQueue

class PrintMaze :
    def __init__(self) :
        
        window = Tk()
        window.title("Bread Maze")

        frame = Frame(window)
        frame.pack()

        btUp = Button(frame, text = "빠르게", command = self.speedup)
        btUp.pack(side = LEFT)
        btPlay = Button(frame, text = "START", command = self.Move)
        btPlay.pack(side = LEFT)
        btDown = Button(frame, text = "느리게", command = self.speeddown)
        btDown.pack(side = LEFT)

        self.bread = PhotoImage(file = "bread.gif")
        self.breadp = self.bread.subsample(8,8)
        self.house = PhotoImage(file = "house.gif")
        self.housep = self.house.subsample(8,8)
        self.hg = PhotoImage(file = "hg.gif")
        self.hgp = self.hg.subsample(5,5)

        self.sleepTime = 1

        self.canvas = Canvas(window, width = 600, height = 600, bg = "white")
        self.canvas.pack()
        self.displayLine()
        
        self.displayLocation()

        window.mainloop()

    def displayLine(self) :
        for i in range(60, 600, 60) :
            self.canvas.create_line(i, 0, i, 600, fill = "black", width = 2)
            self.canvas.create_line(0, i, 600, i, fill = "black", width = 2)

    def displayLocation(self) :
        for i in range(10) :
            for j in range(10) :
                if (Maze.maze[i][j].data == Maze.end) :
                    self.canvas.create_image((j*60)+30, (i*60)+30, image = self.housep)
                elif (Maze.maze[i][j].data == 0) :
                    self.canvas.create_rectangle(j*60, i*60, (j+1)*60, (i+1)*60, fill = "black")

        for i in range(10) :
            for j in range(10) :
                if (Maze.maze[i][j].data == 'U') :
                    self.canvas.create_image((j*60)+30, (i*60)+30, image = self.hgp, tags = "hg")

    def displayMove(self) :
        #Maze.routeQ.print()
        move = False
        for i in range(10) :
            #print("i = ", i)
            for j in range(10) :
                if (Maze.maze[i][j].data =='U') :
                    nex = Maze.routeQ.peek()
                    pos = (i*10)+j+1
                    #print(pos, nex)
                    #밑으로 이동
                    if (nex == pos) :
                        Maze.routeQ.dequeue()
                        break
                    if (nex-pos == 10):
                        for k in range(60) :
                            self.canvas.move("hg", 0, 1)
                            self.canvas.after(self.sleepTime)
                            self.canvas.update()
                        self.canvas.create_line((j*60)+30, (i*60)+30, (j*60)+30, (i*60)+90, width=6, fill = "pink")
                        self.canvas.create_image((j*60)+30, (i*60)+30, image = self.breadp)
                        Maze.routeQ.dequeue()
                        Maze.maze[i+1][j].data = 'U'
                        Maze.maze[i][j].data = pos
                        move = True
                        break
                    #오른쪽으로 이동
                    elif (nex-pos == 1) :
                        for k in range(60) :
                            self.canvas.move("hg", 1, 0)
                            self.canvas.after(self.sleepTime)
                            self.canvas.update()
                        self.canvas.create_line((j*60)+25, (i*60)+30, (j*60)+95, (i*60)+30, width=6, fill = "pink")
                        self.canvas.create_image((j*60)+30, (i*60)+30, image = self.breadp)
                        Maze.routeQ.dequeue()
                        Maze.maze[i][j+1].data = 'U'
                        Maze.maze[i][j].data = pos
                        move = True
                        break
                    #위로 이동
                    elif (nex-pos == -10) :
                        for k in range(60) :
                            self.canvas.move("hg", 0, -1)
                            self.canvas.after(self.sleepTime)
                            self.canvas.update()
                        self.canvas.create_line((j*60)+30, (i*60)-30, (j*60)+30, (i*60)+30, width=6, fill = "pink")
                        self.canvas.create_image((j*60)+30, (i*60)+30, image = self.breadp)
                        Maze.routeQ.dequeue()
                        Maze.maze[i-1][j].data = 'U'
                        Maze.maze[i][j].data = pos
                        move = True
                        break
                    #왼쪽으로 이동
                    elif (nex-pos == -1) :
                        for k in range(60) :
                            self.canvas.move("hg", -1, 0)
                            self.canvas.after(self.sleepTime)
                            self.canvas.update()
                        self.canvas.create_line((j*60)-35, (i*60)+30, (j*60)+35, (i*60)+30, width=6, fill = "pink")
                        self.canvas.create_image((j*60)+30, (i*60)+30, image = self.breadp)
                        Maze.routeQ.dequeue()
                        Maze.maze[i][j-1].data = 'U'
                        Maze.maze[i][j].data = pos
                        move = True
                        break
            if (move) :
                break

    def Move(self) :
        Maze.routeQ.dequeue()
        while (not Maze.routeQ.isEmpty()) :
            self.displayMove()

    def speedup(self) :
        self.sleepTime -= 10

    def speeddown(self) :
        self.sleepTime += 10
    

def main() :
    Maze.main()

