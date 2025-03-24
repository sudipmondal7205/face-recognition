import base64

# Decode the Base64 image data (assuming the user provides a valid base64 string)
base64_data = ""  # Replace with actual base64 string if available

# Convert to binary image data
image_data = base64.b64decode(base64_data)

# Save as a JPG file
file_path = "converted_image.jpg"
with open(file_path, "wb") as f:
    f.write(image_data)

# Return the file path for user to download
file_path
