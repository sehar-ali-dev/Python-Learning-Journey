import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Photo Album")
root.geometry("800x600")
# Agar images aur main.py ek hi folder mein hon, toh sirf naam likhein:
image_paths = [
    r"D:\sehar\project 4\image1.jpg",
    r"D:\sehar\project 4\image2.jpeg",
    r"D:\sehar\project 4\image3.jpg",
    r"D:\sehar\project 4\image4.jpeg",
    r"D:\sehar\project 4\image5.jpg"
]
image_size = (400, 300)
final_images = []

for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size, Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

image_label = tk.Label(root)
image_label.pack(pady=20)

current_index = 0

def start_slideshow():
    global current_index
    photo = final_images[current_index]
    image_label.config(image=photo)
    image_label.image = photo
    current_index = (current_index + 1) % len(final_images)
    root.after(2000, start_slideshow)

play_button = tk.Button(
    root,
    text="Play Slideshow",
    command=start_slideshow,
    font=("Arial", 16)
)
play_button.pack(pady=10)

root.mainloop()