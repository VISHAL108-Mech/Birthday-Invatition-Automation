# 🎂 Birthday Invitation Automation

A Python script that automates sending personalized birthday invitations to a list of guests — reads names from a file, fills in a reusable template, and generates a custom invitation letter for every single person, without writing a single line by hand.

> Give it a names list and a template once. It hands back a personalized letter for everyone on the list.

---

## 🎮 Demo — Sample Output

Given a template with placeholders, the script generates output like this for each guest:

```
Dear Dragon,

You are cordially invited to join us in celebrating
Bapu's Birthday.

📅 Date: 25-12-2026
🕐 Time: 06:00 PM
📍 Venue: Sunset Banquet Hall

Kindly RSVP by 20-12-2026.
We look forward to sharing this special occasion with you.

Warm regards,
Bapu
```

Each guest on the list gets their own letter, saved as an individual `.txt` file (e.g. `letter_for_Dragon.txt`, `letter_for_James.txt`), with the actual event details filled in exactly as entered at runtime.

---

## ✨ Features

- 📋 **Bulk personalization** — reads a plain-text list of guest names and generates one invitation per person automatically.
- 📝 **Template-driven design** — a single `template.txt` file with placeholder tags drives every generated letter, so updating the wording once updates it everywhere.
- 🔄 **Placeholder substitution** using `str.replace()` for name, sender, date, time, venue, and RSVP deadline.
- 🧹 **Whitespace-safe name parsing** via `.strip()`, so trailing newlines from `readlines()` don't leak into the final letters.
- 💾 **Individual file output** — each guest gets their own dynamically named `.txt` file (`letter_for_{name}.txt`) instead of one giant combined file.
- ⌨️ **Fully interactive event details** — prompts for the sender's name, event date, time, venue, and RSVP deadline at runtime, so the same script can be reused for any event without editing code.

---

## 🛠️ Tech Stack

| Category | Tool / Concept |
|---|---|
| Language | Python 3 |
| Core Concepts | File I/O, string manipulation, loops, dynamic file naming |
| Techniques | Template-based text generation, `str.replace()` chains, `readlines()` vs `read()` |
| Data Sources | Plain text files (`names.txt`, `template.txt`) |

---

## 📂 Project Structure

```
Birthday Invitation Automation/
│
├── invitation_script.py    # Main script — reads inputs, fills template, writes letters
├── names.txt                 # List of guest names, one per line
├── template.txt              # Reusable invitation template with placeholder tags
├── Letters/                   # Output folder — auto-generated personalized letters
│   ├── letter_for_Dragon.txt
│   └── letter_for_James.txt
└── README.md
```

Keeping the template, the guest list, and the generated output in separate files means you can update the wording, add/remove guests, or regenerate everything — without touching the script's logic at all.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed (uses only the standard library — no `pip install` needed)

### Setup
1. Add one guest name per line to `names.txt`.
2. Write your invitation wording in `template.txt`, using these placeholder tags anywhere you want dynamic content:

   | Placeholder | Gets Replaced With |
   |---|---|
   | `[Invited Person's Name]` | Each guest's name from `names.txt` |
   | `[Sender's Name]` | Entered via `input()` when the script runs |
   | `[Insert Date]` | Entered via `input()` when the script runs |
   | `[Insert Time]` | Entered via `input()` when the script runs |
   | `[Insert Location]` | Entered via `input()` when the script runs |
   | `[RSVP Date]` | Entered via `input()` when the script runs |

No need to edit the script for a new event — just run it and answer the prompts.

### Run it
```bash
git clone https://github.com/VISHAL108-Mech/Birthday-Invatition-Automation.git 
cd birthday-invitation-automation
python invitation_script.py
```

You'll be prompted for your name, then the script generates a personalized letter for every guest inside the `Letters/` folder.

---

## 🧩 How It Works

### 1. Getting the Event Details
The script opens by prompting for the sender's name and all the event-specific details — date, time, venue, and RSVP deadline — so the same script can be rerun for a completely different event without touching the code.

```python
sender_name = input("Enter Your Name: ")
event_date = input("Enter Date of Event: ")
event_time = input("Enter Time of Event: ")
venue = input("Enter Venue: ")
rsvp_date = input("Enter RSVP Date: ")
```

### 2. Reading the Guest List
`readlines()` pulls in every name from the names file as a list of strings — one entry per line, including the trailing newline character.

```python
with open("Location of invitation names file", "r") as f1:
    names = f1.readlines()
```

### 3. Reading the Template
The entire template is read in as a single string using `read()`, ready to be filled in per guest.

```python
with open("Location of invitation template file", "r") as f2:
    content = f2.read()
```

### 4. Personalizing Each Invitation
For every guest, the script strips stray whitespace/newlines from the name, then chains `.replace()` calls to swap out each placeholder tag with the real value.

```python
for name in names:
    name = name.strip()
    invitation = content.replace("[Invited Person's Name]", name)
    invitation = invitation.replace("[Sender's Name]", sender_name)
    invitation = invitation.replace("[Insert Date]", event_date)
    invitation = invitation.replace("[Insert Location]", venue)
    invitation = invitation.replace("[Insert Time]", event_time)
    invitation = invitation.replace("[RSVP Date]", rsvp_date)
```

### 5. Writing Each Personalized Letter
Each finished invitation is written out to its own dynamically named file, using an f-string to slot the guest's name straight into the filename.

```python
with open(
    f"Location of invitation letters file/letter_for_{name}.txt", "w+",
) as f3:
    f3.write(invitation)
```

---

## 📚 What This Project Demonstrates

- Reading and writing multiple files in a single script (`readlines()`, `read()`, `write()`)
- Building a reusable template system with placeholder-based substitution
- Iterating over a dataset (guest list) to generate a batch of personalized outputs
- Dynamic file naming with f-strings for organized, per-item output
- Practical automation of a genuinely repetitive real-world task

---

## 🔮 Future Improvements

- [ ] Add input validation (e.g. enforce a consistent date format instead of accepting any string)
- [ ] Add email delivery (e.g. via `smtplib`) instead of just generating text files
- [ ] Support CSV input for names + per-guest custom details (plus-ones, dietary notes, etc.)
- [ ] Add error handling for missing files or empty guest lists
- [ ] Generate invitations as styled PDFs instead of plain text

---

## 👤 Developer

**VISHAL YADAV**
- GitHub: https://github.com/VISHAL108-Mech
- LinkedIn: www.linkedin.com/in/vishal-yadav-2a91a7428
- Email: vy4122000@gmail.com
