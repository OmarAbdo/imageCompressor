from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Save the compressed image
            img.save(output_path, 'JPEG', quality=quality)
        print(f"Image compressed and saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_image_path = 'input_image.jpg'
output_image_path = 'compressed_image.jpg'

compress_image(input_image_path, output_image_path, quality=85)