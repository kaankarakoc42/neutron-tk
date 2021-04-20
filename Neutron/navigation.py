
class navigation:
      
      def __init__(self,window):
          self.window=window
          self.stack=[]
          self.menu = lambda :2+2
      
      def getAllWidgets(self):
          widgets = self.window.winfo_children()
          for item in widgets :
              if item.winfo_children() :
                 widgets.extend(item.winfo_children())
          return widgets
     
     
      def clear(self):
          widgets=self.getAllWidgets()
          for widget in widgets:
              widget.destroy()
              
      def navigate(self,target,*args,**kwargs):
          self.clear()
          self.stack.append(target)
          self.menu()
          if len(self.stack)>3:
             self.stack=self.stack[3:]
          target()
      
      def goBack(self):
          if len(self.stack)>1:
             self.clear()
             self.menu()
             self.stack[len(self.stack)-2]()
             self.stack.pop()    