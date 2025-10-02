from pathlib import Path
from PIL import Image

def create_placeholder(output_path: Path):
    """Create a tiny 1x1 white pixel placeholder under 400 bytes."""
    img = Image.new("RGB", (1, 1), color=(255, 255, 255))
    img.save(output_path, optimize=True)
    print(f"Tiny placeholder saved as {output_path} ({output_path.stat().st_size} bytes)")

def compress_to_webp_lossless(input_path: Path, output_path: Path):
    """Compress real image to WebP losslessly without changing dimensions."""
    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")  # convert to RGB for WebP
        img.save(output_path, "WEBP", lossless=True, optimize=True)
        print(f"Lossless WebP saved as {output_path} ({output_path.stat().st_size} bytes)")

# ---- SET INPUT FILE ----
input_file = Path("my_product.png")        # your original PNG
placeholder_file = Path("placeholder.png")
webp_file = Path("my_product_compressed.webp")

# Create tiny placeholder (<400 bytes)
create_placeholder(placeholder_file)

# Compress the real PNG to WebP losslessly, keeping original dimensions
compress_to_webp_lossless
