import os
import shutil
import dicom2jpg


def organize_images_by_digit(source_dir, target_dir, digit_position):
    """
    Organizes images from source_dir into folders in target_dir based on the digit at digit_position in their filenames.
    
    Args:
    - source_dir (str): The directory containing the images to be organized.
    - target_dir (str): The directory where the organized folders will be created.
    - digit_position (int): The position of the digit in the filename to base the organization on (0-based index).
    """
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # List all files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file is an image (optional: based on extension)
        if filename.lower().endswith(('.dcm')):
            # Extract the digit at the specified position
            if len(filename) > digit_position and filename[digit_position].isdigit():
                digits = filename[digit_position:digit_position+3]
                
                print(digits)
                # Create the target directory for this digit if it does not exist
                digit_folder = os.path.join(target_dir, digits)
                os.makedirs(digit_folder, exist_ok=True)
                
                # Construct the full file paths
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(digit_folder, filename)
                
                # copy the file
                shutil.copy(source_file, target_file)
                print(f"copied {filename} to {digit_folder}")
                
                # convert the dicom into bitmap and store it in the new location
                
                # dicom2jpg.dicom2jpg(source_file,target_root=target_dir)
                # print(f"converted {filename} to {digit_folder}")


# Example usage
source_directory = './data/DICOM/'
target_directory = './data/DICOM/'
digit_position = 37  # 0-based index (e.g., the 4th character in the filename)

organize_images_by_digit(source_directory, target_directory, digit_position)
