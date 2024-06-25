import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, username, password, recipient_emails, subject, body, html_content=None):
    """
    Send an email using the SMTP protocol with optional HTML content.
    
    Parameters:
    - sender_email (str): The email address from which the email is sent.
    - username (str): The username for SMTP server authentication.
    - password (str): The password for SMTP server authentication.
    - recipient_emails (list[str]): A list containing the recipient's email addresses.
    - subject (str): The subject line of the email.
    - body (str): The main content of the email in plain text.
    - html_content (str, optional): The HTML version of the email content.
    """
    
    # Initialize Multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)  # Convert list to comma-separated string
    msg['Subject'] = subject
    
    # Attach HTML or plain text content
    if html_content:
        msg.attach(MIMEText(html_content, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))

    # SMTP server configuration
    smtp_server = 'your.smtp.server'
    smtp_port = 587  # Use 465 for SSL if necessary
    SMTP_SECURITY = 'STARTTLS'  # Security protocol

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption

        # Login to the SMTP server using provided credentials
        server.login(username, password)

        # Send the email
        server.sendmail(sender_email, recipient_emails, msg.as_string())

        # Close the SMTP connection
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", str(e))

# Example usage parameters
sender_email = 'example@example.com'
password = 'YourSecurePassword'
recipient_emails = ['recipient@example.com']
subject = 'Test SMTP Configuration'
body = 'This is the plain text body of the email.'
username = 'your_username@example.com'

# HTML content specified as per user request
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Email Test</title>
</head>
<body>
    <p>This is a sample email to test SMTP settings.</p>
</body>
</html>
"""

# Call the function with the parameters and HTML content
send_email(sender_email, username, password, recipient_emails, subject, body, html_content)
