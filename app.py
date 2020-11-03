import re
import os
import platform
import requests

from colorama import init
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup

# Method to get the 'word' inside the HTML tag. I know it's so badly done but it works somehow. 
# For all this method functionality read: https://stackoverflow.com/questions/45700119/python-split-between-two-characters
def getContent(array):
    # array comes from soup.findAll(), even though in the array only comes 1 value ([0]) as a string.
    # It looks similar to this this: '<div class="x"><a href="#">Foo</a></div>' instead of coming as a array

    arrayTags = re.split("><", array) # ['<div class="x"', 'a href="#">Foo</a', '/div>']
    arrayTagsRefined = [arrayTags[0] + ">"]+["<" + i + ">" for i in arrayTags[1:-1]] + ["<" + arrayTags[-1]] # ['<div class="x">', '<a href="x">Foo</a>', '</div>']
    arrayTag = arrayTagsRefined[1] # We get: '<a href="x">Foo</a>'

    # Isolating 'Foo'
    arrayTag = re.split(">", arrayTag)
    arrayTag = re.split("<", arrayTag[1])

    word = arrayTag[0] # Get 'Foo'
    return word        # and return it

# This does the same as getContent() but some things are adapted.
def getTime(time):
    timeTags = re.split(">", time)
    
    try:
        timeTag = re.split(", ", timeTags[3])
        timeTag = re.split("<", timeTag[1])
    except:
        timeTag = re.split(", ", timeTags[2])
        timeTag = re.split("<", timeTag[0])

    eventTime = timeTag[0]
    return eventTime

# Python Colorama init() to support windows.
init(autoreset=True)

# REPLACE HERE THE CONTENT FROM CURL https://curl.trillworks.com/
# -------------------------------------------------------------

headers = {}
cookies = {}

# -------------------------------------------------------------

# Connecting to the calendar page while logged in
response = requests.get('http://plataforma2.siges21.com/calendar/view.php', headers=headers, cookies=cookies)

# Get page data
soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs with class 'event'
for event in soup.findAll(class_="event"):

    eventSubject = event.findChildren(class_="course", recursive=False) # Subject Name (ex: "Maths")
    eventName = event.findChildren(class_="referer", recursive=False) # Event Name (ex: "Exercise 1")
    eventDate = event.findChildren(class_="date", recursive=False) # Event Date (ex: "Tomorrow, 20:00")

    subject = str(eventSubject[0])
    task = str(eventName[0])
    date = str(eventDate[0])
    time = str(eventDate[0])

    # Getting the values
    subjectName = getContent(subject)
    taskName = getContent(task)
    eventDate = getContent(date)
    eventTime = getTime(time)

    # Message that the user will see per moodle event.
    print("")
    print(Back.BLACK + Fore.MAGENTA + f"▇ {subjectName} ▇")
    print(Fore.YELLOW + f"    \033[1m└ {taskName}") # '\033[1m' is to make it bold
    print(Fore.CYAN + f"        └ {eventDate} | {eventTime}")

print("")
