import turtle
import time

# Setup the screen for turtle graphics
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Supercomputers and Operating System Requirements")

# Function to draw a rectangle (representing components)
def draw_rectangle(t, x, y, width, height, label, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    
    t.end_fill()
    
    # Write the label inside the rectangle
    t.penup()
    t.goto(x + width / 2, y + height / 4)
    t.pendown()
    t.color("black")
    t.write(label, align="center", font=("Arial", 12, "normal"))
    time.sleep(1)  # Wait for 1 second after drawing each rectangle

# Function to display requirements of OS
def display_requirements(t, requirements):
    y_offset = -150  # Initial y-position for requirements
    t.penup()
    for req in requirements:
        t.goto(0, y_offset)  # Set position for requirement
        t.pendown()
        t.color("black")
        t.write(req, align="center", font=("Arial", 16, "bold"))
        t.penup()  # Lift the pen up to avoid drawing lines
        time.sleep(1)  # Wait for 1 second to read the requirement
        y_offset -= 30  # Move down for next requirement

# Function to animate supercomputer architecture
def animate_supercomputer():
    pen = turtle.Turtle()
    pen.speed(0)

    # Draw the title at the top of the screen
    pen.penup()
    pen.goto(0, 250)  # Adjusted position for the title at the top
    pen.pendown()
    pen.write("Operating Systems: Backbone of Supercomputers", align="center", font=("Arial", 18, "bold"))

    # Draw nodes (representing processing units) with varying colors
    node_positions = [(-200, 100), (-100, 100), (0, 100), (100, 100), (200, 100)]
    
    # Distinct colors and labels for each node
    node_details = [
        ("Node 1", "lightgreen"),
        ("Node 2", "lightblue"),
        ("Node 3", "lightyellow"),
        ("Node 4", "lightcoral"),
        ("Node 5", "lightpink")
    ]
    
    for i, (label, color) in enumerate(node_details):
        draw_rectangle(pen, node_positions[i][0], node_positions[i][1], 60, 40, label, color)

    # Draw storage unit
    draw_rectangle(pen, -100, -50, 120, 40, "Storage", "orange")

    # Draw lines connecting nodes with animation
    for i in range(len(node_positions) - 1):
        pen.penup()
        pen.goto(node_positions[i][0] + 30, node_positions[i][1])  # Move to the middle of the node
        pen.pendown()
        pen.goto(node_positions[i + 1][0] - 30, node_positions[i + 1][1])  # Connect to next node
        time.sleep(1)  # Wait for a second between each line drawing

    # Display requirements of OS
    requirements = [
        "High Performance",
        "Scalability",
        "Efficient Resource Management",
        "Fault Tolerance",
        "Parallel Processing Support",
        "Advanced Scheduling Algorithms"
    ]
    
    display_requirements(pen, requirements)

# Run the animation
animate_supercomputer()

# Keep the window open
screen.mainloop()
