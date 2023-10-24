"""Paint a scene using Turtle graphics."""
from turtle import Turtle, done


def rectangle(t: Turtle, width: int, height: int, x: int, y: int) -> None:
    """Draw a rectangle with the given width and height."""
    idx = 0
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    while idx < 2:
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        idx += 1
    t.end_fill()    


def circle(t: Turtle, size: int, x: int, y: int) -> None:
    """Draw a circle with the given size."""
    idx = 0
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    while idx < 75:
        t.forward(size)
        t.right(5)
        idx += 1
    t.end_fill()
    

def triangle(t: Turtle, side_length: int, x: int, y: int) -> None:
    """Draw an equilateral triangle with the given side length."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    idx = 0
    while idx < 3:
        t.forward(side_length)
        t.left(120)
        idx += 1
    t.end_fill()


def lollipop(t: Turtle, size: float, x: int, y: int, fill_color: str, pen_color: str) -> None:
    """Draw a lolipop of given size and color."""
    # draw the stick
    stick_height = size * 25
    stick_width = size
    stick_x = x + (size * 10)
    stick_y = y
    t.color("brown")
    t.penup()
    t.goto(stick_x, stick_y)
    t.pendown()
    t.begin_fill()
    t.forward(stick_width)
    t.right(90)
    t.forward(stick_height)
    t.right(90)
    t.forward(stick_width)
    t.right(90)
    t.forward(stick_height)
    t.end_fill()
    # draw the candy
    idx = 0
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(fill_color)
    t.begin_fill()
    while idx < 75:
        t.forward(size)
        t.right(5)
        idx += 1
    idx = 0
    t.hideturtle()
    t.end_fill()
    t.color(pen_color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(0)
    while idx < 200:
        t.forward(size)
        t.right(5.25)
        size *= 0.99
        idx += 1


def main() -> None:
    """Draw lollipop mountains."""
    leo = Turtle()
    bob = Turtle()
    bob.speed(0)
    charles = Turtle()
    charles.speed(0)
    papi = Turtle()
    papi.speed(0)
    kiki = Turtle()
    kiki.speed(0)
    hellen = Turtle()
    hellen.speed(0) 
    lauren = Turtle()
    lauren.speed(0)
    julia = Turtle()
    julia.speed(0)
    brett = Turtle()
    brett.speed(0)
    piere = Turtle()
    piere.speed(0)
    jackson = Turtle()
    jackson.speed(0)
    leo.speed(0)
    # draw the sky
    leo.color("sky blue") 
    rectangle(leo, 720, 600, -360, -300)
    # draw the grass
    leo.color("green")
    rectangle(leo, 720, 100, -360, -400)
    # draw the mountains
    leo.color("gray")
    triangle(leo, 360, -360, -300)
    triangle(leo, 360, 10, -300)
    # draw the sun
    leo.color("yellow")
    circle(leo, 3, 200, 200)
    # draw lollipop trees
    lollipop(bob, 1.5, -125, -175, "red", "pink")
    lollipop(charles, 1.5, 75, -175, "blue", "purple")  
    lollipop(papi, 1.5, -300, -250, "light green", "orange") 
    lollipop(kiki, 1.5, 300, -250, "orange", "pink")
    lollipop(hellen, 1.5, -250, -150, "white", "red")
    lollipop(lauren, 1.5, 250, -150, "pink", "white")
    lollipop(julia, 1.5, -200, -80, "purple", "light green")
    lollipop(brett, 1.5, 180, -80, "black", "orange")
    lollipop(piere, 1.5, -165, -225, "yellow", "purple")
    lollipop(jackson, 1.5, 170, -225, "light blue", "black")

    
if __name__ == "__main__":
    main()


done()