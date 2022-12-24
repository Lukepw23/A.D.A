from __future__ import print_function

import datetime
import os.path
import requests
import json
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from datetime import datetime, timedelta

def init_people():

    SCOPES = ["https://www.googleapis.com/auth/profile.agerange.read", "https://www.googleapis.com/auth/user.addresses.read", "https://www.googleapis.com/auth/contacts.readonly", "https://www.googleapis.com/auth/user.organization.read", "https://www.googleapis.com/auth/directory.readonly", "https://www.googleapis.com/auth/user.phonenumbers.read", "https://www.googleapis.com/auth/user.birthday.read", "https://www.googleapis.com/auth/profile.emails.read", "https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/profile.language.read", "https://www.googleapis.com/auth/userinfo.email", "openid", "https://www.googleapis.com/auth/contacts.other.readonly", "https://www.googleapis.com/auth/user.emails.read", "https://www.googleapis.com/auth/contacts", "https://www.googleapis.com/auth/user.gender.read"]

    try:

        refresh_access_token()
        
        creds = None
        if os.path.exists('STORAGE\Tokens\people_token.json'):
            creds = Credentials.from_authorized_user_file('STORAGE\Tokens\people_token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('STORAGE\google_cred_files\people_creds.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('STORAGE\Tokens\people_token.json', 'w') as token:
                token.write(creds.to_json())
    
    except:

        creds = None
        if os.path.exists('STORAGE\Tokens\people_token.json'):
            os.remove('STORAGE\Tokens\people_token.json')
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('STORAGE\google_cred_files\people_creds.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('STORAGE\Tokens\people_token.json', 'w') as token:
                token.write(creds.to_json())
    
    service = build('people', 'v1', credentials=creds)

    return service

def refresh_access_token():

    with open("STORAGE\Tokens\people_token.json", 'r') as f:
        data = json.load(f)
        refresh_token = data["refresh_token"]

    client_id = "895623481270-fqf59aql4dm2icq4v5rmgunuritovpa6.apps.googleusercontent.com"
    client_secret = "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"

    resp = requests.post('https://oauth2.googleapis.com/token', data={'grant_type':'refresh_token', 'client_id': client_id, 'client_secret':client_secret, 'refresh_token': refresh_token}, allow_redirects=True)

    a = resp.json()

    with open("STORAGE\Tokens\people_token.json", 'r') as f:
        data = json.load(f)
        data['token'] = a["access_token"]
    
    os.remove("STORAGE\Tokens\people_token.json")
    with open("STORAGE\Tokens\people_token.json", 'w') as f:
        json.dump(data, f, indent=4)

def create_contact():

    person = {
        "names": [
            {
                "displayName": f"{prefix} {first_name} {middle_name} {last_name} {suffix}",
                "familyName": f"{last_name}",
                "givenName": f"{first_name}",
                "middleName": f"{middle_name}",
                "honorificPrefix": f"{prefix}",
                "honorificSuffix": f"{suffix}",
                "phoneticFamilyName": f"{phonetic_last}",
                "phoneticGivenName": f"{phonetic_first}",
                "phoneticMiddleName": f"{phonetic_middle}",
                "displayNameLastFirst": f"{last_name}, {prefix} {first_name} {middle_name}, {suffix}",
            }
        ],
        "nicknames": [
            {
                "value": f"{nickname}"
            }
        ],
        "birthdays": [
            {
                "date": {
                    "year": birth_year,
                    "month": birth_month,
                    "day": birth_day
                },
                "text": f"{birth_month}/{birth_day}/{birth_year}"
            }
        ],
        "addresses": [
            {
                "formattedValue": f"{street_address}\n{po_box}\n{street_address_line_2}, {city}, {state} {zip_code}\n{country}",
                "type": f"{address_label}",
                "poBox": f"{po_box}",
                "streetAddress": f"{street_address}",
                "extendedAddress": f"{street_address_line_2}",
                "city": f"{city}",
                "region": f"{state}",
                "postalCode": f"{zip_code}",
                "country": f"{country}",
                "countryCode": f"{country_code}"
            }
        ],
        "emailAddresses": [
            {
                "value": f"{email}",
                "type": f"{email_label}"
            }
        ],
        "phoneNumbers": [
            {
                "value": f"{phone_number}",
                "type": f"{phone_label}"
            }
        ],
        "biographies": [
            {
                "value": f"{notes}",
            }
        ],
        "urls": [
            {
                "value": f"{website}",
                "type": f"{website_label}",
            }
        ],
        "organizations": [
            {

                "name": f"{company}",
                "department": f"{department}",
                "title": f"{job_title}"
            }
        ],
        "relations": [
            {
                "person": f"{relationship}",
                "type": f"{relationship_label}",
            }
        ],
        "userDefined": [
            {
                "key": f"{custom_field_label}",
                "value": f"{custom_field}"
            }
        ],
        "gender": [
            {
                "value": f"{gender}"
            }
        ]
    }

def delete_contact():
    pass

def edit_contact():
    pass

try:
    service = init_people()

    # Call the People API
    print('List 10 connection names')
    results = service.people().connections().list(
        resourceName='people/me',
        # pageSize=10,
        personFields='addresses,ageRanges,biographies,birthdays,calendarUrls,clientData,coverPhotos,emailAddresses,events,externalIds,genders,imClients,interests,locales,locations,memberships,metadata,miscKeywords,names,nicknames,occupations,organizations,phoneNumbers,photos,relations,sipAddresses,skills,urls,userDefined'
        ).execute()

    
    connections = results.get('connections', [])

    for person in connections:
        print(person)
        # for a in person:
        #     print(a, end=" : ")
        #     print(person[a])
        #     print()
            
        print()

except HttpError as err:
    print(err)