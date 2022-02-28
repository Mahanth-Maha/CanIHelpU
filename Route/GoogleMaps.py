import requests

class Maps:
    __api_file = open("Route\\api-key.txt", "r")
    __api_key = __api_file.readline()
    __api_file.close()
    print("CLASS MAPS INIT ---------------")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

    def __init__(self):
        pass

    def get_time_as_text(self,source,destination):
        r = requests.get(Maps.url + "origins=" + source + "&destinations=" + destination + "&key=" + Maps.__api_key) 
        return r.json()["rows"][0]["elements"][0]["duration"]["text"]       
    
    def get_time_in_seconds(self,source,destination):
        r = requests.get(Maps.url + "origins=" + source + "&destinations=" + destination + "&key=" + Maps.__api_key) 
        return r.json()["rows"][0]["elements"][0]["duration"]["value"]


if __name__ == '__main__':
    source = input("Enter a source address\n") 
    destination = input("Enter a destination address\n") 




  