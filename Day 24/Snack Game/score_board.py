from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class ScorbBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(
            "D:/Python Devlopment/Udemy Course/Day 24/Snack Game/high_score.txt"
        ) as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGN,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(
                "D:/Python Devlopment/Udemy Course/Day 24/Snack Game/high_score.txt",
                mode="w",
            ) as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()

    def increse_score(self):
        self.score += 1
        self.update_score_board()
