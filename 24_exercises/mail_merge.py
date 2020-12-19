

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()


with open("./Input/Letters/starting_letter.docx") as f:
    base_text = f.read()

for name in names:
    new_name = name.strip()
    new_letter = base_text.replace('[name]', new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.docx", mode="w") as f:
        f.write(new_letter)
