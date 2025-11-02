import requests, json
keyword = input("Enter keyword for the show you want to watch: ")

request = "https://api.tvmaze.com/search/shows?q=" + keyword

#exception handling
try:
    #response = requests.get(request).json()
    response = requests.get(request)

    if response.statues_code==200:
        json_string= response.json()
        #print(json.dumps(response, indent = 2))

        for a in response :
            print(a["show"],["name"])

except requests.exceptions.RequestException as e:
    print("Request could not be completed. ")




# Request template: https://api.tvmaze.com/search/shows?q=girls
#request = "https://api.tvmaze.com/search/shows?q=" + keyword
#response = requests.get(request).json()
#print(response)



#To change and filter by show name and position on the list
# you have to change the print statement
# You are basically iterating through the list
# print(response[0]["show"]["name"])

#this for loop if for filtering the data by the show name
# learning FLASK and JAVASCRIPT