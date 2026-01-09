# Email-Threat-Detection

The purpose of this project is to develop a security tool designed to protect **personnel** from **phishing attempts**, malicious links, and **attachments** containing **malware**.

## Software Used

* **Mailtrap:** Used to **retrieve** and simulate test emails tailored to this project. This allows for the development of specialized emails containing phishing links, malware samples, or a combination of both in a controlled environment.
* **UTM:** Employed to host a **virtual machine** (VM) environment. This ensures the safety of the host computer by isolating malware and preventing "leaks" from the guest virtual machine to the host device.
* **YARA & ____:** These tools are used to identify and categorize threats within received emails. **YARA rules** are used to detect specific patterns related to phishing campaigns, 