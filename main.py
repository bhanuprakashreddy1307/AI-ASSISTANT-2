from tkinter import* #  *represents all the functions and built-in modules in tkinter library
from PIL import Image , ImageTk
import ACTION
root =Tk()
root.title("AI ASSISTANT") #ADDING TITLE
root.geometry("550x625") #giving dimensions
root.resizable(False,False) #no resize
root.config(bg="#00BFFF") #giving background color

#ASK FUNCTION

def ask():
    user_val = SPEECHRECOGNITION.SPEECHRECOGNITION() #if user clicls button_1
    bot_val = ACTION.ACTION(user_val)
    text.insert(END , 'User----->'+user_val+"\n")
    if bot_val != None:
        text.insert(END , "BOT <----"+str(bot_val)+"\n")
    if bot_val == "ok":
        root.destroy()

def send():
    send = entry.get() #if user clicks button_2 it prints SEND
    bot = ACTION.ACTION(send)
    text.insert(END , 'User--->'+send+"\n")
    if bot!= None:
        text.insert(END , "BOT <----"+str(bot)+"\n")
    if bot == "ok":
        root.destroy()


def delete():
    text.delete('1.0', "end") #if user clicks button_3 it prints DELETE

#MAKING A FRAME

frame = LabelFrame(root , padx = 100 , pady = 7 , borderwidth = 3 , relief = "raised" ) #RELIEF REFERS TO 3-D EFFECTS AROUND THE OUTSIDE OF WIDGET
frame.config(bg="#00BFFF")
frame.grid(row = 0, column = 1, padx = 55 , pady = 10)

#ADDING TEXT LABEL

text_label = Label(frame , text="AI ASSISTANT" , font =("Times" , 14 , "bold"))
text_label.grid(row = 0, column = 0 , padx = 20 , pady = 10)

#IMAGE
image = ImageTk.PhotoImage(Image.open("C:\\Users\\bhanu\\Downloads\\assitant (1).png"))
image_label = Label(frame , image=image)
image_label.grid(row = 1,column=0,pady=20)

#ADDING A TEXT WIDGET

text = Text(root , font = ('coutior 10 bold'), bg ="#356696")
text.grid(row =2, column=0)
text.place(x = 100,y = 375,width = 375,height = 100) #dimensions and positions of textwidget

#ENTRY WIDGET

entry = Entry(root, justify=CENTER)
entry.place(x=100 , y=500 , width = 350 , height =30) #dimensions and position of entrywidget

#BUTTON_1

Button1 = Button(root,text = "ASK" , bg ="#356696" , pady = 16 , padx = 40 , borderwidth = 3 , relief = SOLID ,command = ask)
Button1.place(x = 70 , y = 545) #position of button_1

#BUTTON_2

Button2 = Button(root,text = "SEND" , bg ="#356696" , pady = 16 , padx = 40 , borderwidth = 3 , relief = SOLID ,command = send)
Button2.place(x = 400 , y = 545) #position of button_2

#BUTTON_3

Button3 = Button(root,text = "DELETE" , bg ="#356696" , pady = 16 , padx = 40 , borderwidth = 3 , relief = SOLID ,command = delete)
Button3.place(x = 225 , y = 545) #positon of button_3

#USER INTERFACE PATH IS CREATED SUCCESSFULLY
root.mainloop()
