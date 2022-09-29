import turtle
import time
import random
import sys
from turtle import *
a=1
lap=""
he=input("Hello ")
if he=="hello"or he=="hi"or he=="Hello"or he=="Hi":
    x=input("Where are you from? ")
    y=input("Thats nice I love "+x +" I live in Antartica, how is your day going ")
    if y=="good" or y=="Good":
        b=input("Thats nice Im good aswell, do you want to play snake game? ")
        if b=="yes" or b=="Yes":
            a=2
        else:
            c=input("Okay do you want to play a game of dice, Ill win on even and you win on odd ")
            if c=="yes" or c== "Yes":
                a=3
            else:
                b=input("Thats fine do you want to play highlow instead? ")
                if b=="yes" or b== "Yes":
                    a=4
                else:
                    x=input("do you want to try out my fidget spinner then? ")
                    if x=="yes" or x== "Yes":
                        a=5
                    else:
                        print("Sorry I don't have anything else to play with, see me when you want to play with me again, bye for now.")
                        exit.sys("see you later.")
    elif y=="bad" or y== "Bad":
        b=input("Thats sad, I always like playing a game of snake game to cheer myself up do you want to play? ")
        if b=="yes" or b== "Yes":
            a=2
        else:
            c=input("Ok do you want to play a game of dice, Ill win on even you win on odd ")
            if c=="yes" or x== "Yes":
                a=3
            else:
                b=input("Thats fine do you want to play highlow instead? ")
                if b=="yes" or b== "Yes":
                    a=4
                else:
                    x=input("do you want to try out my fidget spinner then?(press down arrow key to spin) ")
                    if x=="yes" or x=="Yes":
                        a=5
                    else:
                        print("Sorry I dont have anything else to play with, see me when you want to play with me again, bye for now ")
                        exit.sys("see you later" )
    else:       
        print("Sorry I don't understand")
    




if a==2:
    delay = 0.1
    score = 0
    high_score = 0


    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("blue")
    wn.setup(width=600, height=600)
    wn.tracer(0)

    head = turtle.Turtle()
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    food = turtle.Turtle()
    colors = random.choice(['red', 'lime'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score : 0 High Score : 0", align="center",
            font=("candara", 24, "bold"))



    def group():
        if head.direction != "down":
            head.direction = "up"


    def godown():
        if head.direction != "up":
            head.direction = "down"


    def goleft():
        if head.direction != "right":
            head.direction = "left"


    def goright():
        if head.direction != "left":
            head.direction = "right"


    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y+20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y-20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x-20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x+20)


            
    wn.listen()
    wn.onkeypress(group, "Up")
    wn.onkeypress(godown, "Down")
    wn.onkeypress(goleft, "Left")
    wn.onkeypress(goright, "Right")

    segments = []




    while True:
        wn.update()
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red','lime'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)


            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white") 
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 1
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))

        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()

                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
        time.sleep(delay)

    wn.mainloop()

if a==5:
    turn=0
    def spinner():
        clear()
        angle=turn/10
        right(angle)
        forward(100)
        dot(120,"red")
        back(100)
        right(120)
        forward(100)
        dot(120,"green")
        back(100)
        right(120)
        forward(100)
        dot(120,"blue")
        back(100)
        right(120)
        update()
    def animate():
        global turn
        if turn>0:
            turn-=1
        spinner()
        ontimer(animate,20)
    def flick():
        global turn
        turn=turn+10
    setup(400,400,None,None)
    width(20)
    tracer(False)
    speed(0)
    onkey(flick,"Down")
    listen()
    animate()
    #spinner()
    done()

elif a==3:
    rolldie=input("So shall I roll the dice? ")
    while rolldie=="yes" or rolldie=="Yes":
        x=random.randint(1,6)
        y=random.randint(1,6)
        print(x)
        print(y)
        if (x+y)%2==0:
            print("Nice I won")
        else:
            print("Good job you won")
        rolldie=input("Do you want to roll again? ")
    if rolldie=="no" or rolldie=="No":
        lap=input("That was fun wanna put some stakes on it and play highlow ")
if lap=="yes" or lap=="Yes" or a==4:
    totalmoney=1000
    bottotalmoney=1000
    while totalmoney>0 and bottotalmoney>0:
        idk=input("Do you want to play? ")
        if idk=="no" or idk=="No":
            lap="no"
        if idk=="yes" or idk=="Yes":
            print("You currently have: ", totalmoney)
            print("And I have: ", bottotalmoney)
            money=int(input("how much money do you want to bet? "))
            number=[1,2,3,4,5,6,7,8,9,10]
            numbers=random.choice(number)
            trys=1
            if totalmoney>=money and bottotalmoney>=money:
                while trys<=3:
                    y=int(input("guess a number from one to 10 "))
                    if y==numbers:
                        print("BINGO")
                        totalmoney= totalmoney+money
                        bottotalmoney= bottotalmoney-money
                        print("Damn your good at this!!")
                        break
                    elif y<numbers:
                        print("too low")
                        trys+=1
                    elif y>numbers:
                        print("too high")
                        trys+=1
                    if trys==4:
                        print("GAME OVER")
                        totalmoney=totalmoney-money
                        bottotalmoney=bottotalmoney+money

                    elif totalmoney<money:
                        print("you dont have enouguh money to do that")
                    elif bottotalmoney<money:
                        print("Sorry i dont have enoguh money to do that")
                    elif bottotalmoney==0:
                        a=input("im all out of money wanna play a diffrent game? ")
                        lap="no"
                    elif totalmoney==0:
                        wanna=input("your out of money wanna do somthing else? ")
                        if wanna=="yes" or a==5 or wanna=="Yes":
                            print("cool lets try my fidget spinner(click down arrow key to spin)")
                            a=5 


                        else:
                            b=input("Okay do you want to play snake game instead? ")
                            if b=="yes" or b=="Yes":
                                a=2
                            else:
                                c=input("Ok do you want to play a game of dice, Ill win on even you win on odd ")
                                if c=="yes" or c== "Yes":
                                    a=3
                                else:
                                    b=input("Thats fine do you want to play highlow instead? ")
                                    if b=="yes" or b== "Yes":
                                        a=4
                                    else:
                                        print("Sorry I dont have anything else to play with, see me when you want to play with me again, bye for now ")
                                        exit.sys("see you later" )
                            

        elif lap=="no" or x== "No":
            b=input("Okay do you want to play snake game instead? ")
            if b=="yes" or b== "Yes":
                a=2
            else:
                c=input("Ok do you want to play a game of dice, Ill win on even you win on odd ")
                if c=="yes" or c== "Yes":
                    a=3
                else:
                    x=input("do you want to try out my fidget spinner then? (press down arrow key to spin) ")
                    if x=="yes" or x== "Yes":
                            a=5
                    else:
                        print("Sorry I dont have anything else to play with, see me when you want to play with me again, bye for now ")
                        exit.sys("see you later" )



