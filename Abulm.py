from guizero import App,Picture,Box,Text

app = App(title="Abulm Gia đình")
text = Text(app,text="Abulm Ảnh Gia Đình",bold= True,color="Blue")
box = Box(app, layout="grid",border= True)
anh1 = Picture(box,image='1.png',grid=[0,0],width=300,height=300)
anh2 = Picture(box,image='2.png',grid=[1,0],width=300,height=300)
anh3 = Picture(box,image='3.png',grid=[0,1],width=300,height=300)
anh4 = Picture(box,image='4.png',grid=[1,1],width=300,height=300)
app.display()