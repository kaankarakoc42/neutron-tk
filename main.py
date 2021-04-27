from Neutron import NeutronApp,tk,Rotate,Translate,Painter
from PIL import Image,ImageTk


color="#1c1d22"
maincolor="#1c1c1d"
imagepath="image.png"
image = Image.open(imagepath)

app=NeutronApp(800,400)
    
@app.setStartScreen
def rotateScreen():
    app.maincanvas=tk.Canvas(app.window,width=800,height=370,bg=maincolor)
    Rotate(app.window,"image.png").rotateZ(x=270,y=90)
    tk.Label(text="Rotating with neutron app",bg=maincolor,font=("Consolas", 12),fg="lightgray").place(x=280,y=50)
    tk.Button(app.window,text="forward",command=lambda :app.navigation.navigate(translateScreen)).place(x=650,y=300)

def translateScreen():
    Translate(app.window,app.maincanvas,app.maincanvas.create_rectangle(0,0, 25, 25, fill = "cyan")).translateX(300)
    app.createComponent(tk.Button(app.window,text="forward",command=lambda :app.navigation.navigate(painterScreen))).place(x=650,y=300)

def painterScreen():
    app.createComponent(app.maincanvas)
    app.maincanvas.configure(bg="#fff")
    Painter(app.maincanvas)
    app.createComponent(tk.Button(app.window,text="  back   ",command=lambda :app.navigation.goBack())).place(x=650,y=300)

@app.setMenu
def menuComponent():
    app.maincanvas=tk.Canvas(app.window,width=800,height=370,bg=maincolor)
    app.maincanvas.place(x=-2,y=28)
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
   
