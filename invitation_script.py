"""Script to automate the process of sending birthday invitations to a list of people."""

sender_name = input("Enter Your Name: ")
event_date = input("Event Date (in format xx-xx-xxxx): ")
event_time = input("Event Time (in format xx:xx AM/PM): ")
venue = input("Event Venue: ")
rsvp_date = input("RSVP Date (in format xx-xx-xxxx): ")

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
    invitation = invitation.replace("[Insert Date]", date)
    invitation = invitation.replace("[Insert Location]", venue)
    invitation = invitation.replace("[Insert Time]", time)
    invitation = invitation.replace("[RSVP Date]", rsvp_date)

    # Write the personalized invitation to a new text file for each invited person.
    with open(
        f"Location of invitation letters file/letter_for_{name}.txt","w+",) as f3:
        f3.write(invitation)
