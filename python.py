#Importing libraries
import sys
import os
import jsonpickle
import tweepy

#Pass our consumer key and consumer secret to Tweepy's user authentication handler
auth = tweepy.OAuthHandler("Py5YhjOq4QOkwWdvXzvvmZDBe", "M6WO2hEsfTThiaMl757z1uSLfWvJoqFNNSGyyuHOHIry4D86nD")

#Pass our access token and access secret to Tweepy's user authentication handler
auth.set_access_token("753276768690188289-a2cuZaIGXqwW4PU7p26gUFEJMmjQYkU", "wNA0kRrwJn0UwZMkl0NFg9R14N6bCrYpvQt0uXbqgTfng")

#Creating a twitter API wrapper using tweepy
#Details here http://docs.tweepy.org/en/v3.5.0/api.html
api = tweepy.API(auth)

#Error handling
if (not api):
    print ("Problem connecting to API")
	
#Getting Geo ID for USA
places = api.geo_search(query="INDIA", granularity="country")

#Copy USA id
place_id = places[0].id
print('USA id is: ',place_id)

results = api.search(q="Support Modi")

for result in results:
    print result.text