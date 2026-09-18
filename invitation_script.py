"""Script to automate the process of sending birthday invitations to a list of people."""

sender_name = input("Enter Your Name: ")

# Read the names of the invited people from a text file.
with open("Location of invitation names file", "r") as f1:
    names = f1.readlines()

# Read the invitation template from a text file.
with open("Location of invitation template file", "r") as f2:
    content = f2.read()

# Generate personalized invitations for each invited person.
for name in names:
    name = name.strip()
    invitation = content.replace("[Invited Person’s Name]", name)
    invitation = invitation.replace("[Sender’s Name]", sender_name)
    invitation = invitation.replace("[Insert Date]", "xx-xx-xxxx")
    invitation = invitation.replace("[Insert Location]", "xxxxx")
    invitation = invitation.replace("[Insert Time]", "xx:xx AM/PM")
    invitation = invitation.replace("[RSVP Date]", "xx-xx-xxxx")

    # Write the personalized invitation to a new text file for each invited person.
    with open(
        f"Location of invitation letters file/letter_for_{name}.txt","w+",) as f3:
        f3.write(invitation)
