from threading import Thread
from time import time,sleep

class setInterval:
      def __init__(self,func:"function",timing:"miliseconds"):
          self.func=func
          self.timing=timing*2000
          self.__state=True
          self.__counter=0
          Thread(target=self.__run).start()
          
      def clearInterval(self):
          self.__state=False
          
      def __str__(self):
          if not self.__state:
              return f"<Closed Interval-{str(self.func).split(' ')[1]}>"
          return f"<Interval-{str(self.func).split(' ')[1]}>"
      
      def __run(self):
          try:
            while self.__state:
                if self.__counter>=self.timing:
                   self.func()
                   self.__counter=0
                else:
                   self.__counter+=1
          except RuntimeError:
               self.__state=False
           
class setTimeOut:
      def __init__(self,func:"function",timing:"miliseconds"):
          self.func=func
          self.timing=timing*2000
          self.__state=True
          self.__counter=0
          Thread(target=self.__run).start()   
             
      def clearTimeOut(self):
          self.__state=False
          
      def __str__(self):
          if not self.__state:
              return f"<Closed TimeOut-{str(self.func).split(' ')[1]}>"
          return f"<TimeOut-{str(self.func).split(' ')[1]}>"
      
      def __run(self):
          try:  
            while self.__state:
                if self.__counter>=self.timing:
                   self.func()
                   self.__state=False
                else:
                   self.__counter+=1
          except RuntimeError:
               self.__state=False

    
