from __future__ import print_function

import datetime
import os.path
import requests
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from datetime import datetime, timedelta

def init_calender():

    SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/calendar.events.readonly", "https://www.googleapis.com/auth/calendar.events"]

    try:
    
        refresh_access_token()

        creds = None
        if os.path.exists('STORAGE\Tokens\calendar_token.json'):
            creds = Credentials.from_authorized_user_file('STORAGE\Tokens\calendar_token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('STORAGE\google_cred_files\calendar_creds.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('STORAGE\Tokens\calendar_token.json', 'w') as token:
                token.write(creds.to_json())
    
    except:

        creds = None
        if os.path.exists('STORAGE\Tokens\calendar_token.json'):
            os.remove('STORAGE\Tokens\calendar_token.json')
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('STORAGE\google_cred_files\calendar_creds.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('STORAGE\Tokens\calendar_token.json', 'w') as token:
                token.write(creds.to_json())
    
    service = build('calendar', 'v3', credentials=creds)

    return service

def create_event(startYear, startMonth, startDay, endYear, endMonth, endDay, 
                calendar, summary, location = "", description = "", 
                startHour = 0, startMinute = 0, startSecond = 0, endHour = 0, endMinute = 0, endSecond = 0, 
                reccurenceFreq = "", reccurenceInterval = "", reccurenceCount = "", reccurenceUntil = "", reccurenceByDays = [], 
                rDates = [], exDates = []): 
    
    service = init_calender()

    try:

        startTime = datetime(startYear, startMonth, startDay, startHour, startMinute, startSecond)
        endTime = datetime(endYear, endMonth, endDay, endHour, endMinute, endSecond)

        rDateString = ""
        if (len(rDates) != 0):        
            for date in rDates:
                rDateString += date[0]
                rDateString += date[1]
                rDateString += date[2]
                rDateString += ';'
        
        exDateString = ""
        if (len(exDates) != 0):
            for date in exDates:
                exDateString += date[0]
                exDateString += date[1]
                exDateString += date[2]
                exDateString += ';'

        byDayString = ""
        if (len(reccurenceByDays) != 0):
            for i in range(len(reccurenceByDays)):
                byDayString += reccurenceByDays[i]
                if (i != (len(reccurenceByDays)-1)):
                    byDayString += ','

        if (len(rDates) != 0 and len(exDates) != 0):

            if (reccurenceCount == "" and reccurenceUntil == ""):
                
                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};BYDAY={byDayString}',
                            f'RDATE;VALUE=DATE:{rDateString}',
                            f'EXDATE;VALUE=DATE:{exDateString}',
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval}',
                            f'RDATE;VALUE=DATE:{rDateString}',
                            f'EXDATE;VALUE=DATE:{exDateString}',
                        ],
                    }

            elif (reccurenceCount == ""):

                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};UNTIL={reccurenceUntil};BYDAY={byDayString}',
                            f'RDATE;VALUE=DATE:{rDateString}',
                            f'EXDATE;VALUE=DATE:{exDateString}',
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};UNTIL={reccurenceUntil};',
                            f'RDATE;VALUE=DATE:{rDateString}',
                            f'EXDATE;VALUE=DATE:{exDateString}',
                        ],
                    }
            
            elif (reccurenceUntil == ""):

                if (reccurenceInterval == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};COUNT={reccurenceCount};BYDAY={byDayString}',
                            f'RDATE;VALUE=DATE:{rDateString}',
                            f'EXDATE;VALUE=DATE:{exDateString}',
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles',
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};COUNT={reccurenceCount};',
                            f'RDATE;VALUE=DATE:{rDateString}',
                            f'EXDATE;VALUE=DATE:{exDateString}',
                        ],
                    }

        elif (len(rDates) != 0 and len(exDates) == 0):

            if (reccurenceCount == "" and reccurenceUntil == ""):
                
                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};BYDAY={byDayString}',
                            f'RDATE;VALUE=DATE:{rDateString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval}',
                            f'RDATE;VALUE=DATE:{rDateString}'
                        ],
                    }

            elif (reccurenceCount == ""):

                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};UNTIL={reccurenceUntil};BYDAY={byDayString}',
                            f'RDATE;VALUE=DATE:{rDateString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};UNTIL={reccurenceUntil};',
                            f'RDATE;VALUE=DATE:{rDateString}'
                        ],
                    }
            
            elif (reccurenceUntil == ""):

                if (reccurenceInterval == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};COUNT={reccurenceCount};BYDAY={byDayString}',
                            f'RDATE;VALUE=DATE:{rDateString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};COUNT={reccurenceCount};',
                            f'RDATE;VALUE=DATE:{rDateString}'
                        ],
                    }

        elif (len(rDates) == 0 and len(exDates) != 0):

            if (reccurenceCount == "" and reccurenceUntil == ""):

                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};BYDAY={byDayString}',
                            f'EXDATE;VALUE=DATE:{exDateString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval}',
                            f'EXDATE;VALUE=DATE:{exDateString}'
                        ],
                    }

            elif (reccurenceCount == ""):

                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};UNTIL={reccurenceUntil};BYDAY={byDayString}',
                            f'EXDATE;VALUE=DATE:{exDateString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};UNTIL={reccurenceUntil};',
                            f'EXDATE;VALUE=DATE:{exDateString}'
                        ],
                    }
            
            elif (reccurenceUntil == ""):

                if (reccurenceInterval == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};COUNT={reccurenceCount};BYDAY={byDayString}',
                            f'EXDATE;VALUE=DATE:{exDateString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};COUNT={reccurenceCount};',
                            f'EXDATE;VALUE=DATE:{exDateString}'
                        ],
                    }

        elif (len(rDates) == 0 and len(exDates) == 0):

            if (reccurenceCount == "" and reccurenceUntil == ""):

                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};BYDAY={byDayString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval}'
                        ],
                    }

            elif (reccurenceCount == ""):

                if (reccurenceInterval == ""):
                    
                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};UNTIL={reccurenceUntil};BYDAY={byDayString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};UNTIL={reccurenceUntil};'
                        ],
                    }
            
            elif (reccurenceUntil == ""):

                if (reccurenceInterval == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};COUNT={reccurenceCount};BYDAY={byDayString}'
                        ],
                    }

                elif (byDayString == ""):

                    event = {
                        'summary': summary,
                        'location': location,
                        'description': description,
                        'start': {
                            'dateTime': startTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'end': {
                            'dateTime': endTime.strftime("%Y-%m-%dT%H:%M:%S"),
                            'timeZone': 'America/Los_Angeles'
                        },
                        'recurrence': [
                            f'RRULE:FREQ={reccurenceFreq};INTERVAL={reccurenceInterval};COUNT={reccurenceCount};'
                        ],
                    }

        cal_page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=cal_page_token).execute()
            for calendar_list_entry in calendar_list['items']:     
        
                if (calendar_list_entry['summary'] == calendar):
        
                    calId = calendar_list_entry['id']
                    break
        
            cal_page_token = calendar_list.get('nextPageToken')
            if not cal_page_token:
                break
        
        print(event)
        
        service.events().insert(calendarId=calId, body=event).execute()
    
    except:

        print("invalid inputs")

def delete_event(calendar, event):

    service = init_calender()

    try:

        cal_page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=cal_page_token).execute()
            for calendar_list_entry in calendar_list['items']:     
        
                if (calendar_list_entry['summary'] == calendar):
        
                    calId = calendar_list_entry['id']
                    break
        
            cal_page_token = calendar_list.get('nextPageToken')
            if not cal_page_token:
                break
        
        event_page_token = None
        while True:
            event_list = service.events().list(calendarId=calId, pageToken=event_page_token).execute()
            for event_list_entry in event_list['items']:     
        
                if (event_list_entry['summary'] == event):
        
                    eventId = event_list_entry['id']
                    break
        
            event_page_token = event_list.get('nextPageToken')
            if not event_page_token:
                break
        
        service.events().delete(calendarId=calId, eventId=eventId).execute()
        
    except:

        print("invalid event")

def get_event_by_name(summary):

    service = init_calender()
    
    cal_page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=cal_page_token).execute()
        for calendar_list_entry in calendar_list['items']:     

            event_page_token = None
            while True:
                events = service.events().list(calendarId=calendar_list_entry['id'], pageToken=event_page_token).execute()
                for event in events['items']:
                    
                    if (event['summary'] == summary):

                        return event

                event_page_token = events.get('nextPageToken')
                if not event_page_token:
                    break

        cal_page_token = calendar_list.get('nextPageToken')
        if not cal_page_token:
            break
    
    return "event not found"

def edit_event_by_name(summary, editType, editChange):
    pass

def create_calendar(summary):

    service = init_calender()
    
    calendar = {
    'summary': f'{summary}',
    'timeZone': 'America/Los_Angeles'
    }

    service.calendars().insert(body=calendar).execute()

def delete_calendar(summary):
    
    service = init_calender()

    try:
    
        cal_page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=cal_page_token).execute()
            for calendar_list_entry in calendar_list['items']:     

                if (calendar_list_entry['summary'] == summary):
                    calId = calendar_list_entry['id']

            cal_page_token = calendar_list.get('nextPageToken')
            if not cal_page_token:
                break

        service.calendars().delete(calendarId=calId).execute()
    
    except:

        print("invalid input")

def clear_calendar(summary):

    service = init_calender()

    try:
    
        cal_page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=cal_page_token).execute()
            for calendar_list_entry in calendar_list['items']:     

                if (calendar_list_entry['summary'] == summary):
                    calId = calendar_list_entry['id']

            cal_page_token = calendar_list.get('nextPageToken')
            if not cal_page_token:
                break

        service.calendars().clear(calId).execute()
    
    except:

        print("invalid input")

# create_event(2022, 9, 18, 2022, 9, 18, "test", "created event test", reccurenceFreq="DAILY", reccurenceInterval=2)

# delete_event("test", "created event test")

def refresh_access_token():

    with open("STORAGE\Tokens\calendar_token.json", 'r') as f:
        data = json.load(f)
        refresh_token = data["refresh_token"]

    client_id = "648229910272-2c6slfv75mkaokopq1b42b4pssvburrh.apps.googleusercontent.com"
    client_secret = "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"

    resp = requests.post('https://oauth2.googleapis.com/token', data={'grant_type':'refresh_token', 'client_id': client_id, 'client_secret':client_secret, 'refresh_token': refresh_token}, allow_redirects=True)

    a = resp.json()

    with open("STORAGE\Tokens\calendar_token.json", 'r') as f:
        data = json.load(f)
        data['token'] = a["access_token"]
    
    os.remove("STORAGE\Tokens\calendar_token.json")
    with open("STORAGE\Tokens\calendar_token.json", 'w') as f:
        json.dump(data, f, indent=4)

a = init_calender()

