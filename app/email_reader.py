import email
import imaplib
from typing import List

from .classifier import classify_mail
from .models import Task, db


def fetch_and_classify(mail_host: str, username: str, password: str) -> List[Task]:
    """Connects to the IMAP server, retrieves unseen mails and creates tasks."""
    tasks = []
    with imaplib.IMAP4_SSL(mail_host) as mail:
        mail.login(username, password)
        mail.select('inbox')
        status, data = mail.search(None, 'UNSEEN')
        if status != 'OK':
            return tasks

        for num in data[0].split():
            status, msg_data = mail.fetch(num, '(RFC822)')
            if status != 'OK':
                continue

            msg = email.message_from_bytes(msg_data[0][1])
            content = msg.get_payload(decode=True).decode(errors='ignore')
            site = classify_mail(content)
            task = Task(site=site, subject=msg.get('Subject', ''), body=content)
            db.append(task)
            tasks.append(task)
    return tasks
