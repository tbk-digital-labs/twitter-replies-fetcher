# Fetch All Tweet Replies (using Python + Tweepy)
## Using Twitter API for data fetching

After hours of trying, we finally made a solution that allows us to retrieve a large amount of tweets and filter them but beware, the fetch might take a while (rate limits)!

You must have a [Twitter Developer account](https://developer.twitter.com/) and you will need to add your keys within the code (you should also have a project there). 

Navigate to where you downloaded your code, assuring you have [Tweepy](https://www.tweepy.org/) installed within the same environment.

## Running

```
python twitter_reply.py
python add_addresses_column_to_csv.py
```

The replies will be in a .csv file within the same directory. 
If replies contain Ethereum addresses, you can run the 2nd command to add a new column with the addresses. 

This code is free to use, but please give credit to the original author (TBK Digital Labs).
