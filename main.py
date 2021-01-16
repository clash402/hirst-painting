import random
import turtle as t

# import colorgram
# colors = colorgram.extract('./images/kirby-star-allies.jpg', 30)
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

colors = [(35, 33, 138), (20, 19, 82), (132, 159, 208), (225, 122, 163), (251, 154, 197), (205, 226, 244),
          (63, 76, 156), (74, 98, 216), (248, 212, 85), (251, 192, 229), (136, 25, 47), (200, 91, 133), (156, 58, 95),
          (216, 153, 96), (247, 231, 200), (149, 87, 52), (75, 16, 39), (229, 245, 239), (166, 179, 232), (218, 83, 70),
          (112, 222, 248), (70, 21, 12), (184, 138, 51), (31, 46, 239), (126, 32, 27), (118, 192, 138), (243, 168, 151),
          (130, 228, 180), (91, 69, 25), (3, 8, 4)]

t.colormode(255)

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.pendown()
    tim.dot(20, random.choice(colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
