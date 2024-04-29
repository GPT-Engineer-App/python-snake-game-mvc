class SnakeGameModel:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.food = None
        self.direction = 'RIGHT'
        self.game_over = False
        self.place_food()

    def place_food(self):
        import random
        while True:
            self.food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if self.food not in self.snake:
                break

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'UP':
            head_y -= 1
        elif self.direction == 'DOWN':
            head_y += 1
        elif self.direction == 'LEFT':
            head_x -= 1
        elif self.direction == 'RIGHT':
            head_x += 1

        new_head = (head_x, head_y)
        if new_head in self.snake or head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            self.game_over = True
        else:
            self.snake.insert(0, new_head)
            if new_head == self.food:
                self.place_food()
            else:
                self.snake.pop()

    def change_direction(self, direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if direction != opposite_directions.get(self.direction):
            self.direction = direction