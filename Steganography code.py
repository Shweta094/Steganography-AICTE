import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from stegano.lsb import hide, reveal
import random

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#000000") 

        self.label = tk.Label(root, text="Steganography - Hide and Retrieve Text in Images", font=("Arial", 14, "bold"), bg="#000000", fg="cyan")
        self.label.pack(pady=10)

        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image, font=("Arial", 12, "bold"), bg="#FF00FF", fg="#FFFF00", relief=tk.RAISED)
        self.btn_load.pack(pady=5)

        self.canvas = tk.Canvas(root, width=500, height=350, bg="#111111", highlightthickness=5, highlightbackground=random.choice(["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]))
        self.canvas.pack(pady=10)

        self.text_entry = tk.Entry(root, width=50, font=("Arial", 12, "bold"), bg="#222222", fg="lime", insertbackground="white")
        self.text_entry.pack(pady=5)

        self.btn_encode = tk.Button(root, text="Encode Text", command=self.encode_text, font=("Arial", 12, "bold"), bg="#FF4500", fg="white", relief=tk.RAISED)
        self.btn_encode.pack(pady=5)

        self.btn_decode = tk.Button(root, text="Decode Text", command=self.decode_text, font=("Arial", 12, "bold"), bg="#008080", fg="white", relief=tk.RAISED)
        self.btn_decode.pack(pady=5)

        self.vfx_text = tk.Label(root, text="HACK MODE ACTIVATED", font=("Arial", 18, "bold"), fg=random.choice(["red", "green", "blue", "yellow"]), bg="#000000")
        self.vfx_text.pack(pady=5)

        self.image = None
        self.file_path = None

        self.animate_vfx()

    def animate_vfx(self):
        colors = ["red", "green", "blue", "yellow", "purple", "cyan"]
        self.vfx_text.config(fg=random.choice(colors))
        self.root.after(300, self.animate_vfx)

    def load_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
        if self.file_path:
            self.image = Image.open(self.file_path)
            self.image.thumbnail((500, 350))
            self.img_display = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(250, 175, image=self.img_display)

    def encode_text(self):
        if not self.image:
            messagebox.showerror("Error", "Please load an image first")
            return

        text = self.text_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter text to encode")
            return

        encoded_image = hide(self.file_path, text)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            encoded_image.save(save_path)
            messagebox.showinfo("Success", "Text encoded and image saved!")

    def decode_text(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please load an image first")
            return

        try:
            hidden_text = reveal(self.file_path)
            if hidden_text:
                messagebox.showinfo("Decoded Text", hidden_text)
            else:
                messagebox.showwarning("No Hidden Text", "No hidden text found in the image.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decode text: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
