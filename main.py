#Anthony Newton | Piedmont University | Algorithms | Final Project | 4/23/2023
#Information Technology Ticket Manager Implementation Using a Double-Ended Queue
from collections import deque

# create an empty deque to store the tickets
ticket_deque = deque()

# sample dictionary list of tickets
sample_tickets = [
    {"date_time": "2024-01-01 10:00", "summary": "Printer not working", "contact_info": "John Doe - john.doe@example.com", "location": "Library"},
    {"date_time": "2024-01-02 14:30", "summary": "WiFi connectivity issue", "contact_info": "Jane Smith - jane.smith@example.com", "location": "Student Union"},
    {"date_time": "2024-01-03 16:45", "summary": "Computer virus detected", "contact_info": "Bob Brown - bob.brown@example.com", "location": "Engineering building"}
]

# add sample tickets to the deque
ticket_deque.extend(sample_tickets)

# input method to accept new tickets
def add_ticket():
    date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    summary = input("Enter a summary of the issue: ")
    contact_info = input("Enter contact information: ")
    location = input("Enter the relevant university location: ")
    ticket = {"date_time": date_time, "summary": summary, "contact_info": contact_info, "location": location}
    ticket_deque.append(ticket)
    add_another = input("Would you like to add another ticket? (y/n): ")
    if add_another.lower() == "y":
        add_ticket()

# method to display all tickets in the deque
def display_tickets():
    print("All tickets in the deque:")
    for ticket in ticket_deque:
        print(ticket)

# method to display completed tickets
def display_completed_tickets():
    print("Completed tickets:")
    for ticket in sample_tickets:
        if ticket not in ticket_deque:
            print(ticket)

# method to remove tickets from the deque
def remove_ticket():
    ticket = ticket_deque.popleft()
    print("Ticket removed from the deque:", ticket)

# example usage of the above methods
add_ticket()
display_tickets()
remove_ticket()
display_completed_tickets()

