import tkinter as tk
import random

# Constants
WIDTH = 800
HEIGHT = 600
COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
SPECIAL_BUBBLES = ['bomb', 'star', 'freeze']

class BubbleShooter:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.bubbles = []
        self.shooter = self.canvas.create_rectangle(0, HEIGHT-20, 50, HEIGHT, fill='black')
        self.root.bind("<Motion>", self.motion)
        self.root.bind("<Button-1>", self.shoot)
        self.score = 0
        self.level = 1
        self.create_bubbles()
        self.root.after(1000, self.move_bubbles)
        self.root.mainloop()

    def create_bubbles(self):
        for _ in range(10 * self.level):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT // 2)
            color = random.choice(COLORS)
            bubble_type = random.choice([None] + SPECIAL_BUBBLES)  # None for regular bubbles
            bubble = self.canvas.create_oval(x, y, x+40, y+40, fill=color, tags=bubble_type)
            self.bubbles.append(bubble)

    def motion(self, event):
        x = event.x
        self.canvas.coords(self.shooter, x-25, HEIGHT-20, x+25, HEIGHT)

    def shoot(self, event):
        x1, _, x2, _ = self.canvas.coords(self.shooter)
        x = (x1 + x2) / 2
        y = HEIGHT - 20
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill='white', tags='bullet')
        self.check_collision(x, y)

    def check_collision(self, x, y):
        collisions = self.canvas.find_overlapping(x-5, y-5, x+5, y+5)
        for bubble in collisions:
            if 'bubble' in self.canvas.gettags(bubble):
                bubble_type = self.canvas.gettags(bubble)[0]
                if bubble_type == 'bomb':
                    self.destroy_nearby_bubbles(x, y)
                elif bubble_type == 'star':
                    self.destroy_bubbles_of_color(random.choice(COLORS))
                elif bubble_type == 'freeze':
                    self.freeze_bubbles()
                self.canvas.delete(bubble)
                self.bubbles.remove(bubble)
                self.score += 10
                self.update_score()
                break

    def destroy_nearby_bubbles(self, x, y):
        for bubble in self.bubbles[:]:
            bx1, by1, bx2, by2 = self.canvas.coords(bubble)
            if abs(x - (bx1 + bx2) / 2) <= 60 and abs(y - (by1 + by2) / 2) <= 60:
                self.canvas.delete(bubble)
                self.bubbles.remove(bubble)

    def destroy_bubbles_of_color(self, color):
        for bubble in self.bubbles[:]:
            if color in self.canvas.gettags(bubble):
                self.canvas.delete(bubble)
                self.bubbles.remove(bubble)

    def freeze_bubbles(self):
        for bubble in self.bubbles:
            self.canvas.itemconfig(bubble, state=tk.HIDDEN)

    def move_bubbles(self):
        for bubble in self.bubbles:
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            self.canvas.move(bubble, dx, dy)
        self.root.after(1000 // self.level, self.move_bubbles)

    def update_score(self):
        self.canvas.delete('score')
        self.canvas.create_text(WIDTH-50, 20, text=f"Score: {self.score}", anchor=tk.E, tags='score')

if __name__ == "__main__":
    game = BubbleShooter()
