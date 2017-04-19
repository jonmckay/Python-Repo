'''
Created on Apr 19, 2017
This is an interactive command line Python calendar. Users are able to choose to view the calendar, add events, update existing events and delete existing events.
@author: jmckay
'''
from time import sleep, strftime

USERNAME = "Jon"

calendar = {}

def welcome():
    print "Welcome to the Python Calendar App %s!" % (USERNAME)
    print "Opening Calendar..."
    sleep(1)
    print strftime('%A %B %d, %Y')
    print strftime('%H:%M:%S')
    sleep(1)
    print 'What would you like to do?'
  
def start_calendar():
    welcome()
    start = True
    while(start):
        user_choice = raw_input('A to Add, U to Update, V to View, D to Delete, X to Exit: ')
        user_choice.upper()
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print 'Your Calendar is Empty'
            else:
                print calendar
        elif user_choice == 'U':
            date = raw_input('What date?: ')
            update = raw_input('Enter the update: ')
            calendar[date] = update
            print 'Update successful!'
            print calendar
        elif user_choice == 'A':
            event = raw_input('Enter event: ')
            date = raw_input('Enter date (MM/DD/YYYY)')
            if (len(date) > 10) or int(strftime('%Y')) > int(date[6:]):
                print 'Entered date is invalid'
                try_again = raw_input('Try Again? Y for Yes, N for No: ')
                try_again = try_again.upper()
                print try_again
                if try_again == 'Y':
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print 'Event was successfully added'
                print calendar
        elif user_choice == 'D':
            if len(calendar.keys()) < 1:
                print 'Your calendar is empty'
            else:
                event = raw_input('What event?: ')
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print 'Event successfully deleted'
                        print calendar            
                else:
                    print 'Event does not exist'
        elif user_choice == 'X':
            start = False
        else:
            print 'Invalid command entered'
            start = False
 
start_calendar()