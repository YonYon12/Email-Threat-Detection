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
        malware_result = scan_malware(email)
        phishing_result = phishing_check(email)

        if malware_result or phishing_result:
            flaged_emails.append(email)

    return flaged_emails
    
def scan_malware(email):
    if not rules:
        return False

    for file_path in email.get("attachments", []):
        if not os.path.isfile(file_path):
            continue

        try:
            matches = rules.match(filepath=file_path)
            for match in matches:
                if match.namespace == "malware_rules":
                    return True
        except Exception as e:
            print(f"Error scanning file {file_path}: {e}")

    return False

def phishing_check(email):
    if not rules:
        return False

    email_body = email.get("body", "")

    matches = rules.match(data=email_body)

    for match in matches:
        if match.namespace == "phishing_rules":
            print("Phishing threat detected inside email body:")
            print("\nText:", email_body)
            return True

    return False