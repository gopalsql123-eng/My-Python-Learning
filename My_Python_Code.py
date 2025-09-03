import shutil
import os

source_folder = r'C:\Python Code Test\Source'
destination_folder = r'C:\Python Code Test\Destination'

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.copy2(src_path, dst_path)
        print(f'Transferred: {filename}')