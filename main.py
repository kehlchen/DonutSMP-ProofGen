# Englisch Version

import os
from PIL import Image, ImageDraw, ImageFont

# --- KONFIGURATION ---
FONT_PATH = "src/minecraftia.ttf"
TEXTURE_PATH = "src/image.png"
OUTPUT_DIR = "images"
CHAT_WIDTH = 970
CHAT_HEIGHT = 60


COLOR_TEXT = (255, 255, 255)   
COLOR_PLAYER = (85, 255, 255)  
COLOR_MONEY = (85, 255, 85)    

def clean_filename(name):
    """Removes characters that are not allowed in filenames."""
    invalid_chars = '<>:"/\\|?*.'
    for char in invalid_chars:
        name = name.replace(char, "")
    return name

def main():
    print("Starting Program...")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    

    if not os.path.exists(FONT_PATH) or not os.path.exists(TEXTURE_PATH):
        print("ERROR: Font or image not found!")
        return


    betrag_str = input("Enter Amount: ")
    player_str = input("Enter Player: ")


    clean_player = clean_filename(player_str)
    clean_betrag = clean_filename(betrag_str.replace("$", ""))
    filename = f"{clean_player}_{clean_betrag}.png"
    full_path = os.path.join(OUTPUT_DIR, filename)


    print(f"Create image: {full_path}...")
    try:
        texture = Image.open(TEXTURE_PATH).convert("RGB")
        image = Image.new("RGB", (CHAT_WIDTH, CHAT_HEIGHT))
        

        for x in range(0, CHAT_WIDTH, texture.width):
            for y in range(0, CHAT_HEIGHT, texture.height):
                image.paste(texture, (x, y))
        
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(FONT_PATH, 36)
        

        text_segments = [
            ("You paid ", COLOR_TEXT),
            (f"{player_str} ", COLOR_PLAYER), 
            (f"{betrag_str}", COLOR_MONEY),
            (".", COLOR_TEXT)
        ]

        total_text_width = sum(draw.textlength(text, font=font) for text, color in text_segments)
        x_offset = (CHAT_WIDTH - total_text_width) / 2
        
 
        for text, color in text_segments:
            draw.text((x_offset, 10), text, font=font, fill=color)
            x_offset += draw.textlength(text, font=font)
        
        image.save(full_path)
        print(f"Success! '{full_path}' has been saved.")
        
    except Exception as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    main()