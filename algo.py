import time
import random
ac,cmp=0,0
def algochooser(numbers,paint,label_access,label_comparison,something):
    global ac,cmp

    if something=="bubble sort":
        label_access.configure(text="array access:0")
        label_comparison.configure(text="comparison:0")
        bubblesort(numbers,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="selection sort":
        label_access.configure(text="array access:0")
        label_comparison.configure(text="comparison:0")
        selectionsort(numbers,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="insertion sort":
        label_access.configure(text="array access:0")
        label_comparison.configure(text="comparison:0")
        insertionsort(numbers,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="merge sort":
        label_access.configure(text="array access:0")
        label_comparison.configure(text="comparison:0")
        mergesort(numbers,0,len(numbers),paint,label_access,label_comparison)
        paint(numbers,["green" for x in numbers])
        ac,cmp=0,0

    elif something=="heap sort":
        label_access.configure(text="array access:0")
        label_comparison.configure(text="comparison:0")
        heapsort(numbers,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="quick sort":
        label_access.configure(text="array access:"+str(ac))
        label_comparison.configure(text="comparison:0")
        quicksort(numbers,0,len(numbers)-1,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="shell sort":
        label_access.configure(text="array access:" + str(ac))
        label_comparison.configure(text="comparison:0")
        shellsort(numbers,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="radix sort":
        label_access.configure(text="array access:"+str(ac))
        label_comparison.configure(text="comparison:0")
        radixsort(numbers,paint,label_access)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="cocktail shaker":
        label_access.configure(text="array access:"+str(ac))
        label_comparison.configure(text="comparison:0")
        cocktailshakersort(numbers,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

    elif something=="gnome sort":
        label_access.configure(text="array access:" + str(ac))
        gnomesort(numbers,paint,label_access)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0
    elif something=="odd-even sort":
        label_access.configure(text="array access:" + str(ac))
        label_comparison.configure(text="comparison:0")
        oddevensort(numbers,paint,label_access,label_comparison)
        paint(numbers, ["green" for x in numbers])
        ac,cmp=0,0

def bubblesort(number,paint,label_access,label_comparison):

    global cmp,ac

    colors=[]
    for i in range(len(number)-1):
        for j in range(len(number)-1-i):
            swapped=False
            if(number[j]>number[j+1]):
                swapped=True
                number[j],number[j + 1]=number[j+1],number[j]
            # --------------------------------------------
            cmp += 1
            ac += 6
            colors=["#cc0000"if x==number[j] or x==number[j+1] else"#aaaaaa" for x in number]
            paint(number,colors)
            label_access.configure(text="array access:"+str(ac))
            label_comparison.configure(text="comparison:"+str(cmp))
            # ---------------------------------------------
        if not swapped:
            break

def selectionsort(number,paint,label_access,label_comparison):

    global cmp,ac
    colors=[]
    for i in range(len(number)-1):
        for j in range(i+1,len(number)):
            if (number[i]>number[j]):
                number[i],number[j]=number[j],number[i]

            # -----------------------------------------------
            ac += 6
            cmp += 1
            colors=["#cc0000"if  x==number[j] else "#aaaaaa" if x!=number[i] else "green" for x in number]
            paint(number,colors)
            label_access.configure(text="array access:"+str(ac))
            label_comparison.configure(text="comparison:" + str(cmp))
            #-------------------------------------------------

def insertionsort(number,paint,label_access,label_comparison):
    
    global cmp,ac
    colors=[]
    for i in range(1,len(number)):
        current=number[i]
        ac+=1
        y=i-1;
        while(y>=0 and number[y]>current):
            number[y+1]=number[y]
            y-=1
            ac+=3
            cmp+=1
            #----------------------------------------------------------
            for gh in range(len(number)):
            	if y==gh:
            		colors.append("#cc0000")
            	elif gh==i:
            		colors.append("green")
            	else:
            		colors.append("#aaaaaa")
            paint(number,colors)
            colors=[]
            label_access.configure(text="array access:"+str(ac))
            label_comparison.configure(text="comparison:" + str(cmp))
            #------------------------------------------------------------
        number[y+1]=current
        ac+=1
        #-----------------------------------------------------------
        label_access.configure(text="array access:" + str(ac))
        label_comparison.configure(text="comparison:" + str(cmp))
        #-----------------------------------------------------------
        

def mergesort(number,left,right,paint,label_access,label_comparison):
    if left<right:
        middle=(left+right)//2
        mergesort(number,left,middle,paint,label_access,label_comparison)
        mergesort(number,middle+1,right,paint,label_access,label_comparison)
        merge(number,left,middle,right,paint,label_access,label_comparison)

def merge(number,left,middle,right,paint,label_access,label_comparison):
    global cmp,ac
    si=fi=0
    colors=[]
    firstlist=number[left:middle+1]
    secondlist=number[middle+1:right+1]
    ac+=2

    label_access.configure(text="array access:" + str(ac))

    for ai in range(left,right+1):
        if(fi<len(firstlist) and si<len(secondlist)):
            if(firstlist[fi]<secondlist[si]):
                number[ai]=firstlist[fi]
                fi+=1
                ac+=1
                cmp+=1
            else:
                number[ai]=secondlist[si]
                si+=1
                ac+=1
        elif(fi<len(firstlist)):
            number[ai]=firstlist[fi]
            fi+=1
            ac+=1
        elif(si<len(secondlist)):
            number[ai]=secondlist[si]
            si+=1
            ac+=1
        #---------------------------------------------------------
        for x in range(len(number)):
            if x>middle and x<=right:
                colors.append("yellow")
            elif x>=left and x<=middle:
                colors.append("teal")
            else:
                colors.append("#aaaaaa")

        paint(number,colors )

        label_access.configure(text="array access:"+str(ac))
        label_comparison.configure(text="comparison:" + str(cmp))
        #-----------------------------------------------------------

def heapsort(number,paint,label_access,label_comparison):
    global ac,cmp
    n=len(number)//2
    colors=[]

    for i in range(n,-1,-1):
        heapify(number,len(number),i,paint,label_access,label_comparison)

    for i in range(len(number)-1,-1,-1):
        number[i],number[0]=number[0],number[i]
        ac+=4
        #----------------------------------------------------------------
        colors=["green"if x==number[i] else "#aaaaaa" for x in number]
        paint(number,colors)
        label_access.configure(text="array access:"+str(ac))
        #----------------------------------------------------------------
        heapify(number,i,0,paint,label_access,label_comparison)

def heapify(number,limit,parent,paint,label_access,label_comparison):
    global  ac,cmp
    colors=[]
    largest=parent
    left=2*parent
    right=2*parent+1

    if(left<limit and number[left]>number[largest]):
        largest=left
        ac+=2
        cmp+=1
    if(right<limit and number[right]>number[largest]):
        largest=right
        ac+=2
        cmp+=1
    if(largest!=parent):
        number[largest],number[parent]=number[parent],number[largest]
        ac+=4
        #-------------------------------------------------------------------
        for i in range(len(number)):
            if number[i]==number[parent]:
                colors.append("yellow")
                ac+=2
            elif number[i]==number[left] or number[i]==number[right]:
                colors.append("#cc0000")
                ac+=4
            else:
                if i==limit:
                    colors.append("green")
                else:
                    colors.append("#aaaaaa")
        paint(number,colors)
        label_access.configure(text="array access:" + str(ac))
        label_comparison.configure(text="comparison:" + str(cmp))
        #--------------------------------------------------------------------------
        heapify(number,limit,largest,paint,label_access,label_comparison)

def quicksort(number,left,right,paint,label_access,label_comparison):
    color=[]

    if(left<right):
        mid=partition(number,left,right,paint,label_access,label_comparison)
        quicksort(number,left,mid-1,paint,label_access,label_comparison)
        quicksort(number,mid+1,right,paint,label_access,label_comparison)

def partition(number,low,high,paint,label_access,label_comparison):
    global  ac,cmp
    tracker=low
    pivot=number[high]
    #----------------------------------------------------------
    ac+=1
    color=[]
    for i in range(len(number)):
        if i==low and i==high-1:
            color.append("#cc0000")
        elif i == high:
            color.append("yellow")
        else:
            color.append("#aaaaaa")
    paint(number,color)
    label_access.configure(text="array access:"+str(ac))
    label_comparison.configure(text="comparison:" + str(cmp))
    #----------------------------------------------------------
    for i in range(low,high,1):
        if number[i]<=pivot:
            number[i],number[tracker]=number[tracker],number[i]
            tracker+=1
            color=[]
            ac+=5
            cmp+=1
        #---------------------------------------------------------
        for i in range(len(number)):
            if i==low or i==high-1:
                color.append("#cc0000")
            elif i==high:
                color.append("yellow")
            else:
                color.append("#aaaaaa")
        paint(number,color)
        label_access.configure(text="array access:" + str(ac))
        label_comparison.configure(text="comparison:" + str(cmp))
        #-----------------------------------------------------------

    number[tracker],number[high]=number[high],number[tracker]
    #------------------------------------------------------------------
    ac+=4
    label_access.configure(text="array access:" + str(ac))
    label_comparison.configure(text="comparison:" + str(cmp))
    #------------------------------------------------------------------
    return tracker

def shellsort(number,paint,label_access,label_comparison):
    global ac,cmp
    length=len(number)
    gap=length//2
    while gap>0: #loop until gap #cc0000uced to 1. -if array size is 20 then gap=10,5,2,1
        for x_sort in range(gap,length):#loop srart from gap bcoz we are using j=x_sort-gap

            j=x_sort-gap #initial j will be 0 x_sort=gap so j=x_sort-x_sort=0
            paint(number, ["#cc0000" if xy == j + gap or xy == j else "#aaaaaa" for xy in range(len(number))])
            while j>=0:#if you swap element then go back by gap(j-=gap) and swap and if you haven't swapped then break the loop so you can go forward
                if(number[j+gap]<number[j]):
                    number[j + gap],number[j]=number[j],number[j + gap]
                    ac+=6
                    cmp+=1
                else:
                    break
                paint(number, ["#cc0000" if xy == j + gap or xy == j else "#aaaaaa" for xy in range(len(number))])
                label_access.configure(text="array access:" + str(ac))
                label_comparison.configure(text="comparison:" + str(cmp))
                j-=gap
        gap//=2
ac=0
def countsort(number,exp,paint,label_access):
    global  ac
    count=[0]*10
    temp=[0]*len(number)
    for x in range(len(number)):
        count[(number[x]//exp)%10]+=1
        ac+=1

    for y in range(1,len(count)):
        count[y]+=count[y-1]
    for z in range(len(number)-1,-1,-1):
        index=count[(number[z]//exp)%10]
        temp[index-1]=number[z]
        count[(number[z]//exp)%10]-=1

        ac+=3
        label_access.configure(text="array access:" + str(ac))
    #time.sleep(0.2)
    for w in range(len(temp)):
        number[w]=temp[w]
        ac+=1
    label_access.configure(text="array access:" + str(ac))
    paint(number,["#aaaaaa" for h in number])

    time.sleep(0.5)

def radixsort(number,paint,label_access):
    maximum=max(number)
    exp=1
    while(maximum//exp>=1):
        countsort(number,exp,paint,label_access)
        #paint(number, ["#aaaaaa" for h in number])
        #time.sleep(0.1)
        exp*=10
ac=0
def cocktailshakersort(number,paint,label_access,label_comparison):
    first,last=0,len(number)
    swapped=True
    colors=[]
    global  ac,cmp
    while swapped:
        swapped=False
        for x in range(first,last-1):
            if number[x]>number[x+1]:
                number[x],number[x + 1]=number[x+1],number[x]
                ac+=6
                cmp+=1
                swapped=True
            colors=[]
            for gh in range(len(number)):
                if number[gh]==number[x] or number[gh]==number[x+1]:
                    colors.append("#cc0000")
                else:
                    colors.append("#aaaaaa")
            paint(number,colors)
            label_access.configure(text="array access:" + str(ac))
            label_comparison.configure(text="comparison:" + str(cmp))
        if not swapped:
            break
        last-=1
        for y in range(last-1,first-1,-1):
            if number[y+1]<number[y]:
                number[y + 1],number[y]=number[y],number[y+1]
                swapped=True
                ac+=6
                cmp+=1
            colors=[]
            for gh in range(len(number)):
                if number[gh] == number[y] or number[gh] == number[y + 1]:
                    colors.append("#cc0000")
                else:
                    colors.append("#aaaaaa")
            paint(number,colors)
            label_access.configure(text="array access:" + str(ac))
            label_comparison.configure(text="comparison:" + str(cmp))
        first+=1

def gnomesort(number,paint,label_access):
    i,length=0,len(number)
    colors=[]
    while(i<length):
        if i==0:
            i+=1
        if(number[i]>=number[i-1]):

            
            for gh in number:
            	# print(gh)
	            if(gh==number[i]):
	            	colors.append("#cc0000")
	            else:
	            	colors.append("#aaaaaa")
            paint(number,colors)
            colors=[]
            i += 1
        else:
            number[i],number[i-1]=number[i-1],number[i]
            for gh in number:
	            if(gh==number[i]):
	            	colors.append("#cc0000")
	            else:
	            	colors.append("#aaaaaa")
            paint(number,colors)
            colors=[]
            i -= 1
    
ac=0
def oddevensort(number,paint,label_access,label_comparison):
    global ac,cmp
    length=len(number)
    is_sort=False
    while is_sort==False:
        is_sort=True
        colors=[]
        for x in range(0,length-1,2):
            if number[x]>number[x+1]:
                number[x],number[x+1]=number[x+1],number[x]
                ac+=1
                cmp+=1
                is_sort=False
                colors=[ "#cc0000" if v==x or v==x+1 else "#aaaaaa" for v in range(len(number))]
                paint(number,colors)
                label_access.configure(text="array access:" + str(ac))
                label_comparison.configure(text="comparison:" + str(cmp))
        for y in range(1,length-1,2):
            if number[y]>number[y+1]:
                number[y],number[y+1]=number[y+1],number[y]
                ac+=6
                cmp+=1
                is_sort=False
                colors = ["#cc0000" if v == y or v == y + 1 else "#aaaaaa" for v in range(len(number))]
                paint(number, colors)
                label_access.configure(text="array access:" + str(ac))
                label_comparison.configure(text="comparison:" + str(cmp))