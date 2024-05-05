import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk


class ImageDenoiserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Noise Removal")
        self.root.geometry("480x520")  # Increased height to accommodate image display

        # Add colorful background
        self.background = tk.Label(root, bg="lightblue", width=480, height=480)
        self.background.place(x=0, y=0)

        # Add title label
        self.title_label = tk.Label(root, text="Image Noise Removal", font=("Helvetica", 18), bg="lightblue")
        self.title_label.pack(pady=20)

        # Add remove noise button
        self.btn_remove_noise = tk.Button(root, text="Remove Noise", font=("Helvetica", 12), command=self.remove_noise)
        self.btn_remove_noise.pack(pady=10)

        # Initialize image and photo label
        self.img = None
        self.photo_label = tk.Label(root, bg="white")
        self.photo_label.pack(pady=10)

        # Add save and try again buttons (initially hidden)
        self.btn_save = tk.Button(root, text="Save Image", font=("Helvetica", 12), command=self.save_image)
        self.btn_save.pack(pady=5)
        self.btn_try_again = tk.Button(root, text="Try Again", font=("Helvetica", 12), command=self.try_again)
        self.btn_try_again.pack(pady=5)
        self.hide_buttons()

        # Initialize denoised image PIL object
        self.denoised_img_pil = None

    def hide_buttons(self):
        self.btn_save.pack_forget()
        self.btn_try_again.pack_forget()

    def show_buttons(self):
        self.btn_save.pack(pady=5)
        self.btn_try_again.pack(pady=5)

    def remove_noise(self):
        # Open file dialog to choose image
        filepath = filedialog.askopenfilename(title="Select Image File",
                                              filetypes=(
                                              ("Image files", "*.jpg;*.jpeg;*.png;*.bmp"), ("All files", "*.*")))
        if not filepath:
            return

        try:
            # Read the image
            img = cv2.imread(filepath)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB for PIL

            # Convert to grayscale
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

            # Apply noise removal technique (e.g., Gaussian blur)
            denoised_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

            # Convert denoised image to PIL format
            self.denoised_img_pil = Image.fromarray(denoised_img)
            self.denoised_img_pil.thumbnail((400, 400))  # Resize the image while maintaining aspect ratio

            # Convert PIL image to Tkinter format
            self.denoised_img_tk = ImageTk.PhotoImage(self.denoised_img_pil)

            # Display the denoised image
            self.photo_label.config(image=self.denoised_img_tk)

            # Show save and try again buttons
            self.show_buttons()

        except Exception as e:
            messagebox.showerror("Error", "An error occurred: {}".format(str(e)))
            self.hide_buttons()

    def save_image(self):
        # Save the denoised image
        try:
            filepath = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                    filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")))
            if filepath:
                self.denoised_img_pil.save(filepath)
                messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while saving the image: {}".format(str(e)))

    def try_again(self):
        self.hide_buttons()
        self.photo_label.config(image="")
        self.photo_label.image = None


# Create GUI window
root = tk.Tk()
app = ImageDenoiserApp(root)

# Run the GUI loop
root.mainloop()
