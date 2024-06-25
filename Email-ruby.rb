# This script uses the 'mail' gem to send emails with both text and HTML parts using SMTP.
# It handles multiple recipients and includes basic HTML content for demonstration.

require 'mail'

# Configure SMTP settings with dummy data for public sharing. Replace these with actual credentials.
Mail.defaults do
  delivery_method :smtp, {
    address:              'smtp.yourserver.com', # SMTP server address
    port:                 587,                   # SMTP port
    user_name:            'username',            # SMTP username
    password:             'password',            # SMTP password
    authentication:       'plain',               # Authentication type
    enable_starttls_auto: true                   # Enable TLS automatically if available
  }
end

# List of recipients
recipients = [
  'recipient1@example.com',
  'recipient2@example.com',
  'recipient3@example.com'
]

# Sending an email
begin
  Mail.deliver do
    from    'yourdomain@example.com' # Sender email address
    to      recipients.join(',')     # Joining the recipient array into a single string
    subject 'SMTP Settings Test'     # Email subject

    # Text part of the email
    text_part do
      body 'Hello, this is the text part of the email.'
    end

    # HTML part of the email
    html_part do
      content_type 'text/html; charset=UTF-8'
      body 'This is a sample email to test SMTP settings'
    end

    # Uncomment the following line and set the path to add an attachment
    # add_file '/path/to/attachment/file.pdf'
  end

  puts "Email sent successfully!"
rescue StandardError => e
  puts "Error sending email: #{e.message}"
end
