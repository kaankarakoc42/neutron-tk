import tkinter as tk
from PIL import ImageTk
from PIL import Image



class Rotate(object):
    def __init__(self, master, filepath, **kwargs):
        self.master = master
        self.image = Image.open(filepath)
        self.canvas = tk.Canvas(master,width=self.image.size[0],height=self.image.size[1])
        self.angle = 0
        
    def rotateZ(self,x,y,speed=1):
        self.canvas.place(x=x,y=y)
        self.update = self.__rotateZ(speed).__next__
        self.master.after(100, self.update)
        return self.canvas
        

    def __rotateZ(self,speed):
        while True:
            tkimage = ImageTk.PhotoImage(self.image.rotate(self.angle))
            canvas_obj = self.canvas.create_image(self.image.size[0]/2,self.image.size[1]/2, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            self.angle += speed
            self.angle %= 360

class Translate:
    def __init__(self,AppWindow,canvas,element):
        self.AppWindow = AppWindow
        self.canvas = canvas
        self.element = element
        self.x = self.canvas.coords(self.element)[0]
        self.y = self.canvas.coords(self.element)[1]
        self.AppWindow.update()
        self.canvasWidth=self.canvas.winfo_width()
        self.canvasHeight=self.canvas.winfo_height() 
        self.state = True
    
    def setState(self,bool):
        self.state=bool    
      
    def translateX(self,targetX,speed=1):
        if self.state==True and self.x!=targetX and  self.canvas.coords(self.element)[2]+self.canvas.coords(self.element)[3]<self.canvasWidth:
           self.x+=speed
           self.canvas.move(self.element,self.x,self.y)
           self.canvas.after(100, lambda :self.translateX(targetX))


class Painter:
    def __init__(self,maincanvas,color="#476042"):
        self.maincanvas=maincanvas
        self.color=color
        self.bind()
    
    def bind(self):
        self.maincanvas.bind("<B1-Motion>",self.paint)
    
    def paint(self,event):
        x1, y1 = ( event.x - 1 ), ( event.y - 1 )
        x2, y2 = ( event.x + 1 ), ( event.y + 1 )
        self.maincanvas.create_rectangle( x1, y1, x2, y2, fill = self.color)