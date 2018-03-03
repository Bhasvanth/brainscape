# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = '*****'
app_key = '*'

language = 'en'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))
result_json =  json.loads(r.text)
for records in result_json["results"][0]["lexicalEntries"] :
    print ("Type: "+str(records["lexicalCategory"]))
    for entry in records["entries"]:
        for sense in entry["senses"] :
            print("Def: "+ str(sense["definitions"]))
            for example in sense["examples"]:
                print ("Ex:- "+ str(example["text"]))
    print ("---------------")
