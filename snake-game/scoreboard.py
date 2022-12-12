from turtle import Turtle
ALIGNMENT = "center"
FONT = "Calibri"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.fetch_high_score_from_data_file()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.update_scoreboard()

    def fetch_high_score_from_data_file(self):
        with open("data.txt") as file:
            data = int(file.read())
            return data

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", move=False, align=ALIGNMENT, font=(FONT, 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=(FONT, 24, "normal"))