class SnakeGameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.bind("<KeyPress>", self.on_key_press)
        self.view.focus_set()

    def on_key_press(self, event):
        key = event.keysym
        direction_map = {'Up': 'UP', 'Down': 'DOWN', 'Left': 'LEFT', 'Right': 'RIGHT'}
        if key in direction_map:
            self.model.change_direction(direction_map[key])

    def run(self):
        self.view.update()
        self.view.mainloop()