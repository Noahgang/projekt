import requests
import yaml
import base64

status_code = input("Please enter the status code number (e.g., 200, 404): ")

url = f"https://http.cat/{status_code}"

with open("src/config.yaml", "r") as file:
    data = yaml.safe_load(file)
if data is None:
    data = {}

response = requests.get(url)

if response.status_code == 200:
    image_path = f"cat_{status_code}.jpg"
    
    with open(image_path, "wb") as file:
        file.write(response.content)
    print("Image saved successfully.")

    with open(image_path, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode('utf-8')

    data['image'] = encoded_image
    with open("src/config.yaml", "w") as file:
        yaml.safe_dump(data, file)
    print("YAML file updated successfully.")

    print_format = input("Choose the file format to print:\n1. YAML file only\n2. JPG file only\n3. Both files\n")

    if print_format == '1':
        print("YAML file contents printed to 'config.yaml'")
    elif print_format == '2':
        print("JPG file created")
        with open(image_path, "rb") as file:
            jpg_contents = file.read()
    elif print_format == '3':
        print("YAML file contents printed to 'config.yaml'")
        print("JPG file created")
        with open(image_path, "rb") as file:
            jpg_contents = file.read()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
else:
    print("Failed to retrieve the image.")