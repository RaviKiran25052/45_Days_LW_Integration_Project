import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageToggleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Toggle App")

        self.image_paths = ["off.png", "on.png"]
        self.current_image_idx = 0
        self.images = []

        for path in self.image_paths:
            image = Image.open(path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            self.images.append(ImageTk.PhotoImage(image))

        self.image_button = ttk.Button(root, image=self.images[0], command=self.toggle_image,style="Custom.TButton")
        self.image_button.pack()

        self.quit_button = ttk.Button(root, text="Quit", command=self.root.quit,style="Custom.TButton")
        self.quit_button.pack()

    def toggle_image(self):
        self.current_image_idx = (self.current_image_idx + 1) % len(self.images)
        self.image_button.configure(image=self.images[self.current_image_idx])
        if self.current_image_idx:
            self.call_function()

    def call_function(self):
        print("Function called after image toggle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToggleApp(root)
    root.mainloop()