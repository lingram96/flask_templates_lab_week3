from models.event import *

event1 = Event("16/09/2021", "Comic Con, ","500,", "Hall, ", "Convention for Cool People", True)
event2 = Event("20/10/2021", "E3 for Games","1000,", "Hydro, ", "Gaming Expo", True)
event3 = Event("24/12/2021", "CodeClan Christmas Party", "20, ", "Office, ", "Xmas party time", False)
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)