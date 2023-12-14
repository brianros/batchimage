import csv
from tkinter import Tk, Label, Button, Entry, filedialog, Canvas
from PIL import Image, ImageDraw, ImageFont, ImageTk

class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Imager - Image processor by Brian Rosenfeld")
        root.geometry("910x630") 

        self.label_original_image = Label(root, text="Original Image:")
        self.label_original_image.grid(row=0, column=0)

        self.entry_original_image = Entry(root, width=40)
        self.entry_original_image.grid(row=0, column=1)

        self.browse_original_image_button = Button(root, text="Browse", command=self.browse_original_image)
        self.browse_original_image_button.grid(row=0, column=2)

        self.label_names_list = Label(root, text="Names List:")
        self.label_names_list.grid(row=1, column=0)

        self.entry_names_list = Entry(root, width=40)
        self.entry_names_list.grid(row=1, column=1)

        self.browse_names_list_button = Button(root, text="Browse", command=self.browse_names_list)
        self.browse_names_list_button.grid(row=1, column=2)

        self.label_output_folder = Label(root, text="Output Folder:")
        self.label_output_folder.grid(row=2, column=0)

        self.entry_output_folder = Entry(root, width=40)
        self.entry_output_folder.grid(row=2, column=1)

        self.browse_output_folder_button = Button(root, text="Browse", command=self.browse_output_folder)
        self.browse_output_folder_button.grid(row=2, column=2)

        self.label_font = Label(root, text="Font:")
        self.label_font.grid(row=3, column=0)

        self.entry_font = Entry(root, width=40)
        self.entry_font.grid(row=3, column=1)

        self.browse_font_button = Button(root, text="Browse", command=self.browse_font)
        self.browse_font_button.grid(row=3, column=2)

        self.label_font_size = Label(root, text="Font Size:")
        self.label_font_size.grid(row=4, column=0)

        self.entry_font_size = Entry(root, width=40)
        self.entry_font_size.grid(row=4, column=1)

        self.label_position_x = Label(root, text="Position X:")
        self.label_position_x.grid(row=5, column=0)

        self.entry_position_x = Entry(root, width=20)
        self.entry_position_x.grid(row=5, column=1)

        self.label_position_y = Label(root, text="Position Y:")
        self.label_position_y.grid(row=5, column=2)

        self.entry_position_y = Entry(root, width=20)
        self.entry_position_y.grid(row=5, column=3)

        self.canvas_preview = Canvas(root, width=600, height=400, bg="white")
        self.canvas_preview.grid(row=7, column=1, pady=(10, 0))

        self.preview_button = Button(root, text="Preview", command=self.update_preview)
        self.preview_button.grid(row=8, column=1)

        self.process_button = Button(root, text="Process Images", command=self.process_names, width=20, height=2)
        self.process_button.grid(row=7, column=3)


        self.update_preview()

    def browse_original_image(self):
        original_image_path = filedialog.askopenfilename(title="Select Original Image")
        self.entry_original_image.delete(0, 'end')
        self.entry_original_image.insert(0, original_image_path)
        self.update_preview()

    def browse_names_list(self):
        names_list_path = filedialog.askopenfilename(title="Select Names List")
        self.entry_names_list.delete(0, 'end')
        self.entry_names_list.insert(0, names_list_path)
        self.update_preview()

    def browse_output_folder(self):
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        self.entry_output_folder.delete(0, 'end')
        self.entry_output_folder.insert(0, output_folder)
        self.update_preview()

    def browse_font(self):
        font_path = filedialog.askopenfilename(title="Select Font")
        self.entry_font.delete(0, 'end')
        self.entry_font.insert(0, font_path)
        self.update_preview()

    def update_preview(self):
        original_image_path = self.entry_original_image.get()
        font_path = self.entry_font.get()

        # Validate font size
        font_size_str = self.entry_font_size.get()
        try:
            font_size = int(font_size_str) if font_size_str else 40  # Default to 40 if empty
        except ValueError:
            print("Invalid font size. Using default value.")
            font_size = 40

        # Validate position
        position_x_str = self.entry_position_x.get()
        position_y_str = self.entry_position_y.get()
        try:
            position_x = int(position_x_str) if position_x_str else 10  # Default to 10 if empty
            position_y = int(position_y_str) if position_y_str else 10  # Default to 10 if empty
        except ValueError:
            print("Invalid position. Using default values.")
            position_x, position_y = 10, 10

        try:
            with Image.open(original_image_path).convert("RGB") as original_image:
                preview_image = original_image.copy()

                if font_path:
                    font = ImageFont.truetype(font_path, font_size)
                    draw = ImageDraw.Draw(preview_image)
                    draw.text((position_x, position_y), "Preview Text", font=font, fill=(0, 0, 0))

                preview_image.thumbnail((600, 400))
                photo = ImageTk.PhotoImage(preview_image)

                self.canvas_preview.config(width=preview_image.width, height=preview_image.height)
                self.canvas_preview.create_image(0, 0, anchor="nw", image=photo)
                self.canvas_preview.image = photo
        except Exception as e:
            print(f"Error updating preview: {e}")

    def add_text_to_image(self, input_image_path, output_image_path, text, font_size=40, font_path=None, fill_color=(0, 0, 0), position=(10, 10)):
        with Image.open(input_image_path).convert("RGB") as original_image:
            new_image = original_image.copy()

            if font_path is None:
                font = ImageFont.load_default()
            else:
                font = ImageFont.truetype(font_path, font_size)

            draw = ImageDraw.Draw(new_image)
            draw.text(position, text, font=font, fill=fill_color)

            new_image.save(output_image_path, "JPEG")

    def process_names(self):
        original_image_path = self.entry_original_image.get()
        names_list_path = self.entry_names_list.get()
        output_folder = self.entry_output_folder.get()
        font_path = self.entry_font.get()
        font_size = int(self.entry_font_size.get())
        position_x = int(self.entry_position_x.get())
        position_y = int(self.entry_position_y.get())
        position = (position_x, position_y)

        with open(names_list_path, "r") as file:
            reader = csv.reader(file)
           # header = next(reader)

            for row in reader:
                if row:
                    name = row[0]
                    output_image_path = f"{output_folder}/{name}.jpg"
                    self.add_text_to_image(original_image_path, output_image_path, name, font_size, font_path, position=position)

        print("Images created successfully.")

if __name__ == "__main__":
    root = Tk()
    app = ImageProcessor(root)
    root.mainloop()
