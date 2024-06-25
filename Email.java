import javax.mail.*;
import javax.mail.internet.*;
import java.util.Properties;

/**
 * The SendMail class provides functionality to send emails using JavaMail API.
 * It uses SMTP server details to authenticate and send email messages to specified recipients.
 */
public class SendMail {

    public static void main(String[] args) {
        // Sender's email and password as placeholders (replace with actual credentials securely)
        final String username = "your_email@example.com";
        final String password = "your_password";

        // Setup mail server properties
        Properties props = new Properties();
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", "smtp.example.com");
        props.put("mail.smtp.port", "587");

        // Create a session with authentication
        Session session = Session.getInstance(props, new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });

        try {
            // Create a default MimeMessage object and set its fields
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress("sender@example.com"));
            message.setRecipients(Message.RecipientType.TO,
                    InternetAddress.parse("recipient1@example.com,recipient2@example.com"));
            message.setSubject("Sample Subject");
            message.setText("This is a sample email content.");

            // Send the message
            Transport.send(message);

            System.out.println("Message sent successfully");
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
    }
}
