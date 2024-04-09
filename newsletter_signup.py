import os

import requests

SHEETY_ENDPOINT = os.environ.get("SHEETY_USERS")

def post_new_row(first_name, last_name, email):
    body = {
      "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
      }
    }

    response = requests.post(SHEETY_ENDPOINT, json=body)
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    print("Welcom to Michal's Flight CLub.")
    print("We find the best flight deals and email you.")

    first_name = input("What is tour first name?\n")
    last_name = input("What is tour last name?\n")

    correct_emial = False
    email = None

    while not correct_emial:
        email = input("What is your email?\n")
        if email.lower() == "quit" or email.lower() == "exit":
            exit()
        email_check = input("Type your email again.\n")
        if email_check.lower() == "quit" or email_check.lower() == "exit":
            exit()

        if email == email_check:
            correct_emial = True
        else:
            print("Emails don't match. Please try again.\n")

    print("You're in the club!")

    post_new_row(first_name, last_name, email)
