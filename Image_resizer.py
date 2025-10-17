from PIL import Image

def resize_image(input_path, output_path, width, height):
    """Resize an image to the given width and height."""
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"✅ Image resized successfully and saved as {output_path}")
    except FileNotFoundError:
        print("❌ Error: Input file not found.")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")


if __name__ == "__main__":
    print("🖼️ Welcome to Image Resizer!")
    input_path = input("Enter image file path (e.g., sample_image.jpg): ")
    output_path = input("Enter output file name (e.g., resized_image.jpg): ")
    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))

    resize_image(input_path, output_path, width, height)
