import os
import yara 

try:
    rules_files = {
        'malware_rules': 'rules/malware_rules.yar',
        'phishing_rules': 'rules/phishing_rules.yar'
    }
    rules = yara.compile(filepaths=rules_files)

except yara.Error as e:
    print(f"Error compiling YARA rules: {e}")
    rules = None

def scan_for_threats(emails):
    # TODO: Create defensive coding to prevent errors / crashes.

    flaged_emails = []

    for email in emails:
        # TODO: integrate scanMalware logic
        malware_result = scan_malware(email)
        phishing_result = phishing_check(email)

        if malware_result or phishing_result:
            flaged_emails.append(email)

    return flaged_emails
    
def scan_malware(email):
    
    for file_path in email.get("attachments", []):
        try:
            matches = rules.match(filepath=file_path)
            if matches:
                return True
        except Exception as e:
            print(f"Error scanning file {file_path}: {e}")
    
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