with open("mail_merge/input/names/invited_names.txt") as names:
    users = names.readlines()


with open("mail_merge/input/letters/starting_letter.txt") as letter:
    letter_text = letter.read()
    for user in users:
        new_letter = letter_text.replace("[name]", user.strip())
        with open(
            f"mail_merge/output/ReadyToSend/letter_for_{user}.txt", mode="w"
        ) as letter:
            letter.write(new_letter)
