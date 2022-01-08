import canvas
import random

def main ():
    #setting up the 2 required options
    f =  (input("blue or teal sky"))
    if f == 'blue':
        x = 0.9
    else:
        x = 0.3
        
    d = (input('white or black door?'))
    if d == 'white': 
        y = 1
    else:
        y = 0
    

    canvas.set_size(500,500)
    canvas.set_fill_color(0.1,0.3,x)
    canvas.fill_rect(0,0,500,500)
    
    canvas.set_fill_color(.5,.8,0.1)
    canvas.fill_rect(0,0,500,150)
    
    canvas.set_fill_color(0.6,0.3,0.35)
    canvas.fill_rect(180,150,150,150)
    
    canvas.set_fill_color(1,1,1)
    
    
    canvas.set_fill_color(0.7,0.4,0.55)
    
    #Making a triangle for the roof
    canvas.begin_path()
    canvas.move_to(180,300)
    canvas.add_line(330,300)
    canvas.add_line(275,400)
    canvas.close_path()
    canvas.fill_path()
    
    canvas.set_fill_color(.58,.29,0)
    canvas.fill_rect(30,150,50,250)
    
    canvas.set_fill_color(0.63,0.85,0.43)
    canvas.fill_ellipse(30,370,90,90)
    canvas.fill_ellipse(1,370,90,90)
    canvas.fill_ellipse(15,430,90,90)
    
    #Door
    canvas.draw_rect(230,150,50,85)
    canvas.set_fill_color(y,y,y)
    canvas.fill_rect(230,150,50,85)
    
    canvas.set_fill_color(0.01,0.2,0.45)
    
    canvas.fill_rect(188,245,50,50)
    canvas.fill_rect(271,245,50,50)
    
    #Window Pannels    
    canvas.draw_rect(188,245,50,50)
    canvas.draw_rect(271,245,50,50)
    canvas.draw_rect(188,245,50,24)
    canvas.draw_rect(188,245,25,50)
    canvas.draw_rect(271,245,25,50)
    canvas.draw_rect(271,245,50,24)
    
    #sun
    canvas.set_fill_color(1,0.5,0)
    canvas.fill_ellipse(360,385,100,100)
    
    # SNOW IN AIR using Random Randit
    canvas.set_fill_color(1,1,1)
    for i in range(100):
        g = random.randint(0,500)
        h = random.randint(100,500)
        canvas.fill_ellipse(g,h,2,2)
        
    #SNOW ACCUMULATED ON THE FLOOR 
    for i in range(500):
        g = random.randint(0,500)
        h = random.randint(1,140)
        canvas.fill_ellipse(g,h,8,8)
    
    
    
    
main()
