with open("Input/Names/invited_names.txt", "r") as f1:
    names = f1.readlines()

with open("Input/Letters/starting_letter.txt", "r") as f2:
    content = f2.read()

for name in names:
    name = name.strip()
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as f3:
        replace_name = content.replace("[name]", name)
        f3.write(replace_name)