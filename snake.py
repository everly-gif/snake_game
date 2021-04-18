import curses
from random import randint

#setup window
curses.initscr()
win= curses.newwin(20,60,0,0) #size of window which is in terms of y,x
win.keypad(1) #input from keyyboard
curses.noecho() #while program is running don't want to listen external inputs
curses.curs_set(0) #hide the cursor
win.border(0) #to draw a border at 0
win.nodelay(1)#-1

#snake and food
snake=[(4,10),(4,9),(4,8)] #a tuple is immutable
food=(10,20)

#game logic
score=0
win.addch(food[0],food[1],'#') 
ESC=27
key=curses.KEY_RIGHT
while key !=ESC:
    win.addstr(0,2,'Score '+str(score)+' ')
    win.timeout(150-(len(snake))//5+ len(snake)//10 %120) #increase speed

    prev_key=key
    event=win.getch() #event is a variable to get input from user
    key=event if event !=-1  else prev_key
    if key not in[curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_UP,curses.KEY_DOWN,ESC]:
        key=prev_key
    # calculate next coordinates
    y=snake[0][0]
    x=snake[0][1]

    if key==curses.KEY_DOWN:
        y+=1
    if key==curses.KEY_UP:
        y-=1
    if key==curses.KEY_LEFT:
        x-=1
    if key==curses.KEY_RIGHT:
        x+=1

    snake.insert(0,(y,x))#append for a list o(1) but this is o(n)  

    #check if we hit the border

    if y==0: break
    if y==19: break
    if x==0 : break
    if x==59: break

    #To check if snake runs over itself
    if snake[0] in snake[1:]:break
    
    if snake[0]==food: 
        #eat the food
        score+=1
        food=()
        while food ==():
            food=(randint(1,18), randint(1,58))
            if food in snake:
                food=()
        win.addch(food[0],food[1],'#') 
    else:
        #move snake
         last=snake.pop()    #removes last coordinate and removes it from array
         win.addch(last[0],last[1],' ')
    
    win.addch(snake[0][0],snake[0][1],'*')  
          
curses.endwin()    #destroying a window
print(f"Score= {score}") # pritning  score
