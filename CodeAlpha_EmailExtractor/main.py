import re

try:
    with open("input.txt", "r", encoding="utf-8") as file:
        content = file.read()

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        content
    )

    emails = sorted(set(emails))

    with open("emails.txt", "w", encoding="utf-8") as output:
        for email in emails:
            output.write(email + "\n")

    print("\nEmail extraction successful!\n")

    if emails:
        print("Extracted Email Addresses:")
        for i, email in enumerate(emails, start=1):
            print(f"{i}. {email}")

        print(f"\nTotal Emails Found: {len(emails)}")
    else:
        print("No email addresses found.")

except FileNotFoundError:
    print("Error: input.txt file not found.")