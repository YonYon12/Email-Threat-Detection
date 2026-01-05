import recieveEmails
import scanEmails

def main():
    # Step 1: Receive Emails
    emails = recieveEmails.fetch_emails()
    
    # Step 2: Scan Emails for Threats
    threats = scanEmails.scan_for_threats(emails)
    
    # Output the results
    if threats:
        print("Threats detected in the following emails:")
        for threat in threats:
            print(threat)
    else:
        print("No threats detected.")