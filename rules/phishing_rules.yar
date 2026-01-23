
// Basic outline for common phishing tactics
rule Phishing_Tactics {
    meta:
        description = "Detects common urgency and account-lockout themes in phishing emails"
        author = "Anthony Romero"
        severity = "Medium"

    strings:
        // Urgency Phrases
        $u1 = "Urgent action required" nocase
        $u2 = "Immediate password check" nocase
        $u3 = "Final notice" nocase
        $u4 = "avoid legal action" nocase
        
        // Account Status Phrases
        $a1 = "account has been locked" nocase
        $a2 = "new device has logged into" nocase
        
        // Call to Action Phrases
        $c1 = "verify your account details" nocase
        $c2 = "Confirm your account changes" nocase

    condition:
        // Trigger if we find any TWO of these phrases. 
        // This reduces false positives from a single 'Urgent' word.
        2 of ($u*, $a*, $c*)
}