import secrets

animals_file = open("animals.txt", "r")
animals_list = animals_file.readlines()

fruits_file = open("fruits.txt", "r")
fruits_list = fruits_file.readlines()

next_key = []
next_key.append(secrets.choice(animals_list).strip())
next_key.append(secrets.choice(fruits_list).strip())
alternative_key = secrets.choice(animals_list) + secrets.choice(fruits_list)
print(''.join(next_key) + '{:03}'.format(secrets.randbelow(999)))