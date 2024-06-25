// Import the nodemailer module to handle email sending
const nodemailer = require('nodemailer');

/**
 * Asynchronously sends an email using SMTP settings.
 * This function sets up a mail transporter with STARTTLS security and
 * sends an email to a specified recipient.
 */
async function sendEmail() {
    // Configure SMTP transporter
    let transporter = nodemailer.createTransport({
        host: 'your-smtp-host.com',  // Replace with your SMTP host
        port: 587,
        secure: false,              // true for 465, false for other ports
        auth: {
            user: 'example@example.com', // Replace with SMTP username
            pass: 'password'             // Replace with SMTP password
        },
        requireTLS: true             // Enforce TLS as the security protocol
    });

    // Define email parameters
    let info = await transporter.sendMail({
        from: '"Sender Name" <sender@example.com>',  // Sender address
        to: 'recipient@example.com',                // List of recipients
        subject: 'Sample Email',                    // Subject line
        html: '<p>This is a sample email to test SMTP settings.</p>'  // HTML body content
    });

    // Log the result
    console.log('Message sent: %s', info.messageId);
}

// Trigger the sendEmail function to run
sendEmail();
