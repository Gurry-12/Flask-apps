def send_email(user_email, subject, message):
    """
    Placeholder for sending email. Integrate SMTP or third-party later.
    """
    print(f"Sending email to {user_email}\nSubject: {subject}\nMessage: {message}")
    return True

def send_alert_notification(user, alert):
    """
    Send alert notification (email/push/SMS)
    """
    subject = f"Disaster Alert: {alert.title}"
    message = f"{alert.description} | Severity: {alert.severity}"
    return send_email(user.email, subject, message)
