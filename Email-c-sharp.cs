using System;
using MimeKit;
using MailKit.Net.Smtp;
using MailKit.Security;
using System.Net.Mail;

class Program
{
    static void Main()
    {
        // SMTP server configuration
        string smtpServer = "smtp.mailrcld.com"; // Replace with your SMTP server address
        int smtpPort = 587; // Usually, 587 for TLS
        string smtpUsername = "client-email@domain.com"; // Replace with your email address from settings
        string smtpPassword = ""; // Replace with your email password

        // Email details
        string fromAddress = "support@domain.com"; // Replace with your email address
        string toAddress = "email@gmail.com"; // Replace with recipient's email address
        string subject = "Test Email";
        string body = "This is a test email sent using MailKit with TLS security.";

        try
        {
            var message = new MimeMessage();
            message.From.Add(new MailboxAddress("", fromAddress));
            message.To.Add(new MailboxAddress("Recipient", toAddress));
            message.Subject = subject;
            message.Body = new TextPart("plain")
            {
                Text = body
            };

            using (var client = new MailKit.Net.Smtp.SmtpClient())
            {
                Console.WriteLine("Connecting to SMTP server...");
                client.Connect(smtpServer, smtpPort, SecureSocketOptions.StartTls);

                Console.WriteLine("Authenticating...");
                client.Authenticate(smtpUsername, smtpPassword);

                Console.WriteLine("Sending email...");
                client.Send(message);

                Console.WriteLine("Disconnecting...");
                client.Disconnect(true);
                Console.WriteLine("Email sent successfully.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception: " + ex.Message);
            if (ex.InnerException != null)
            {
                Console.WriteLine("Inner Exception: " + ex.InnerException.Message);
            }
        }
    }
}
