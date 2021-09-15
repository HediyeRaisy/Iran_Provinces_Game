import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Iran Provinces Game")
img = "iran.gif"
screen.addshape(img)
turtle.shape(img)

#for find location on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("provinces.csv")
provinces = []

game_is_on = True
c=0
data_list = data["province"].to_list()
while game_is_on:
    answer = screen.textinput(title="Guess the Province",prompt="What's another province?").capitalize()

    for i in data_list:
        if i == answer:
            d = data[data.province == answer]
            x = int(d.x)
            y = int(d.y)
            provinces.append(Turtle())
            provinces[c].penup()
            provinces[c].hideturtle()
            provinces[c].goto(x,y)
            provinces[c].color("Black")

            provinces[c].write(f"{answer} ", move=False, align="center", font=("Arial",6, "bold"))
            c += 1


screen.exitonclick()
