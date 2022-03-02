# Apologize for this test, I had to register for twitter API and don't have access to it now so I will explain how I would do it.
#
# First I found and endpoint that is returning an object containing the number of followers:
# https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show
#
# As you can see on the returned object user-object-definition contains a field follower_count
# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user
#
# In the script I will have to follow Twitter dev documentation to know how to build the requests with the API keys
# and get the token to use for authorization to use the API
# I could take this repository listed on twitter API doc to get examples https://github.com/tweepy/tweepy
#
# Or I could use python requests module or axios to make the REST requests
#
