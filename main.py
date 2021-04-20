from Neutron import window,tk
from time import sleep

color="#1c1d22"
maincolor="#1c1c1d"

app=window(800,400)
    

@app.setStartScreen
def waitingScreen():
    loadingStr=tk.StringVar()
    loadingStr.set("   ")
    tk.Label(app.window,bg=maincolor,fg="white",font=("Courier",30),textvariable=loadingStr).place(x=330,y=150)
    def textAnimation(variable,list,duration=1):
        for i in list:
            sleep(duration)
            variable.set(i)
    app.setInterval(lambda :textAnimation(loadingStr,["   ",".  ",".. ","..."],0.5),0.001)
    app.setTimeOut(lambda :app.navigation.navigate(mainScreen),3000)

def mainScreen():
    tk.Label(text="main screen",bg=maincolor,fg="white",).place(x=100,y=100)
    app.setTimeOut(lambda :app.navigation.navigate(loginScreen),3000)
    
def loginScreen():
    tk.Label(text="login screen",bg=maincolor,fg="white").place(x=100,y=100)
    tk.Entry().place(x=100,y=150,width=300,height=30)
    tk.Entry().place(x=100,y=200,width=300,height=30)
    app.setTimeOut(lambda :app.navigation.navigate(mainScreen),3000)
    tk.Button(text="   send   ",bg=color,fg="white",highlightthickness=1,activebackground=color,bd =4,highlightcolor=color,borderwidth=1,highlightbackground=color).place(x=230,y=250)

@app.setMenu
def menuComponent():
    tk.Canvas(app.window,width=800,height=370,bg=maincolor).place(x=-2,y=28)
    tk.Canvas(app.window,width=800,height=30,bg=color).place(x=-2,y=-2)
    tk.Label(app.window,text="Neutron",font=("Consolas", 12),bg=color,fg="lightgray").place(x=350,y=5)
    app.minimizeButton=tk.Label(app.window,text=" __ ",bg=color,fg="gray")
    app.minimizeButton.place(x=740,y=5)
    app.minimizeButton.bind("<Button-1>",app.minimize)
    app.minimizeButton.bind("<Enter>",lambda e:app.onHoverColor(e))
    app.minimizeButton.bind("<Leave>",lambda e:app.onBlurColor(e,color))
    app.closeButton=tk.Label(app.window,text=" X ",bg=color,fg="gray")
    app.closeButton.place(x=770,y=5)
    app.closeButton.bind("<Button-1>",app.quit)
    app.closeButton.bind("<Enter>",lambda e:app.onHoverColor(e))
    app.closeButton.bind("<Leave>",lambda e:app.onBlurColor(e,color,"gray"))
    
    
if __name__ == "__main__":
   app.run()
   
