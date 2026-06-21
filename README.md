# DonutSMP-ProofGen

A Python-based proof generator designed to generate payment proof images, specifically tailored for DonutSMP. The tool is highly configurable and can be adapted to work for other Minecraft servers that utilize similar chat formats and color schemes.

### ⚠️ Disclaimer
**For Educational Purposes Only.** This software is provided "as is", without warranty of any kind. Use this software at your own risk. The developer is not responsible for any misuse of this tool or violation of server terms of service.

---

## 🚀 Features
- **Customizable:** Easily change chat colors, dimensions, and text via `main.py`.
- **Tiled Background:** Automatically tiles textures to avoid distortion.
- **Easy Export:** Generates clean `.png` files in a dedicated output directory.
- **Dynamic:** Handles custom usernames and payment amounts via command-line input.

## 🛠️ Prerequisites
- Python 3.x
- [Pillow](https://python-pillow.org/) (Python Imaging Library)

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/kehlchen/DonutSMP-ProofGen.git
   cd DonutSMP-ProofGen
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt

## ⚙️ Usage
1. Place your minecraftia.ttf font and your background texture (image.png) in the project root folder(usually its already there).
2. Run the script:
   ```bash
   python main.py
3. Follow the prompts in the terminal to enter the Player Name and Payment Amount.
4. Your generated proof will be saved in the images/ directory.
## 🔧 Configuration
You can customize the layout in main.py:
 * **CHAT_WIDTH / CHAT_HEIGHT**: Adjust these to fit your server's chat UI.
 * **COLOR_TEXT, COLOR_PLAYER, COLOR_MONEY**: Modify these RGB tuples to match the server's color codes.
## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

