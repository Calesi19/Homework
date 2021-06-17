import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.

    width = 800
    height = 500

    draw_sky(canvas, width, height)
    draw_floor(canvas, width, height)
    draw_cloud(canvas, height)
    draw_pebble(canvas, height)
    draw_tree(canvas, width, height)
    draw_grass_blade(canvas, height, width)
    draw_fence(canvas, width, height)
    


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_pebble(canvas, height):
    canvas.create_oval(90, height - 100, 200, height - 150, outline="#1c2123", fill="#63747b", width=2)
    canvas.create_oval(110, height - 80, 210, height - 130, outline="#1c2123", fill="#63747b", width=2)

def draw_sky(canvas, width, height):
    canvas.create_rectangle(0, 0, width, height, outline="#006fff", fill="#3c7ec3", width=2)

def draw_cloud(canvas, height):
    canvas.create_oval(90, height - 400, 200, height - 450, outline="#FEFFFF", fill="#FEFFFF", width=2)
    canvas.create_oval(110, height - 400, 210, height - 430, outline="#FEFFFF", fill="#FEFFFF", width=2)
    canvas.create_oval(300, height - 400, 200, height - 450, outline="#FEFFFF", fill="#FEFFFF", width=2)
    canvas.create_oval(350, height - 400, 210, height - 430, outline="#FEFFFF", fill="#FEFFFF", width=2)
    canvas.create_oval(600, height - 400, 700, height - 450, outline="#FEFFFF", fill="#FEFFFF", width=2)
    canvas.create_oval(550, height - 425, 775, height - 350, outline="#FEFFFF", fill="#FEFFFF", width=2)

def draw_grass_blade(canvas, height, width):
    
    for i in range(0, width, 20):
        canvas.create_rectangle(i, height - 20, i + 10, height - 70, outline="#136e30", fill="#1b9d44")
    for i in range(0, width, 15):
        canvas.create_rectangle(i, height, i + 10, height - 50, outline="#136e30", fill="#1b9d44")
    

def draw_fence(canvas, width, height):
    for i in range(0, width, 20):
        canvas.create_rectangle(i, height - 200, i + 10, height - 250, outline="#FFFFFF", fill="#FFFFFF")
    canvas.create_rectangle(0, height - 245, width, height - 250, outline="#181818", fill="#FFFFFF")
    canvas.create_rectangle(0, height - 220, width, height - 225, outline="#181818", fill="#FFFFFF")


def draw_floor(canvas, width, height):
    canvas.create_rectangle(0, height - 200, width, height, outline="#006fff", fill="#219b23", width=2)


def draw_tree(canvas, width, height):
    points = [width - 275, height - 400,width - 330, height - 265,width - 220, height - 265]
    canvas.create_rectangle(width - 300, height - 200, width - 250, height - 300, outline="#6c6122", fill="#6c6122", width=2)
    canvas.create_polygon(points, outline='#047000', fill='#047000', width=2)
    

# Call the main function so that
# this program will start executing.
main()