# move_jpg_files.py

import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)
    jpg_files = [f for f in files if f.lower().endswith('.jpg')]

    if not jpg_files:
        print("❌ No .jpg files found in the source folder.")
        return

    for file in jpg_files:
        src_path = os.path.join(source_folder, file)
        dst_path = os.path.join(destination_folder, file)
        shutil.move(src_path, dst_path)
        print(f"✅ Moved: {file}")

    print(f"\n🎉 Done! Moved {len(jpg_files)} .jpg files from '{source_folder}' to '{destination_folder}'.")

if __name__ == "__main__":
    source = input("Enter the path to the source folder: ")
    destination = input("Enter the path to the destination folder: ")
    move_jpg_files(source, destination)
