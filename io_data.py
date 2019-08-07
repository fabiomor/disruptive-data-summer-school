from __future__ import print_function
import pandas
import pickle
import os.path
import csv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = '1y5HvjZgY3Fw2Qju9Y3KxpCsERJQcgTPFreHTXjWZSig'
SAMPLE_RANGE_NAME = 'Foglio1!A:B'


def read_uris_from_google_docs():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    values.pop(0)
    return split_values_to_lists(values)


def read_uris_from_csv():
    df = pandas.read_csv('uris.csv', header=0)
    return split_values_to_lists(df.values.tolist())


def read_words_from_csv():
    df = pandas.read_csv('words.csv')
    return df.values.tolist()


def split_values_to_lists(values):
    l1 = []
    l2 = []
    for i in values:
        try:
            if not pandas.isnull(i[0]):
                l1.append(i[0])
            if not pandas.isnull(i[1]):
                l2.append(i[1])
        except IndexError:
            continue
    return l1,l2


def write_to_csv(data, filename):
    with open(filename, 'w') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(data)
