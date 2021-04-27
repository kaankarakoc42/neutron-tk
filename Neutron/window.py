import tkinter as tk
from mouse import get_position
from .interval import setInterval,setTimeOut
from .navigation import navigation

class NeutronApp:
      def __init__(self,w=800,h=400):
          self.window = tk.Tk()
          self.navigation=navigation(self.window)
          self.window.geometry(f"{w}x{h}")
          self.window.resizable(False, False)
          self.window.overrideredirect(True)
          self.window.bind('<B1-Motion>', lambda e: self.__event(e))
          self.window.bind('<ButtonRelease-1>', lambda e: self.__standard_bind())
          self.window.bind("<Unmap>",self.minimize)
          self.window.bind("<Map>",self.__frame_mapped)
          self.windowMove=True
          self.x,self.y=0,0
          self.timeouts,self.intervals=[],[]
      
      #window frame movement
      def __frame_mapped(self,e):
          self.window.update_idletasks()
          self.window.overrideredirect(True)

        
      def __standard_bind(self,e=None):
          self.window.bind('<B1-Motion>', lambda e: self.__event(e, Mode=True))

      def __event(self,widget, Mode=False):
          if Mode:
             self.x = widget.x
             self.y = widget.y
          self.window.bind('<B1-Motion>', lambda e: self.__event(e))
          if self.windowMove:
             self.window.geometry(f'+{get_position()[0]-self.x}+{get_position()[1]-self.y}')

      def setWindowMove(self,bool):
          #stop window frame movement
          self.windowMove=bool
     
      #window exit,minimize button commands
      def quit(self,e=None):
          for i in self.intervals:
              i.clearInterval()
          for i in self.timeouts:
              i.clearTimeOut()
          self.window.destroy()
          exit()
          
      def minimize(self,e=None):
          self.window.update_idletasks()
          self.window.overrideredirect(False)
          self.window.state('iconic')

      # about components
      def createComponent(self,element):
          element.update()
          element.bind("<Enter>",lambda e:self.setWindowMove(False))
          element.bind("<ButtonRelease-1>",self.setWindowMove(False))
          element.bind("<Leave>",lambda e:self.setWindowMove(True))
          return element
          
      def onHoverColor(self,event,bg="lightGray",fg=None):
          if fg:
              event.widget.config(bg=bg,fg=fg)
          event.widget.config(bg=bg)

      def onBlurColor(self,event,bg="#1b1c1f",fg=None):
          if fg:
              event.widget.config(bg=bg,fg=fg)
          event.widget.config(bg=bg)

      #timers
      def setInterval(self,func,miliseconds):
          i=setInterval(func,miliseconds)
          self.intervals.append(i)
          return i
      
      def setTimeOut(self,func,miliseconds):
          i=setTimeOut(func,miliseconds)
          self.timeouts.append(i)
          return i
     
      #decorators
      def setStartScreen(self,func):
          self.startScreen=func
          
      def setMenu(self,func):
          self.navigation.menu=func


      #for run app 
      def run(self):
          self.navigation.menu()
          self.startScreen()
          self.navigation.stack.append(self.startScreen)
          self.window.mainloop()
          
          