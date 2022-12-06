import turtle

class Turtle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.fillcolor("white")
        self.t.pencolor("white")
        window = turtle.Screen()
        window.bgcolor("black")
    def line(self, direction, steps, angle):

        def switch(direction):
            if direction == "right":
                self.t.right(angle)
            if direction == "left":
                self.t.left(angle)
        
        switch(direction)
        self.t.forward(steps)


def main():
    height = input("please provide a height for your screen\n")
    width = input("please provide a width for your screen\n")

    height = int(height)
    width = int(width)

    if width < 1:
        print('please add a positive integer for width')
        return

    if height < 1:
        print('please add a positive integer for height')
    t = Turtle()

    triangle = [
        {
            "direction": "left",
            "steps": 500,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 500,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 500,
            "angle": 120
        }
    ]

    for line in triangle:
        t.line(line["direction"], line["steps"], line["angle"])

    triangle = [
        {
            "direction": "left",
            "steps": 250,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 250,
            "angle": 120
        },
        {
            "direction": "right",
            "steps": 250,
            "angle": 120
        },
        {
            "direction": "right",
            "steps": 250,
            "angle": 120
        }
    ]


    for line in triangle:
        t.line(line["direction"], line["steps"], line["angle"])

    
    triangle = [
        {
            "direction": "right",
            "steps": 125,
            "angle": 120
        },
        {
            "direction": "right",
            "steps": 125,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 125,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 125,
            "angle": 120
        }
    ]

    for line in triangle:
        t.line(line["direction"], line["steps"], line["angle"])

        
    triangle = [
        {
            "direction": "left",
            "steps": 62.5,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 62.5,
            "angle": 120
        },
        {
            "direction": "right",
            "steps": 62.5,
            "angle": 120
        },
        {
            "direction": "right",
            "steps": 62.5,
            "angle": 120
        }
    ]

    for line in triangle:
        t.line(line["direction"], line["steps"], line["angle"])


    triangle = [
        {
            "direction": "right",
            "steps": 31.25,
            "angle": 120
        },
        {
            "direction": "right",
            "steps": 31.25,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 31.25,
            "angle": 120
        },
        {
            "direction": "left",
            "steps": 31.25,
            "angle": 120
        }
    ]

    for line in triangle:
        t.line(line["direction"], line["steps"], line["angle"])
    

    turtle.mainloop()

if __name__ == "__main__":
    main()

