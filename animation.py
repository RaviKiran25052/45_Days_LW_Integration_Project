import tkinter as tk
import time
import threading

class LoadingAnimation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=300, bg='black')
        self.canvas.pack()
        self.loading_text = self.canvas.create_text(200, 150, text="Loading...", fill="white", font=("Helvetica", 20))
        self.loading_bar = self.canvas.create_rectangle(100, 200, 100, 220, fill="gray", outline="")
        self.direction = 1  # 1 for right, -1 for left
        self.is_running = True
        self.thread = threading.Thread(target=self.animate)

    def start_animation(self):
        self.thread.start()

    def stop_animation(self):
        self.is_running = False
        self.thread.join()
        self.root.destroy()

    def animate(self):
        while self.is_running:
            x0, y0, x1, y1 = self.canvas.coords(self.loading_bar)
            new_x0 = x0 + 10 * self.direction
            new_x1 = x1 + 10 * self.direction

            if new_x0 <= 100 or new_x1 >= 300:
                self.direction *= -1

            self.canvas.coords(self.loading_bar, new_x0, y0, new_x1, y1)
            self.canvas.itemconfig(self.loading_text, text="Loading...")
            self.root.update()
            time.sleep(0.1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Loading Animation")
    app = LoadingAnimation(root)

    # Simulate your process here
    # For demonstration purposes, we will use a sleep function to simulate the process.
    def simulate_process():
        time.sleep(5)  # Simulating a process that takes 5 seconds
        app.stop_animation()

    # Start the loading animation
    app.start_animation()

    # Start the process (in this case, simulation)
    thread = threading.Thread(target=simulate_process)
    thread.start()

    root.mainloop()
