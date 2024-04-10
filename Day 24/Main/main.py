PLACEHOLDER = "[name]"

with open("Main/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


with open("Main/Input/Letters/starting_letter.txt") as sample_letter_file:
    letter_formet = sample_letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_formet.replace(PLACEHOLDER, name)
        with open(
            f"Main/Output/ReadyToSend/letter_for_{name}.txt", mode="w"
        ) as output_file:
            output_file.write(new_letter)
