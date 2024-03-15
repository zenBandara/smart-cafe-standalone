import os

def count_foods(name):
    image_counts = {}
    detect_folder_path = 'detect/' + name + '/predict/crops'
    # Iterate through subdirectories in 'detect'
    for root, dirs, files in os.walk(detect_folder_path):
        for dir in dirs:
            # Join the subdirectory path with 'detect' folder path
            subfolder_path = os.path.join(root, dir)

            # List all files in the subdirectory
            subfolder_files = os.listdir(subfolder_path)

            # Count the number of image files (assuming they have common image extensions like .jpg, .png, .jpeg, etc.)
            image_count = sum(
                1 for file in subfolder_files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')))

            # Store the count in the dictionary with the subfolder name as the key
            image_counts[dir] = image_count

    return image_counts
