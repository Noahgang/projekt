import random
import requests
import yaml
import base64

numbers = [
    100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 214, 226, 300, 
    301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 
    409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425, 
    426, 428, 429, 431, 444, 450, 451, 497, 498, 499, 500, 501, 502, 503, 504, 506, 
    507, 508, 509, 510, 511, 521, 522, 523, 525, 530, 599
]

def get_random_number():
    return random.choice(numbers)

def main():
    while True:
        user_input = input("Enter status code number, type 'random' for a random cat image, or 'stop' to exit: ")

        if user_input.lower() == "stop":
            break

        if user_input.lower() == "random":
            status_code = get_random_number()
            print(f"Random status code selected: {status_code}")
        else:
            try:
                status_code = int(user_input)
            except ValueError:
                print("Invalid input. Enter valid status code number, 'random', or 'stop'.")
                continue

        url = f"https://http.cat/{status_code}"

        try:
            with open("src/config.yaml", "r") as file:
                data = yaml.safe_load(file)
            if data is None:
                data = {}
        except FileNotFoundError:
            data = {}

        response = requests.get(url)

        if response.status_code == 200:
            print_format = input("Choose the file format to create:\n1. YAML file only\n2. JPG file only\n3. Both files\n")

            if print_format == '1' or print_format == '3':
                encoded_image = base64.b64encode(response.content).decode('utf-8')
                data['image'] = encoded_image
                with open("src/config.yaml", "w") as file:
                    yaml.safe_dump(data, file)
                print("YAML file updated successfully.")
            
            if print_format == '2' or print_format == '3':
                image_path = f"cat_{status_code}.jpg"
                with open(image_path, "wb") as file:
                    file.write(response.content)
                print(f"Image saved successfully as {image_path}.")

            if print_format not in ['1', '2', '3']:
                print("Invalid choice. Please enter 1, 2, or 3.")
        else:
            print("Failed to retrieve the image.")

if __name__ == "__main__":
    main()
