from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name='Home'),
    path('contact',views.contact,name='contact'),
    path('why_us',views.why_us,name='why_us'),
    path('project',views.project,name='project'),
    path('who_we_are',views.who_we_are,name='who_we_are'),
    path('Our_Team',views.Our_Team,name='Our_Team'),
    path('How_we_operate',views.How_we_operate,name='How_we_operate'),
    path('Health_and_safety',views.Health_and_safety,name='Health_and_safety'),
    path('G_implementation',views.G_implementation,name='G_implementation'),
    path('Communication_system',views.Communication_system,name='Communication_system'),
    path('Data_implementation',views.Data_implementation,name='Data_implementation'),
    path('Telecommunication',views.Telecommunication,name='Telecommunication'),
    path('Design_network',views.Design_network,name='Design_network'),
    path('Disaster_recovery',views.Disaster_recovery,name='Disaster_recovery'),
    path('Edge_computer_network',views.Edge_computer_network,name='Edge_computer_network'),
    path('Local_area',views.Local_area,name='Local_area'), 
    path('Network_automation',views.Network_automation,name='Network_automation'),
    path('Network_Virtualization',views.Network_Virtualization,name='Network_Virtualization'), 
    path('Network_Integration',views.Network_Integration,name='Network_Integration'),
    path('Network_Traffic_Analysis',views.Network_Traffic_Analysis,name='Network_Traffic_Analysis'), 
    path('Network_Security',views.Network_Security,name='Network_Security'), 
    path('Voip_Network',views.Voip_Network,name='Voip_Network'), 
    path('Vpn_Implementation',views.Vpn_Implementation,name='Vpn_Implementation'), 
    path('Wide_Area_Network',views.Wide_Area_Network,name='Wide_Area_Network'),   
    path('Wifi_Implementation',views.Wifi_Implementation,name='Wifi_Implementation'), 
    path('Wireless_Design',views.Wireless_Design,name='Wireless_Design'),  
    path('Enterprise_Network',views.Enterprise_Network,name='Enterprise_Network'),  
    path('Remote_Network_Monitoring',views.Remote_Network_Monitoring,name='Remote_Network_Monitoring'),  
    path('email_sender/',views.email_sender,name='email_sender')
]

