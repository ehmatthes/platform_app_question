from pathlib import Path

path = Path(".platform.app.yaml")

try:
    contents = path.read_text()
except UnicodeDecodeError:
    print("Using utf-16 encoding.")
    contents = path.read_text(encoding='utf-16')

print(len(contents))