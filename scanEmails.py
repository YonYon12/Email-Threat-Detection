import os
import yara 

try:
    rules = yara.compile(filepath='myYaraRules.yar')
except yara.Error as e:
    print(f"Error compiling YARA rules: {e}")
    rules = None

def scan_for_threats(emails):
    # TODO: Create defensive coding to prevent errors / crashes.

    """
    Scan a list of emails for malware threats.
    """

    flaged_emails = []

    for email in emails:
        # TODO: integrate scanMalware logic
        malware_result = scan_malware(email)
        phishing_result = phishing_check(email)

        if malware_result or phishing_result:
            flaged_emails.append(email)

    return flaged_emails
    
def scan_malware(email):
    """
    Scans email links and attachments for malicious payloads.
    Returns True if a threat is detected, False otherwise.
    """
    # TODO: implement actual scanning logic for attatchements and links
    raise False # Placeholder to indicate no threat detected

def phishing_check(email):
    # TODO: clean up code, implement cleaner logic as well as subject checks
    if not rules:
        return False
    
    email_subject = email.get("subject")
    email_body = email.get("body")

    phishing_match = rules.match(data=email_body)
    if phishing_match:
        print("Phishing threat detected inside email body : ")
        print("\n Text: " + email_body)
        return True
    return False