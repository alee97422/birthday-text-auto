from twilio.rest import Client
import datetime

# Your Twilio account SID and auth token
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

# Your Twilio phone number and the recipient's phone number
twilio_number = "YOUR_TWILIO_NUMBER"
recipient_number = "RECIPIENT_PHONE_NUMBER"

# Your birthday message
birthday_message = "Happy Birthday! Have a wonderful day!"

# The recipient's birthday (in YYYY-MM-DD format)
recipient_birthday = "YYYY-MM-DD"

# Get the current date
now = datetime.datetime.now()

# Convert the recipient's birthday to a datetime object
birthday = datetime.datetime.strptime(recipient_birthday, "%Y-%m-%d")

# Check if today is the recipient's birthday
if now.month == birthday.month and now.day == birthday.day:
    # Send the birthday message using the Twilio API
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=recipient_number,
        from_=twilio_number,
        body=birthday_message
    )

    print("Birthday message sent to", recipient_number)
else:
    print("No birthday today")
