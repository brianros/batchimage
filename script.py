import csv
from PIL import Image, ImageDraw, ImageFont

# Usage variables
csv_file_path = "c:/diplomas/random_names.csv"  # Replace with the path to your CSV file
font_path = "c:/diplomas/dobkin.ttf"  # Replace with the path to your font file
input_image_path = "c:/diplomas/diploma.jpeg"  # Replace with the path to your input image
output_folder = "c:/diplomas/datos/"
position = (600, 430)

def add_text_to_image(input_image_path, output_image_path, text, font_size=60, font_path=None, fill_color=(0, 0, 0)):
    # Open the original image directly as RGB
    with Image.open(input_image_path).convert("RGB") as original_image:
        # Create a copy of the original image
        new_image = original_image.copy()

        # Get a font
        if font_path is None:
            font = ImageFont.load_default()  # You can replace this with a specific font file if needed
        else:
            font = ImageFont.truetype(font_path, font_size)

        # Get a drawing context for the new image
        draw = ImageDraw.Draw(new_image)

        # Draw text on the new image
        draw.text(position, text, font=font, fill=fill_color)

        # Save the new image to a file as JPEG
        new_image.save(output_image_path, "JPEG")

        # Display the result
        new_image.show()

def process_names():
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        #header = next(reader)  # Skip header if present

        for row in reader:
            if row:  # Check if the row is not empty
                name = row[0]  # Assuming the name is in the first column
                output_image_path = f"{output_folder}{name}.jpg"
                add_text_to_image(input_image_path, output_image_path, name, font_path=font_path)

# Example usage
process_names()

print("Images created successfully.")
