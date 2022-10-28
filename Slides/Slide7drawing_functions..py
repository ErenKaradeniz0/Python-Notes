from DrawingPanel import *
panel = DrawingPanel(400, 400, background="gray")


def worm():
    for i in range(1, 11):
        panel.fill_oval(100+20*i, 5+20*i, 50, 50, "red")


def circles():
    for i in range(1, 11):
        panel.draw_oval(100, 100, 22*i, 22*i, "magenta")


def draw_car():
    panel.fill_rect(10, 30, 100, 50, "black")
    panel.fill_oval(20, 70, 20, 20, "red")
    panel.fill_oval(80, 70, 20, 20, "red")
    panel.fill_rect(80, 40, 30, 20, "cyan")


def my_function_top():
    for i in range(0, 20):
        panel.draw_rectangle(20, 20+10*i, 200-10*i, 10)


def my_function_left():
    for i in range(0, 10):
        panel.draw_rectangle(20+10*i, 20+10 * i, 100-10*i, 10)

def my_function_bottom():
    for i in range(0, 10):
        panel.draw_rectangle(110-10*i, 20+10 * i, 10+10*i, 10)
        
my_function_bottom()
