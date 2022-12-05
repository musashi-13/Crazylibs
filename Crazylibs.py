from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox, Canvas, Label 
from gtts import gTTS
from playsound import playsound
import os, random, csv

root= Tk()

root.geometry("1920x1080")
root.title("CrazyLibs")
root.iconbitmap("Assets/MainLogo.ico")
root.configure(bg="#282828")

backgroundimage = PhotoImage(file="Assets/background.png")
canvas = Canvas(root, height=1080, width=1920, bg="#282828", highlightthickness=0)
canvas.create_image(0,0, image= backgroundimage, anchor=NW)
canvas.place(relx=0.5, rely=0.5,anchor= CENTER)

frame = Frame(root, padx=10, bg="#282828")
frame.place(relx=.5, rely=.05,anchor= CENTER)

Logo= (Image.open("Assets/MainLogo.png"))
Resized_Logo= Logo.resize((100,100), Image.Resampling.LANCZOS)
NewLogo= ImageTk.PhotoImage(Resized_Logo, Image.Resampling.LANCZOS)
LogoMain = Label(frame, image=NewLogo, bg="#282828")
LogoMain.grid(row=0, column=0)
Heading = Label(frame, text="CRAZY LIBS", fg="white", bg="#282828")
Heading.grid(row=0, column=1)
Heading.config(font=("Bauhaus 93", 44))

AdminMode=False
UsernameInput = "admin"
PasswordInput = "crazylibs"

def adminpage():
    top = Toplevel()
    top.configure(bg="#282828")
    top.title("Settings")
    top.iconbitmap("Assets/MainLogo.ico")
    top.geometry("700x350")

    r=IntVar()
    def AddWord(Type,Word):
        u=Type-1
        if u == -1:
            Label(top, text="You did not select the word type  ", fg="red", bg="#282828",font=("Calibri", 14)).place(x=295, y=193)
        elif Word =='':
            Label(top, text="You did not enter the word yet    ", fg="red", bg="#282828",font=("Calibri", 14)).place(x=295, y=193)
        else:
            with open("wordbank.csv","r") as WordBank:
                r =csv.reader(WordBank)
                v=[]
                for lines in r:
                    v.append(lines)
                WordBank.close()
                if Word.lower() in v[u]:
                    Label(top, text="The word you entered already exists", fg="red", bg="#282828",font=("Calibri", 14)).place(x=295, y=193)
                else:
                    Label(top, text="Word has been successfully added! ", fg="red", bg="#282828",font=("Calibri", 14)).place(x=295, y=193)
                    with open ("wordbank2.csv","w", newline='') as WordBank2:
                        w=csv.writer(WordBank2)
                        for element in v:
                            if v.index(element) != u:
                                w.writerow(element)
                            else:
                                element.append(Word)
                                w.writerow(element)
                        WordBank2.close()
                    os.remove("wordbank.csv")
                    os.rename("wordbank2.csv","wordbank.csv")

    def RemoveWord(Word):
        print(Word)
        if Word =='':
            Label(top, text="You did not enter the word yet    ", fg="red", bg="#282828",font=("Calibri", 14)).place(x=295, y=193)
        else:
            with open("wordbank.csv","r") as WordBank:
                r =csv.reader(WordBank)
                v=[]
                rmv = False
                for lines in r:
                    v.append(lines)
                WordBank.close()
                for i in range(len(v)):
                    if Word in v[i]:
                        with open ("wordbank2.csv","w", newline='') as WordBank2:
                            w=csv.writer(WordBank2)
                            for element in v:
                                if v.index(element) != i:
                                    w.writerow(element)
                                else:
                                    element.remove(Word)
                                    w.writerow(element)
                            WordBank2.close()
                        os.remove("wordbank.csv")
                        os.rename("wordbank2.csv","wordbank.csv")
                        rmv = True
            if rmv == False:
                Label(top, text="The word you entered does not exist", fg="red", bg="#282828",font=("Calibri", 14)).place(x=295, y=193)
            else:            
                Label(top, text="Word has been successfully removed ", fg="red", bg="#282828",font=("Calibri", 14)).place(x=295, y=193)
    
    Label(top, text="WORD BANK SETTINGS", fg="white", bg="#282828",font=("Bauhaus 93", 24)).place(x=205)
    Label(top,text="Add a word to the word bank!",font=("Calibri", 14),bg="#282828", fg="white",).place(x=57,y=50)
    Label(top,text="Enter the word: ",font=("Calibri", 14),bg="#282828", fg="white",).place(x=57,y=83)
    WordInput = Entry(top, width=30, bg="white", font=("Calibri", 14))
    WordInput.place(x=200,y=83)
    Label(top,text="Select what type of word it is: ",font=("Calibri", 14),bg="#282828", fg="white",).place(x=57,y=117)
    Radiobutton(top, text="Noun",font=("Calibri", 14), bg="#282828", fg="white", activebackground="#212121",activeforeground="white", selectcolor="#212121", variable=r, value=1).place(x=57,y=150)
    Radiobutton(top, text="Verb",font=("Calibri", 14), bg="#282828", fg="white", activebackground="#212121",activeforeground="white", selectcolor="#212121", variable=r, value=2).place(x=130,y=150)
    Radiobutton(top, text="Adjective",font=("Calibri", 14), bg="#282828", fg="white", activebackground="#212121",activeforeground="white", selectcolor="#212121", variable=r, value=3).place(x=196,y=150)
    Radiobutton(top, text="Verb ending with -ing",font=("Calibri", 14), bg="#282828", fg="white", activebackground="#212121",activeforeground="white", selectcolor="#212121", variable=r, value=4).place(x=297,y=150)
    Radiobutton(top, text="Place",font=("Calibri", 14), bg="#282828", fg="white", activebackground="#212121",activeforeground="white", selectcolor="#212121", variable=r, value=5).place(x=492,y=150)
    Radiobutton(top, text="Object",font=("Calibri", 14), bg="#282828", fg="white", activebackground="#212121",activeforeground="white", selectcolor="#212121", variable=r, value=6).place(x=562,y=150)
    btn=Button(top, text="Add", bg="#282828",fg="white",font=("Calibri", 14), width=10, command=lambda: AddWord(r.get(),WordInput.get()))
    btn.place(x=180,y=190)
    btn=Button(top, text="Remove", bg="#282828",fg="white",font=("Calibri", 14), width=10, command=lambda: RemoveWord(WordInput.get()))
    btn.place(x=180,y=235)
    btn=Button(top, text="Close", bg="#BA1010",fg="white",font=("Calibri", 14), width=10, command=top.destroy)
    btn.place(x=180,y=280)
    top.mainloop()

stgbtn = Button(root, text="Settings", bg="black",fg="white", width=10, command=adminpage)
stgbtn.config(font=("Hansief", 12))

def openadmin():
    global AdminMode
    top = Tk()
    top.configure(bg="#282828")
    top.title("Admin Login")
    top.iconbitmap("Assets/MainLogo.ico")
    top.geometry("400x250")

    AdminHeading = Label(top, text="ADMIN LOGIN", fg="white", bg="#282828")
    AdminHeading.config(font=("Bauhaus 93", 28))
    AdminHeading.place(x=90, y=10)

    def LogOut():
        global AdminMode
        AdminMode=False
        global stgbtn
        stgbtn.place_forget()
        top.destroy()

    if AdminMode==False:
        Username = Label(top, bg="#282828", text="Enter the username:", font=("Calibri", 12), fg="white").place(x=80, y=60)
        USInput = Entry(top, width=30, bg="white", font=("Calibri", 12))
        USInput.place(x=80, y=80)

        Password = Label(top, bg="#282828", text="Enter the password:", font=("Calibri", 12), fg="white").place(x=80, y=105)
        PSInput = Entry(top, width=30, bg="white", font=("Calibri", 12),show="•")
        PSInput.place(x=80, y=125)
        InputPassword = PSInput.get()
        
        btn = Button(top, text="Ok",bg="#366994",fg="white", width=10, command=lambda: checkpass(InputPassword))
        btn.config(font=("Bauhaus 93", 12))
        btn.place(x=80, y=180)
        btn = Button(top, text="Cancel",bg="white",fg="black", width=10, command=top.destroy)
        btn.config(font=("Bauhaus 93", 12))
        btn.place(x=225, y=180)

        def checkpass(InputPassword):
            InputPassword = PSInput.get()
            InputUsername = USInput.get()
            global PasswordInput, UsernameInput, AdminMode
            if InputPassword==PasswordInput and InputUsername==UsernameInput:
                AdminMode=True
                global stgbtn
                stgbtn.place(relx=0.702, rely=0.01)
                top.destroy()    
            elif InputPassword!= PasswordInput or InputUsername!=UsernameInput:
                PassCheck = Label(top, bg="#282828", text="Credentials are incorrect", font=("Calibri", 12), fg="#FF5454").place(x=80, y=150)

    elif AdminMode==True:
        LoggedIn = Label(top, bg="#282828", text="Already logged in.", font=("Calibri", 12), fg="#FF5454").place(x=140, y=80)
        btn = Button(top, text="Log Out",bg="#366994",fg="white", width=10, command=LogOut)
        btn.config(font=("Bauhaus 93", 12))
        btn.place(x=150, y=110)

    top.mainloop()
 
def openhelp():
    top = Toplevel()
    top.title("Admin Login")
    top.iconbitmap("Assets/MainLogo.ico")
    top.geometry("800x450")
    global img
    img = PhotoImage(file=r"help.png")
    Label(top,image=img).place(x=0, y=0)

def popup():
    response=messagebox.askyesno("WARNING", "Are you sure you want to Exit?")
    if response==1:
        root.destroy()

Word_Bank=[]
with open ('wordbank.csv', 'r') as WordBank:
    r = csv.reader(WordBank)
    for lines in r:
        Word_Bank.append(lines)
    WordBank.close

NounList= Word_Bank[0]
VerbList = Word_Bank[1]
AdjList = Word_Bank[2]
IngList= Word_Bank[3]
PlaceList = Word_Bank[4]
ObjList = Word_Bank[5]

StoriesList=[]
with open("Storybank.txt",'r') as StoryBank:
    LineList = []
    for j in range(5):
        for i in range(3):
            if i==0:
                LineList.append(StoryBank.readline().rstrip("\n"))
            else:
                t= StoryBank.readline().rstrip("\n")
                u = t.split("|")
                LineList.append(u)
            i+=1
        StoriesList.append(LineList)
        LineList=[ ]    
        j+=1
    StoryBank.close()

canvas = Canvas(root, height=20, width=1600, bg="#282828", highlightthickness=0)
canvas.create_line(0, 0, 1600, 0, width=10, fill="#ffc331")
canvas.place(relx=0.5, rely=.1,anchor= CENTER)

frame = Frame(root, padx=10, bg="#282828")
frame.place(relx=.8, rely=.0945,anchor= CENTER)

btn = Button(frame, text="Help",bg="#366994",fg="white", width=10, command=openhelp)
btn.config(font=("Bauhaus 93", 12))
btn.grid(row=0, column=0)

btn = Button(frame, text="Admin", bg="#f22c67",fg="white", width=10, command=openadmin)
btn.config(font=("Bauhaus 93", 12))
btn.grid(row=0, column=1)

btn = Button(frame, text="Exit",bg="#BA1010", fg="white", width=10, command=popup)
btn.config(font=("Bauhaus 93", 12))
btn.grid(row=0, column=2)

frame3 = Frame(root, padx=10, pady=10, bg="#282828")
frame3.place(width=1072, height=270, relx=.5, rely=0.3,anchor= CENTER)

Heading = Label(frame3, text="CHOOSE YOUR STORY!", fg="white", bg="#282828")
Heading.place(x=0, y=0, anchor=NW)
Heading.config(font=("Hansief", 24))

def story(n):
    framestory1 = Frame(root, padx=10, pady=10, bg="#282828")
    framestory1.place(width=1072, height=580, relx=.5, rely=0.45,anchor= N)
    global StoriesList
    entries1,answer1 = [], []

    def redirect(f, *arg):
        return lambda: f(*arg)

    def execute():
        for txt in entries1:
            answer1.append(txt.get())
        answer1.append(" ")
        frameDS1= Frame(framestory1, bg="#282828")
        frameDS1.place(width=610, height=580, relx=1, rely=0, anchor=NE)
        textbox = ''
        for objct in (StoriesList[n-1][1]):
                i = (StoriesList[n-1][1]).index(objct)
                textbox= textbox + objct.replace('\\n', '\n')
                textbox= textbox + answer1[i]+" "
        label = Label(frameDS1, font=("Calibri", 14), text=textbox, fg="white", bg="#282828", width=55, anchor=NW, height=10, wraplength=560, justify=LEFT)
        label.place(relx=0.01, rely=0)

        def tts():
            v = gTTS(text=textbox, lang="en", slow=False)
            v.save(f'speech.mp3')
            playsound(f'speech.mp3')
            os.remove("speech.mp3")
        
        btn = Button(frameDS1, text="Speak it out!",bg="#003C6B", fg="white", width=20, borderwidth=0,  command=tts)
        btn.config(font=("Hansief", 16))
        btn.place(relx=0.46, rely=0.5, anchor=CENTER)
        label= Label(frameDS1, font=("Calibri", 14), text="To try this story again select it from the Menu above!", fg="white", bg="#282828", width=55, anchor=CENTER)
        label.place(relx=0, rely=0.55)
    try:
        TypeList=StoriesList[n-1][2]

        def randnoun(entry):
            global NounList
            random_noun = NounList[random.randint(0, (len(NounList) - 1))]
            entry.delete(0, END)
            entry.insert(0, random_noun)
        def randverb(entry):
            global VerbList
            random_verb = VerbList[random.randint(0, (len(VerbList) - 1))]
            entry.delete(0, END)
            entry.insert(0, random_verb)  
        def randadj(entry):
            global AdjList
            random_adj = AdjList[random.randint(0, (len(AdjList) - 1))]
            entry.delete(0, END)
            entry.insert(0, random_adj)
        def randing(entry):
            global IngList
            random_ing = IngList[random.randint(0, (len(IngList) - 1))]
            entry.delete(0, END)
            entry.insert(0, random_ing)
        def randplace(entry):
            global PlaceList
            random_place = PlaceList[random.randint(0, (len(PlaceList) - 1))]
            entry.delete(0, END)
            entry.insert(0, random_place)
        def randobj(entry):
            global ObjList
            random_obj = ObjList[random.randint(0, (len(ObjList) - 1))]
            entry.delete(0, END)
            entry.insert(0, random_obj)

        for count, i in enumerate(TypeList):
            label = Label(framestory1, font=("Calibri", 14), text=i+' ', fg="white", bg="#282828")
            label.grid(row=count, column=0)
            entry = Entry(framestory1, width=15, font=("Calibri", 14), borderwidth=0)
            entries1.append(entry)
            entry.grid(row=count, column=1)

            if "noun" in i.lower():
                btn = Button(
                    framestory1,font=("Calibri",10), width=8, borderwidth=0, pady=3, bg="#366994", fg="white", text = "RANDOM",
                    command= redirect(randnoun, entry))
                btn.grid(row = count, column = 2, pady=2)
            elif "verb" in i.lower() and "ing" not in i.lower():
                btn = Button(
                    framestory1,font=("Calibri",10), width=8, borderwidth=0, pady=3, bg="#366994", fg="white", text = "RANDOM",
                    command= redirect(randverb, entry))
                btn.grid(row = count, column = 2, pady=2) 
            elif "adjective" in i.lower():
                btn = Button(
                    framestory1,font=("Calibri",10), width=8, borderwidth=0, pady=3, bg="#366994", fg="white", text = "RANDOM",
                    command= redirect(randadj, entry))
                btn.grid(row = count, column = 2, pady=2) 
            elif "ing" in i.lower():
                btn = Button(
                    framestory1,font=("Calibri",10), width=8, borderwidth=0, pady=3, bg="#366994", fg="white", text = "RANDOM",
                    command= redirect(randing, entry))
                btn.grid(row = count, column = 2, pady=2)  
            elif "place" in i.lower():
                btn = Button(
                    framestory1,font=("Calibri",10), width=8, borderwidth=0, pady=3, bg="#366994", fg="white", text = "RANDOM",
                    command= redirect(randplace, entry))
                btn.grid(row = count, column = 2, pady=2) 
            elif "object" in i.lower():
                btn = Button(
                    framestory1,font=("Calibri",10), width=8, borderwidth=0, pady=3, bg="#366994", fg="white", text = "RANDOM",
                    command= redirect(randobj, entry))
                btn.grid(row = count, column = 2, pady=2)           

        btn = Button(framestory1, width=14, text='GO!', font=("Hansief", 14), padx = 4, bg="#ffc331", borderwidth=0, command=execute)
        btn.grid(row=count+1, column=1, pady=2)

    except IndexError:
        label = Label(framestory1, font=("Calibri", 14), text="Story YET to be published..", fg="white", bg="#282828")
        label.grid(row=0, column=0, columnspan=2)

btn = Button(frame3, text=StoriesList[0][0], bg="#003C6B", fg="white", width=40, borderwidth=0,  command=lambda: story(1))
btn.config(font=("Hansief", 16))
btn.place(x=0, y=50, anchor=NW)
btn = Button(frame3, text=StoriesList[1][0],bg="#003C6B", fg="white", width=40, borderwidth=0, command=lambda: story(2))
btn.config(font=("Hansief", 16))
btn.place(x=457, y=50, anchor=NW)
btn = Button(frame3, text=StoriesList[2][0],bg="#003C6B", fg="white", width=40, borderwidth=0, command= lambda: story(3))
btn.config(font=("Hansief", 16))
btn.place(x=150, y=100, anchor=NW)
btn = Button(frame3, text=StoriesList[3][0],bg="#003C6B", fg="white", width=40, borderwidth=0, command= lambda: story(4))
btn.config(font=("Hansief", 16))
btn.place(x=607, y=100, anchor=NW)
btn = Button(frame3, text=StoriesList[4][0],bg="#003C6B", fg="white", width=40, borderwidth=0, command= lambda: story(5))
btn.config(font=("Hansief", 16))
btn.place(x=0, y=150, anchor=NW)
btn = Button(frame3, text="STORY 6",bg="#003C6B", fg="white", width=40, borderwidth=0, command= lambda: story(6))
btn.config(font=("Hansief", 16))
btn.place(x=457, y=150, anchor=NW)
btn = Button(frame3, text="STORY 7",bg="#003C6B", fg="white", width=40, borderwidth=0, command= lambda: story(7))
btn.config(font=("Hansief", 16))
btn.place(x=150, y=200, anchor=NW)
btn = Button(frame3, text="STORY 8",bg="#003C6B", fg="white", width=40, borderwidth=0, command= lambda: story(8))
btn.config(font=("Hansief", 16))
btn.place(x=607, y=200, anchor=NW)

root.mainloop() 