import turtle
import random
import math

# Initialize screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Concentric Squares")

# Create a turtle for drawing
draw_turtle = turtle.Turtle()
draw_turtle.speed(0)  # Fastest drawing speed
draw_turtle.hideturtle()
draw_turtle.penup()


num_squares = 10
size_increment = 20
starting_size = 10
min_color_diff = 100  # Minimum color difference to avoid overlap

# Function to convert hex color to RGB
def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

# Function to calculate the Euclidean distance between two colors
def color_distance(color1, color2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))

# Function to generate a list of distinct colors
def generate_distinct_colors(num_colors, min_diff):
    colors = []
    while len(colors) < num_colors:
        new_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_rgb = hex_to_rgb(new_color)
        if all(color_distance(new_rgb, hex_to_rgb(c)) >= min_diff for c in colors):
            colors.append(new_color)
    return colors

# Generate distinct colors
distinct_colors = generate_distinct_colors(num_squares, min_color_diff)

# Draw concentric squares with distinct colors from outside to inside
def draw_squares():
    sizes = [starting_size + i * size_increment for i in range(num_squares)]
    sizes.sort(reverse=True)  # Sort sizes from largest to smallest
    
    for i, size in enumerate(sizes):
        draw_turtle.goto(-size / 2, size / 2)
        draw_turtle.pendown()
        
        color = distinct_colors[i]
        
        draw_turtle.color(color)
        draw_turtle.begin_fill()  # Start filling the color
        
        for _ in range(4): 
            draw_turtle.forward(size)
            draw_turtle.right(90)
        
        draw_turtle.end_fill()  # End filling the color
        draw_turtle.penup()

# Draw squares and save their details
squares = []
def draw_squares_and_save():
    sizes = [starting_size + i * size_increment for i in range(num_squares)]
    sizes.sort(reverse=True)  # Sort sizes from largest to smallest
    
    for i, size in enumerate(sizes):
        draw_turtle.goto(-size / 2, size / 2)
        draw_turtle.pendown()
        
        color = distinct_colors[i]
        
        draw_turtle.color(color)
        draw_turtle.begin_fill()
        
        for _ in range(4):  # Drawing each square with four sides
            draw_turtle.forward(size)
            draw_turtle.right(90)
        
        draw_turtle.end_fill()
        draw_turtle.penup()
        squares.append((draw_turtle.pos(), size, color))

draw_squares_and_save()

# Set up click handler
def on_click(x, y):
    for pos, size, color in squares:
        half_size = size / 2
        if -half_size < x < half_size and -half_size < y < half_size:
            draw_turtle.goto(pos)
            draw_turtle.color("red")  # Color of the selected square
            draw_turtle.begin_fill()
            
            for _ in range(4):  # Redraw the square with the new color
                draw_turtle.forward(size)
                draw_turtle.right(90)
            
            draw_turtle.end_fill()
            draw_turtle.penup()
            break

screen.onclick(on_click)


screen.mainloop()
