# Python Email Sender with Gmail
This script allows you to send HTML emails using Gmail's SMTP server in Python.

# Usage

1. Clone this repository:
   git clone https://github.com/Sona_Gaud/python-email-sender.git

2. Navigate to the project directory:
   cd python-email-sender
   
3. Install the required dependencies using pip:
   pip install -r requirements.txt

4. Run the script:
   python send_email.py

5. Enter your Gmail password when prompted.

Note: If you have Two-Factor Authentication (2FA) enabled on your Gmail account, you may need to generate an App Password instead of using your regular Gmail password. Follow the instructions provided. 

Follow these steps to generate an App Password:

1. Go to your Google Account settings: https://myaccount.google.com/.
   In the "Security" section, find the "Signing in to Google" option and 
   select "App passwords".
2. If prompted, sign in to your Google Account.
3. Under "Select app", choose "Mail" and under "Select device", choose 
   "Other (Custom name)".
4. Enter a custom name for the app password (e.g., "Python Email Script") 
   and click "Generate".
5. Google will generate a 16-digit app password for you. Copy this password.
   Use this app password instead of your regular Gmail password in your 
   Python script.
