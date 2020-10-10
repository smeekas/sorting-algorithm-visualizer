from tkinter import *
from random import shuffle,randint
from algo import algochooser
import time
root=Tk()
WINDOW_X,WINDOW_Y=1650,950
CANVAS_X,CANVAS_Y=1420,950
FRAME1_X,FRAME1_Y=230,950
root.geometry(f"{WINDOW_X}x{WINDOW_Y}")
root.config(bg="white")
root.wm_resizable(False,False)
root.title("sortlizer")
root.iconbitmap("final2.ico")
times=0
size_var=IntVar()
size_var.set(40)            #starting size of array
time_var=DoubleVar()
time_var.set(0.05)
starting_point=2            #starting point from where array will be drawn

def paint(numbers,colortype):       #this function will draw the array
    global canva,rec_width,size_var,starting_point,root

    canva.delete("all")
    starting_point=2
    rec_width=CANVAS_X/size_var.get()

    for i in range(len(numbers)):
        canva.create_rectangle(starting_point,CANVAS_Y-numbers[i],starting_point+rec_width,CANVAS_Y,fill=colortype[i])
        starting_point+=rec_width

    frame2.update()


def new_list():         #function to generate new list
    global  numbers,size_var,starting_point,label_access,label_comparison

    numbers=[]
    label_access.configure(text="array access:0")
    label_comparison.configure(text="comparison:0")

    numbers = [randint(5, 950) for i in range(size_var.get())]
    shuffle(list(set(numbers)))
    colortype=["#aaaaaa" for x in numbers]

    paint(numbers,colortype)

def shuffle_list():     #function to shuffle the list
    global  numbers,starting_point,label_access,label_comparison
    shuffle(numbers)
    label_access.configure(text="array access:0")
    label_comparison.configure(text="comparison:0")

    colortype = ["#aaaaaa" for x in numbers]
    paint(numbers,colortype)


def change_size(event):         #this function will change the size of the array
    global numbers,size_var,label_access,label_comparison
    numbers=[]
    label_access.configure(text="array access:0")
    label_comparison.configure(text="comparison:0")

    numbers = [randint(5, 950) for i in range(size_var.get())]
    shuffle(list(set(numbers)))
    colortype = ["#aaaaaa" for x in numbers]
    paint(numbers,colortype)


def change_time(event):
    global times
    times=time_var.get()

def sort_list():            #this function will sort the list with seleted sorting algorithm
    global numbers,label_access,algo_var,label_comparison
    label_access.configure(text="array access:0")
    label_comparison.configure(text="comparison:0")

    algochooser(numbers,paint,label_access,label_comparison,algo_var.get())

def case_chooser(event):        #this will display wrost case, average case, best case of algorithm
    global information
    label_avg.pack_forget()
    label_avg.configure(text=information[algo_var.get()])


frame1=Frame(root,width=FRAME1_X,height=FRAME1_Y,bg="#DEE6DB")    #frame1 contain all the buttons, menus, sliders.(left side of the window)
frame1.grid_propagate(0)
frame1.pack(side=LEFT)

information = {"bubble sort": "wrost case:O(n²)\naverage case:O(n²)\nbest case:O(n)",
             "selection sort": "wrost case:O(n²)\naverage case:O(n²)\nbest case:O(n²)",
             "merge sort": "wrost case:O(n*log n)\naverage case:O(n*log n)\nbest case:O(n*log n)",
             "heap sort": "wrost case:O(n*log n)\naverage case:O(n*log n)\nbest case:O(n*log n)",
             "insertion sort": "wrost case:O(n²)\naverage case:O(n²)\nbest case:O(n)",
             "quick sort": "wrost case:O(n²)\naverage case:O(n*log n)\nbest case:O(n*log n)",
             "shell sort": "wrost case:O((n*log n)²)\naverage case:O((n*log n)²)\nbest case:O(n)",
             "radix sort": "wrost case:O(nk)\naverage case:O(nk)\nbest case:O(nk)",
             "cocktail shaker": "wrost case:O(n²)\naverage case:O(n²)\nbest case:O(n)",
             "odd-even sort": "wrost case:O(n²)\naverage case:O(n²)\nbest case:O(n)",
             "gnome sort":"wrost case:O(n²)\naverage case:O(n²)\nbest case:O(n)"}

algorithm=["bubble sort","selection sort","merge sort",
           "heap sort","insertion sort","quick sort",
           "shell sort","radix sort","cocktail shaker",
           "odd-even sort","gnome sort"]

algo_var=StringVar()
algo_var.set(algorithm[0])
algo_menu=OptionMenu(frame1,algo_var,*algorithm,command=case_chooser)
algo_menu["highlightthickness"]=0
algo_menu["padx"]=24
algo_menu["pady"]=8
algo_menu.grid_propagate(0)
algo_menu.place(rely=0.1,relx=0.5,anchor=CENTER)

frame_btn=Frame(frame1,width=230,height=200,bg="#DEE6DB")
frame_btn.grid_propagate(0)
frame_btn.place(relx=0.0,rely=0.15)

btn_new=Button(frame_btn,text="NEW",padx=13,pady=3,command=new_list,bg="#305962",fg="#ffffff")
btn_new.place(relx=0.35,rely=0.1)

btn_shuffle=Button(frame_btn,text="Shuffle",padx=13,pady=3,command=shuffle_list,bg="#305962",fg="#ffffff")
btn_shuffle.place(relx=0.32,rely=0.4)

btn_sort=Button(frame_btn,text="sort",padx=13,pady=3,command=sort_list,bg="#305962",fg="#ffffff")
btn_sort.place(relx=0.36,rely=0.7)



label_access=Label(frame1,text="array access:0",bg="#DEE6DB",fg="#027EFF",font=("Fixedsys",14))
label_access.place(relx=0.1,rely=0.37)

label_comparison=Label(frame1,text="comparison:0",bg="#DEE6DB",fg="#027EFF",font=("Fixedsys",12))
label_comparison.place(relx=0.1,rely=0.40)


scale_size=Scale(frame1,label="Size :",orient=HORIZONTAL,from_=20,to=200,length=230,bg="#d6e0d2",troughcolor="#024e76",variable=size_var,command=change_size,relief="sunken")
                                                                                                                                        #flat, groove, raised, ridge, solid, or sunken
scale_size.place(relx=0,rely=0.48)
scale_size["highlightthickness"]=0




frame_algo_info=Frame(frame1,bg="#d8f1f3",width=230,height=150,relief="sunken",bd=4)
frame_algo_info.grid_propagate(0)
frame_algo_info.place(relx=0,rely=0.63)

label_avg=Label(frame_algo_info,bg="#d8f1f3",text=information[algo_var.get()],font=("comic sans ms",10,"bold"))
label_avg.pack_propagate(0)
label_avg.place(relx=0.02,rely=0.15)
label_credit=Label(frame1,text="by smeet kachhadiya",bg="#DEE6DB",fg="#99b299",font=("comic sans ms",12,"bold"))
label_credit.place(relx=0.02,rely=0.79)

label_note=Label(frame1,text="NOTE: please don't interrupt\n   the program while it is sorting.",bg="#DEE6DB")
label_note.place(relx=0,rely=0.91)


frame2=Frame(root,width=CANVAS_X,height=CANVAS_Y)
frame2.pack(side=LEFT)
canva=Canvas(frame2,width=CANVAS_X,height=CANVAS_Y,bg="#222222")
canva.pack()

numbers=[ randint(5,950) for i in range(40)]
shuffle(list(set(numbers)))
rec_width=CANVAS_X//size_var.get()
for num in numbers:
    canva.create_rectangle(starting_point,950-num,starting_point+rec_width,CANVAS_Y,fill="#aaaaaa")
    starting_point+=rec_width


root.mainloop()
