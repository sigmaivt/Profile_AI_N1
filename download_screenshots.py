#!/usr/bin/env python3
import base64
import os

# Create simple colored placeholder screenshots using data URLs
def create_colored_image(filename, color, game_name):
    # Create a simple SVG image as base64 data URL
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="600" fill="{color}"/>
  <text x="400" y="280" font-family="Arial, sans-serif" font-size="48" fill="white" text-anchor="middle" font-weight="bold">{game_name}</text>
  <text x="400" y="550" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle">RETRO ZONE SCREENSHOT</text>
</svg>'''

    # Convert SVG to base64
    svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    data_url = f"data:image/svg+xml;base64,{svg_base64}"

    # Create a simple HTML file that can be opened to save as image
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <title>{game_name} Screenshot</title>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            background: {color};
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: calc(100vh - 40px);
        }}
        .game-name {{
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }}
        .footer {{
            font-size: 24px;
            opacity: 0.8;
        }}
    </style>
</head>
<body>
    <div class="game-name">{game_name}</div>
    <div class="footer">RETRO ZONE SCREENSHOT</div>
</body>
</html>'''

    # Save as HTML file that can be screenshot
    html_filename = filename.replace('.jpg', '.html')
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Created {html_filename} - open in browser and save as image")

# Game screenshots data with colors representing each game
games = [
    ('cs16-screenshot.jpg', '#2a3038', 'COUNTER-STRIKE 1.6'),
    ('warcraft3-screenshot.jpg', '#1e3a8a', 'WARCRAFT III'),
    ('quake3-screenshot.jpg', '#7f1d1d', 'QUAKE III ARENA'),
    ('starcraft-screenshot.jpg', '#1f2937', 'STARCRAFT'),
    ('diablo2-screenshot.jpg', '#451a03', 'DIABLO II'),
    ('halflife-screenshot.jpg', '#0f172a', 'HALF-LIFE'),
    ('dota-screenshot.jpg', '#166534', 'DOTA'),
    ('ut2004-screenshot.jpg', '#7c2d12', 'UNREAL TOURNAMENT 2004')
]

if __name__ == "__main__":
    print("Creating game screenshot HTML files...")

    for filename, color, game_name in games:
        html_filename = filename.replace('.jpg', '.html')
        if os.path.exists(html_filename):
            print(f"{html_filename} already exists, skipping...")
            continue

        try:
            create_colored_image(filename, color, game_name)
            print(f"✓ Created {html_filename}")
        except Exception as e:
            print(f"✗ Failed to create {html_filename}: {e}")

    print("HTML creation completed!")
    print("\nNext steps:")
    print("1. Open each .html file in browser")
    print("2. Take screenshot (F12 -> screenshot)")
    print("3. Save as .jpg with corresponding name")
    print("4. Delete .html files")
