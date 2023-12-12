from typing import List

def numUniqueEmails( emails: List[str]) -> int:
        unique_mail = set()
        for email in emails:
            email_parts = email.split('@')
            localpart = email_parts[0].replace('.', '')
            localpart = localpart.split('+')[0]
            forwarded_email = localpart + '@' + email_parts[1]
            unique_mail.add(forwarded_email)

        return len(unique_mail)
    
    
# Example 1:

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
numUniqueEmails(emails)
# Output: 2

# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

# Example 2:

emails_ = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3
numUniqueEmails(emails)
