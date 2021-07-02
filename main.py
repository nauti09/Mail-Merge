# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you:


with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    lines_of_letter = letter.readlines()

with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()

edited_names = []

for name in names:
    name = name.strip("\n")
    edited_names.append(name)

for name in edited_names:
    personalized_name = lines_of_letter[0].replace("[name]", name)
    lines_of_letter[0] = personalized_name
    personalized_letter = ""
    for lines in lines_of_letter:
        personalized_letter += lines
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(personalized_letter)
    lines_of_letter[0] = lines_of_letter[0].replace(name, "[name]")
