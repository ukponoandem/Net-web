import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject,body,to_email,from_email,password):
    # Create a multipart message
    Message = MIMEMultipart()
    Message ["From"] = from_email
    Message ["To"]= to_email
    Message ["subject"] = subject
    
      # Add body to email
    Message.attach(MIMEText(body, "plain"))

    try:
      # Connect to Outlook's SMTP server
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
        # server.starttls()  # Start TLS encryption
        server.login(from_email, password)  # Login to your account
        
          # Send email
        server.sendmail(from_email, to_email, Message.as_string())
        print("Email sent successfully!")
        
        
              
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Failed to send email. Error: {e}")
        
    finally:
        # Close the connection to the server
        if server:
            server.quit()
