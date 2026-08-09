"""
Project 116: Console Snake Game
Category: Algorithms & DS
Description: Real-time interactive terminal Snake game with keyboard controls (WASD/Arrows), food spawning, collision detection, and score tracking.
"""
import asyncio
import random
import sys

try:
    import js
except ImportError:
    js = None

class InteractiveSnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.snake = [(self.height // 2, self.width // 2)]
        self.direction = (0, 1) # Right
        self.food = self._spawn_food()
        self.score = 0
        self.high_score = getattr(self, 'high_score', 0)
        self.game_over = False
        self.paused = False

    def _spawn_food(self):
        while True:
            f = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            if f not in self.snake:
                return f

    def handle_input(self, key):
        if not key:
            return True
            
        key_lower = str(key).lower()
        
        if key_lower in ['w', 'arrowup'] and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key_lower in ['s', 'arrowdown'] and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif key_lower in ['a', 'arrowleft'] and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key_lower in ['d', 'arrowright'] and self.direction != (0, -1):
            self.direction = (0, 1)
        elif key_lower == 'p':
            self.paused = not self.paused
        elif key_lower == 'r' and self.game_over:
            self.reset()
        elif key_lower == 'q':
            return False
            
        return True

    def tick(self):
        if self.game_over or self.paused:
            return

        head_r, head_c = self.snake[0]
        dr, dc = self.direction
        new_head = (head_r + dr, head_c + dc)

        # Wall collision
        if new_head[0] < 0 or new_head[0] >= self.height or new_head[1] < 0 or new_head[1] >= self.width:
            self.game_over = True
            return

        # Self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            self.food = self._spawn_food()
        else:
            self.snake.pop()

    def render(self):
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
        fr, fc = self.food
        grid[fr][fc] = "●"
        for idx, (r, c) in enumerate(self.snake):
            grid[r][c] = "█" if idx == 0 else "▓"

        lines = []
        lines.append("🐍 CONSOLE SNAKE GAME")
        lines.append("┌" + "─" * self.width + "┐")
        for row in grid:
            lines.append("│" + "".join(row) + "│")
        lines.append("└" + "─" * self.width + "┘")

        if self.game_over:
            lines.append(f"💥 GAME OVER! Score: {self.score} | Best: {self.high_score}")
            lines.append("Press [R] to Restart | Press [Q] to Quit")
        elif self.paused:
            lines.append(f"⏸️ PAUSED | Score: {self.score}")
            lines.append("Press [P] to Resume | Press [Q] to Quit")
        else:
            lines.append(f"Score: {self.score} | Best: {self.high_score}")
            lines.append("Controls: [WASD / Arrows] Move | [P] Pause | [Q] Quit")
            
        return "\n".join(lines)

async def run_game():
    game = InteractiveSnakeGame()
    
    # Send frame reset marker
    print("\x1bc" + game.render())
    
    while True:
        # Check for keypress from JS environment
        if js and hasattr(js, 'lastKeyPressed') and js.lastKeyPressed:
            key = str(js.lastKeyPressed)
            js.lastKeyPressed = None
            if not game.handle_input(key):
                print("\nGame exited cleanly.")
                break

        game.tick()
        # Output frame with clear-screen ANSI escape char
        print("\x1bc" + game.render())
        await asyncio.sleep(0.12)

def run_project_116():
    try:
        asyncio.run(run_game())
    except (KeyboardInterrupt, SystemExit, EOFError):
        print("\nGame session ended.")

if __name__ == "__main__":
    run_project_116()
