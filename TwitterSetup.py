import tweepy


auth = tweepy.OAuthHandler("Consumer Key (API Key)",
                           "Consumer Secret (API Key)")
auth.set_access_token("Access Token",
                      "Access Token Secret")
api = tweepy.API(auth)

# ----------fast way to get all the following (under 300) limit--------------
# following_ids=api.friends_ids("Twitter_username",-1)
# for friend in tweepy.Cursor(api.friends).items():
#     # Process the friend here
#     print(friend.name)


# All the people user_name is following with (10k+ followers)
def find_following(User_name):
    following_list = []
    following_ids=api.friends_ids(User_name,-1)
    sum=0
    for following in following_ids:
        cur_user=api.get_user(following)
        # check for "known" artists only
        if(cur_user.followers_count > 10000):
            following_list.append(cur_user.name)
        sum+=1
    return following_list
