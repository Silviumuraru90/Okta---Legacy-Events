import requests, json

#Org's API token
token = input("Input an API token, to authorize the requests: ")

headers = {"Authorization": "SSWS " + token,
           "Accept": "application/json",
           "Content-Type": "application/json"}

Order={
    "1":"DESCENDING",
    "2":"ASCENDING"
}

ignore_the_first_iteration = 0

print("Firstly, please fill in the form below all the necessary details:")

#Domain and Subdomain
print("\nConsidering the format for subdomain / domain as being: <tenant>.<okta*>.com \n")
tenant = input("Subdomain equals: ")
domain = input("Domain equals: ")

def main_data_aspects(event, n, x):
    pass

def raw_data(event, n, x):
    pass

def detailed_data(event, n, x):
        print("========================================")

        if x == 1:
            print("========== The only Event is: ==========")
        else:
            print("=========== Event nr. {} is: ===========".format(n))

        print("========================================\n")
        print("The Actor is:\n",event["actor"],"\n\n")
        print("The Client is:\n",event["client"],"\n\n")
        print("The Auth. Context is:\n",event["authenticationContext"],"\n\n")
        print("The Display Message is:\n",event["displayMessage"],"\n\n")
        print("The Event Type is:\n",event["eventType"],"\n\n")
        print("The Outcome is:\n",event["outcome"],"\n\n")
        print("It's been Published at:\n",event["published"],"\n\n")
        print("The Security Context is:\n",event["securityContext"],"\n\n")
        print("The Severity is:\n",event["severity"],"\n\n")
        print("The Debug Context is:\n",event["debugContext"],"\n\n")
        print("The Legacy Event you search with is:\n",event["legacyEventType"],"\n\n")
        print("The Transaction is:\n",event["transaction"],"\n\n")
        print("The UUID is:\n",event["uuid"],"\n\n")
        print("The Version is:\n",event["version"],"\n\n")
        print("The Request is:\n",event["request"],"\n\n")
        print("The Target is:\n",event["target"],"\n\n")
        print("========================================")
        print("========================================")
        print("========================================\n\n\n\n\n\n")

while True:
    if ignore_the_first_iteration != 0:
        cont = input("Do you want to continue with a new set of events? Y or N -> ").strip().lower()
        if cont == "n":
            break
        print("Firstly, please fill in the form below all the necessary details:")

    ignore_the_first_iteration += 1

    #Date - From / To
    print("\n\nNow, keeping in mind the format for date is yyyy-mm-dd,")
    since = input("\nStarting date is: ")
    until = input("Ending date is: ")

    #Legacy Event Type
    legacy_event_type = input("\n\nPlease input a 'legacyEventType', such as 'core.user.config.user_deactivated'\n")

    #Limit of Events displayed
    limit = int(input("\n\nNr. of events you want displayed is: \n").strip())

    #Descending or Ascending order
    order = int(input("\n\nIf you want the events to be displayed in a Descending order -> type 1,\n Or else, if you need to see them in an Ascending order -> type 2\n").strip())

    def main():
        n=0
        list_of_events = getEvents()
        if limit == 0:
            print("The limit should be != 0, if you want events to be displayed.")
        elif len(list_of_events) == 1:
            print("\n\n")
            detailed_data(list_of_events[0], limit)
        else:
            print("\n\n\nThe {} events are: \n\n".format(len(list_of_events)))
            for event in list_of_events:
                n += 1
                detailed_data(event, n, len(list_of_events))

    def getEvents():
        if order == 1:
            r = requests.get(f'https://{tenant}.{domain}.com/sage/api/v1/logs?since={since}T22%3A00%3A00Z&until={until}T20%3A59%3A59Z&limit={limit}&sortOrder={Order["1"]}&filter=legacyEventType+eq+%22{legacy_event_type}%22', headers = headers)
        else:
            r = requests.get(f'https://{tenant}.{domain}.com/sage/api/v1/logs?since={since}T22%3A00%3A00Z&until={until}T20%3A59%3A59Z&limit={limit}&sortOrder={Order["2"]}&filter=legacyEventType+eq+%22{legacy_event_type}%22', headers = headers)

        req = json.loads(r.text)
        return req

    main()