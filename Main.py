import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, master):
        self.master = master
        master.title("Watermark App")

        # Create GUI elements
        self.select_button = Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.watermark_entry = Entry(master)
        self.watermark_entry.pack()

        self.add_button = Button(master, text="Add Watermark", command=self.add_watermark)
        self.add_button.pack()

    def select_image(self):
        """Opens a file dialog to select an image file."""
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    def add_watermark(self):
        """Adds a watermark to the selected image file."""
        if not hasattr(self, "filename"):
            print("Please select an image file.")
            return

        # Open the image file
        with Image.open(self.filename) as im:
            # Create a new image for the watermark
            watermark = Image.new("RGBA", im.size, (255, 255, 255, 0))

            # Draw the watermark text
            draw = ImageDraw.Draw(watermark)
            font = ImageFont.truetype("arial.ttf", 36)
            draw.text((10, 10), self.watermark_entry.get(), font=font, fill=(255, 255, 255, 128))

            # Combine the original image and the watermark
            result = Image.alpha_composite(im.convert("RGBA"), watermark)

            # Save the result
            result.save(os.path.splitext(self.filename)[0] + "_watermarked.png")

            print("Watermark added.")

# Create the GUI window
root = Tk()
app = WatermarkApp(root)
root.mainloop()
