import os
import shutil

# Define file type categories and their corresponding extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".odt"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Applications": [".exe", ".msi", ".dmg", ".apk"],
    "Others": []  # Will capture files with extensions not listed above
}

def organize_folder(folder_path, log_file_path=None):
    """Organize files in the given folder into categorized subfolders."""
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Create categorized subfolders if they don't exist
    for category in FILE_CATEGORIES:
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

    # Initialize log entries
    log_entries = []

    # Move files into their respective categorized folders
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file's category based on its extension
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                target_folder = os.path.join(folder_path, category)
                shutil.move(file_path, os.path.join(target_folder, filename))
                log_entries.append(f"Moved: {filename} -> {category}/")
                moved = True
                break

        # If no matching category was found, move to 'Others'
        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            shutil.move(file_path, os.path.join(others_folder, filename))
            log_entries.append(f"Moved: {filename} -> Others/")

    print("Files have been organized.")

    # Write log file if path is provided
    if log_file_path:
        with open(log_file_path, "w") as log_file:
            log_file.write("\n".join(log_entries))
        print(f"Log file saved to: {log_file_path}")

if __name__ == "__main__":
    # Example usage
    default_folder = os.path.expanduser("~/Downloads")
    folder_to_organize = input(f"Enter the path of the folder to organize (default: {default_folder}): ").strip()
    folder_to_organize = folder_to_organize or default_folder

    log_file = os.path.join(folder_to_organize, "organize_log.txt")
    organize_folder(folder_to_organize, log_file_path=log_file)
