<?php

require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';
require 'PHPMailer/src/Exception.php';

use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;

try {
    $mail = new PHPMailer(true);
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;
    $mail->isSMTP();
    $mail->Host = 'your_host_address';
    $mail->SMTPAuth = true;
    $mail->Username = 'your_username';
    $mail->Password = 'your_password';
    $mail->SMTPSecure = 'tls';
    $mail->Port = 587;
    $mail->setFrom('your_email_address', "From Name");
    $mail->addAddress('recipient_email_address');
    $mail->Subject = "Your Email Subject";
    $mail->Body = 'This is a sample email to test SMTP settings.';
    $mail->CharSet = 'UTF-8';
    $mail->IsHTML(true);

    if (!$mail->send()) {
        echo 'Mailer Error: ' . $mail->ErrorInfo;
    } else {
        echo 'Message sent successfully!';
    }
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
