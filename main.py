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

def main():
    window = Window (800,600)
    window.wait_for_close()

main()
