// Package main defines an application that sends a simple HTML email.
package main

import (
    "fmt"
    "gopkg.in/gomail.v2"
)

func main() {
    // Create a new email message.
    m := gomail.NewMessage()
    
    // Set essential headers: sender, recipient, and subject.
    m.SetHeader("From", "your_email@yourdomain.com")
    m.SetHeader("To", "recipient_email@theirdomain.com")
    m.SetHeader("Subject", "Welcome to Our Service!")

    // Define the HTML content of the email.
    m.SetBody("text/html", `This is a sample email to test SMTP settings`)

    // Configure the mail server connection with dummy credentials.
    d := gomail.NewDialer("smtp.yourdomain.com", 587, "username@yourdomain.com", "password")

    // Send the email, logging errors or success.
    if err := d.DialAndSend(m); err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Message sent successfully")
    }
}
