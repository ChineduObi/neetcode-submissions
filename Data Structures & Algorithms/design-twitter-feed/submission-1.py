''' This is the naive approach. The idea is to use a sorting algorithm to sort them by timestamp(most recent first). Time is used to keep track of the tweets and every time a post is made the time (of the tweet) and the tweetid associated to the user is stored in the dictionary with the userId: userId -> [time, tweetId] .
'''
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        '''get the users tweets from the followMap and all the tweets for every followee in related to the user get th

        '''
        feed = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])

        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        #Allow only 
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
