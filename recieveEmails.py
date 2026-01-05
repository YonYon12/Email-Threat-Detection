import os
from imap_tools import MailBox, AND
import config

# Creates a list of flagged emails that should be checked for threats
def receive_emails():
    flagged_emails = []
    # Connect to the email server using credentials from config.py
    with MailBox(config.EMAIL_HOST).login(config.EMAIL_USER, config.EMAIL_PASS) as mailbox:

        # create quarantine directory if it doesn't exist
        os.makedirs(config.QUARANTINE_DIR, exist_ok=True)

        # Fetch new emails from the inbox
        for msg in mailbox.fetch(AND(seen=False)):
            email_data = {
                "sender": msg.from_,
                "subject": msg.subject,
                "body": msg.text,
                "attachments": []
            }
            
            # Process attachments if any
            for att in msg.attachments:
                if att.size <= config.MAX_FILE_SIZE:
                    save_path = os.path.join(config.QUARANTINE_DIR, att.filename)
                    with open(save_path, 'wb') as f:
                        f.write(att.payload)
                    email_data["attachments"].append(save_path)

            flagged_emails.append(email_data)

    return flagged_emails
                    
                    
                    
                    