from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class ScorbBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
