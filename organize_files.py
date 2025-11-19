import shutil
import os

# Define file movements
moves = [
    ('train.py', 'src/train.py'),
    ('infer.py', 'src/infer.py'),
    ('embedding.py', 'src/embedding.py'),
    ('utils.py', 'src/utils.py'),
    ('models.py', 'models/models.py'),
    ('prepare_data.py', 'scripts/prepare_data.py'),
    ('IMg.ipynb', 'notebooks/IMg.ipynb'),
    ('loaddata.ipynb', 'notebooks/loaddata.ipynb'),
]

# Move files
for src, dest in moves:
    if os.path.exists(src):
        print(f"Moving {src} to {dest}")
        shutil.move(src, dest)
    else:
        print(f"Skipping {src} (not found)")

print("\nFile organization complete!")
