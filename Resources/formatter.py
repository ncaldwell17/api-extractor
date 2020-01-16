class APIFormat(object):

    def __init__(self, service):

        str(service).lower()
        if service == 'nytimes' or service == 'new york times':
            self.api = self.nytimes()

    def nytimes(self):

        print('Please define type of API from the New York Times')
        api_type = input().lower()

        if api_type == 'archive':
            root = 'https://api.nytimes.com/svc/archive/v1/'

            print("Please insert the year that you would like to retrieve")
            year = int(input())

            print("Please insert the month that you would like to retrieve")
            month = int(input())

            print("Please insert your New York Times API account key")
            key = input()

            call = root+year+"/"+month+".json"+"?api-key="+key

        return call
