import requests, json

token = ""

#Domain
print("\n\nConsidering the format for subdomain / domain as being: <tenant>.<okta*>.com\n")
tenant = input("Subdomain equals: ")
domain = input("Domain equals: ")

#Date
print("\n\nNow,keeping in mind the format for date is yyyy-mm-dd")
since = input("\nStarting date is: ")
until = input("Ending date is: ")

#Event Type
legacy_event_type = input("\n\nPlease input a 'legacyEventType', such as 'core.user.config.user_deactivated'\n=>")

#Limit
limit = int(input("\n\nNr. of events you want displayed is: \n").strip())

headers = {"Authorization": "SSWS " + token,
           "Accept": "application/json",
           "Content-Type": "application/json"}


def main():
    list_of_events = getEvents()
    if limit == 0:
        print("The limit should be != 0")
        return
    elif limit == 1:
        print("\n\n\n\nThe event is: \n\n", list_of_events)

    else:
        print("\n\n\n\nThe {} events are: \n\n".format(limit))
        for event in list_of_events:
            print(event, "\n")

def getEvents():
    r = requests.get(f'https://{tenant}.{domain}.com/sage/api/v1/logs?since={since}T22%3A00%3A00Z&until={until}T20%3A59%3A59Z&limit={limit}&sortOrder=DESCENDING&filter=legacyEventType+eq+%22{legacy_event_type}%22', headers = headers)

    req = json.loads(r.text)
    return req

main()
