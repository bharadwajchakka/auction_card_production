import os
import cv2

# Path to the folder containing the foreground images
folder_path = 'C:/Users/BHARADWAJ/Downloads/cricverse2024/photo'
template_folder_path='C:/Users/BHARADWAJ/Downloads/cricverse2024/player_card'
output_folder_path='C:/Users/BHARADWAJ/Downloads/cricverse2024/output'
# Define the coordinates of the rectangular area
x1, y1 = 55,604 # Top-left corner of the rectangle
x2, y2 = 781,1638 # Bottom-right corner of the rectangle

# Iterate over the files in the folder
for file_name in os.listdir(folder_path):
    # Load the foreground image
    foreground_path = os.path.join(folder_path, file_name)
    foreground = cv2.imread(foreground_path, cv2.IMREAD_UNCHANGED)

    # Create a unique name for the output file
    output_file_name = os.path.splitext(file_name)[0] + '.jpg'
    output_path = os.path.join(output_folder_path, output_file_name)

    try:
        # Load the background image
        bg_filename = os.path.splitext(file_name)[0] + '.png'
        bg_path = os.path.join(template_folder_path, bg_filename)
        background = cv2.imread(bg_path)

        # Check if the background image was loaded successfully
        if background is None:
            raise Exception(f"Could not open background image at path: {bg_path}")

        # Resize the foreground image to fit the size of the rectangular area
        foreground_resized = cv2.resize(foreground, (x2 - x1, y2 - y1))

        # Check if the foreground image has an alpha channel
        if foreground_resized.shape[2] == 4:
            # Extract the alpha channel from the foreground image
            alpha = foreground_resized[:, :, 3] / 255.0

            # Blend the images using the alpha channel
            for c in range(0, 3):
                background[y1:y2, x1:x2, c] = \
                    foreground_resized[:, :, c] * alpha + \
                    background[y1:y2, x1:x2, c] * (1.0 - alpha)
        else:
            # Overlay the resized foreground image onto the background image directly
            background[y1:y2, x1:x2] = foreground_resized[:, :]

        # Save the resulting image
        cv2.imwrite(output_path, background)
        

    except Exception as e:
        print(f"Error processing {file_name}: {e}")

print("all cards are processed")
