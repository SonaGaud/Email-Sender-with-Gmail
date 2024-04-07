import smtplib
import ssl
from email.message import EmailMessage

def send_email():
    # Step 1: Define email parameters
    subject = "Add subject"
    body = "Type your message here"
    sender_email = "youraccount@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = input("Enter your password: ")

    # Step 2: Create an EmailMessage object
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Step 3: Construct HTML email body
    html = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    padding: 20px;
                }}
                h1 {{
                    color: #333333;
                }}
                p {{
                    color: #555555;
                }}
            </style>
        </head>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
            <p>This is a customized message. Feel free to modify it further!</p>
        </body>
    </html>
    """

    # Step 4: Attach HTML content to the message
    message.add_alternative(html, subtype="html")

    # Step 5: Create a secure SSL context
    context = ssl.create_default_context()

    print("Sending Email...")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)

    print("Email sent successfully!")

if __name__ == "__main__":
    send_email()
