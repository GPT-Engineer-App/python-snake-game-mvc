import tkinter as tk

class SnakeGameView(tk.Tk):
    def __init__(self, model, cell_size=20):
        super().__init__()
        self.model = model
        self.cell_size = cell_size
        self.canvas = tk.Canvas(self, bg='black', width=model.width * cell_size, height=model.height * cell_size)
        self.canvas.pack()

    def draw(self):
        self.canvas.delete(tk.ALL)
        for x, y in self.model.snake:
            self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size, (x + 1) * self.cell_size, (y + 1) * self.cell_size, fill='green')
        fx, fy = self.model.food
        self.canvas.create_rectangle(fx * self.cell_size, fy * self.cell_size, (fx + 1) * self.cell_size, (fy + 1) * self.cell_size, fill='red')

    def update(self):
        if not self.model.game_over:
            self.model.move_snake()
            self.draw()
            self.after(100, self.update)
        else:
            self.canvas.create_text(self.model.width * self.cell_size / 2, self.model.height * self.cell_size / 2, text="Game Over", fill="white", font=('Arial', 24))