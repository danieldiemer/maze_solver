from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.root = Tk()
        self.root.title("Amazing Maze Solver") 
        self.canvas = Canvas(self.root, width=width, height=height, bg="grey")
        self.canvas.pack(fill=BOTH,expand=1) 
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("exited successfully")

    def close(self):
        self.running = False

    def draw_line(self, line, color_fill="black"):
        line.draw(self.canvas,color_fill)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point_1,point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self,canvas,color_fill="black"):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=color_fill, width=3)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
        def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    win.wait_for_close()

main()
