#Code written from scratch by Noureldin Khalil.

import turtle as t

pixel_size = 30
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

def initialize():
    t.tracer(False) #Turn off the turtle animation, comment out this line to see the turtle draw the grid
    t.speed(10)
    t.penup()
    t.goto(-(pixel_size*columns)/2,(pixel_size*(rows/2))) #Go to the top left corner of the grid
    t.setheading(0)
    t.pensize(1)
    t.fillcolor("white")
    t.pencolor("black")
    t.pendown()

def draw_pixel(): #Draw a single pixel
    t.setheading(0)
    counter = 0
    while counter < 4: #Draw a square
        t.forward(pixel_size)
        t.left(90)
        counter += 1
    t.forward(pixel_size) #Move to the next pixel

def draw_row(): #Draw a row of pixels which is the same as the number of columns
    pixel_counter = 0
    while pixel_counter < columns: #Draw the number of pixels in a row
        draw_pixel()
        pixel_counter += 1

def next_row(): #Move to the next row
    currentX = t.xcor()
    currentY = t.ycor()
    t.penup()
    t.goto(currentX - (pixel_size*columns), currentY - pixel_size) #Subtract the number of columns * pixel_size to go to the leftmost column of the row, then go 1 pixel down
    t.pendown()

#*********** Unnecessary section ***********
#Did this as an extra challenge just to label the rows and columns.

def lable_rows(): #Label the row
    t.penup()
    t.goto(-((pixel_size * columns)/2) - pixel_size*3, 0 + pixel_size) #Go to the leftmost column of the grid and go up 1 pixel
    t.write("Rows", font=("Arial", 12, "normal"), align="center") #Write the row number
    t.goto(-((pixel_size * columns)/2) - pixel_size, (pixel_size * (rows/2)) + (pixel_size/4))
    for i in range(0, rows):
        t.pendown()
        t.write(f"{i + 1}", font=("Arial", 12, "normal"), align="center") #Write the row number
        t.penup()
        t.setheading(270)
        t.forward(pixel_size)

def lable_columns(): #Label the row
    t.penup()
    t.goto(0, (pixel_size * (rows/2)) + (pixel_size * 2.25))
    t.write("Columns", font=("Arial", 12, "normal"), align="center") #Write the row number
    t.goto(-((pixel_size * columns)/2) + pixel_size/2, (pixel_size * (rows/2)) + (pixel_size * 1.25))
    for i in range(0, columns):
        t.pendown()
        t.write(f"{i + 1}", font=("Arial", 12, "normal"), align="center") #Write the row number
        t.penup()
        t.setheading(0)
        t.forward(pixel_size)

#********************************************

def draw_grid(rows): #Draw the grid
    for i in range(0, rows):
        draw_row()
        next_row()
    center_dot()
    lable_rows()
    lable_columns()

def center_dot(): #Draw a red dot in the center of the grid
    t.penup()
    t.goto(0, (pixel_size * ((rows/2) + 1)) - (pixel_size * rows/2) - 5)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

def main(): #Main function
    initialize()
    draw_grid(rows)
    t.hideturtle()
    t.exitonclick()

if __name__ == "__main__":
    main()