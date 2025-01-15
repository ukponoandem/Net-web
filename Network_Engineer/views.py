from django.shortcuts import render




def Home(request):
    return render(request,"Home.html")


def contact(request):
    return render(request,"contact.html")

def why_us(request):
    return render(request,"why us.html")

def project(request):
    return render(request,"project.html")

def who_we_are(request):
    return render(request,"who we are.html")


def Our_Team(request):
    return render(request,"our Team.html")

def How_we_operate(request):
    return render(request,"How we operate.html")


def Health_and_safety(request):
    return render(request,"Health and safety.html")



def G_implementation(request):
    return render(request,"5G.html")


def Communication_system(request):
    return render(request,"com-system.html")


def Data_implementation(request):
    return render(request,"data.html")


def Telecommunication(request):
    return render(request,"telecom.html")

def Design_network(request):
    return render(request,"design.html")


def Disaster_recovery(request):
    return render(request,"disaster.html")


def Edge_computer_network(request):
    return render(request,"edge.html")

def Local_area(request):
    return render(request,"local-area.html")

def Network_Virtualization(request):
    return render(request,"virtualization.html")

def Network_automation(request):
    return render(request,"automation.html")

def Network_Traffic_Analysis(request):
    return render(request,"traffic-analysis.html")

def Network_Integration(request):
    return render(request,"integration.html")

def Network_Security(request):
    return render(request,"security.html")

def Voip_Network(request):
    return render(request,"voip.html")

def Vpn_Implementation(request):
    return render(request,"vpn.html")

def Wide_Area_Network(request):
    return render(request,"wide-area.html")

def Wifi_Implementation(request):
    return render(request,"wifi.html")

def Wireless_Design(request):
    return render(request,"wireless.html")

def Remote_Network_Monitoring(request):
    return render(request,"remote.html")

def Enterprise_Network(request):
    return render(request,"enterprise.html")




from .send_mail import send_email
from django.http import HttpResponse

def email_sender(request):
    if request.method == "POST":
        
      # Get form data
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        Message = request.POST.get('Message')
        number = request.POST.get('number')
        email = request.POST.get('email')
        page = request.POST.get('page') 
        # First_name = request.POST.get('Firstname')
        # Last_name = request.POST.get('Last_name')
        # message = request.POST.get('message')
        # Email = request.POST.get('email')
        
        
        print(f"Form submitted from: {page} by {First_name} {Last_name}")
        

        try:
            # Prepare subject and body for the email
            subject = f"Message from {First_name} {Last_name} on {page} with number {number}"
            body = Message
            to_email = 'ukponoadem@gmail.com'  # This is your email address
            from_email = 'ukponoadem@gmail.com'  # Same as sender's email (your email)
            password = 'eggf vykb lkxd yajo'  # Your email password or app password
            

            send_email(subject, body, to_email, from_email, password)
            return HttpResponse(f"Email sent successfully from {page} to {to_email}, check your inbox!")
        # return HttpResponse(f"Email sent successfully to {to_email}, check your inbox!")
        except Exception as e:
            return HttpResponse(f"Failed to send email: {e}")
        
        
        
        
    if request.path == 'email_sender/':
    #     # Render the default contact form template
        return render(request, 'contact.html') 
    # # You can also render different templates based on the 'page' value
    # # Example: Render different templates for design, disasters, or edge
    # if 'design' in request.path:
    #     return render(request, 'design.html')
    # elif 'disasters' in request.path:
    #     return render(request, 'disaster.html')
    # elif 'edge' in request.path:
    #     return render(request, 'edge.html')
        
    
    return render(request, 'contact.html')





# Create your views here.
