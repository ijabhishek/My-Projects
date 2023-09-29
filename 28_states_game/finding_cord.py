import pandas
import turtle

screen = turtle.Screen()
screen.title("India States Game")

image = "india_map.gif"
turtle.addshape(image)
turtle.shape(image)
#--for getting x and y cordinates ---
def get_mouse_click_cordinates(x,y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_cordinates)
turtle.mainloop()


