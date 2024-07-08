import random

def generate_phone_number():
    country_code = "+1"
    number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return f"{country_code}{number}"

def update_config_file(phone_numbers, config_file_path='config.py'):
    with open(config_file_path, 'r') as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        if line.strip().startswith("sourceNumbers ="):
            lines[i] = f"sourceNumbers = {phone_numbers}\n"
            break

    with open(config_file_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    num_of_numbers = int(input("How many phone numbers do you want to generate? "))
    generated_numbers = [generate_phone_number() for _ in range(num_of_numbers)]
    print("Generated phone numbers:", generated_numbers)

    update_config_file(generated_numbers)
    print(f"Updated {len(generated_numbers)} phone numbers in config.py")
