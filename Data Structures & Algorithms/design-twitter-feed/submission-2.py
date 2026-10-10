from collections import defaultdict
class Twitter:

    def __init__(self):
        # self.users = defaultdict(lambda: {following:set(),tweets:[]})
        self.tweet_map = defaultdict(list)
        self.following_map = defaultdict(set)
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1
        # print(self.tweet_map)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # this will have user_ids, for all people that our user follows
        # keep track of the 10 recent, so use priority queue
        following_set = self.following_map[userId]
        following_set.add(userId)
        combined_posts = []
        for user in following_set:
            combined_posts.extend(self.tweet_map[user])
        combined_posts.sort(reverse = True)
        newest_posts = combined_posts[:10]

        return [pair[1] for pair in newest_posts]
       


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if I use list,for keeping track of all followers of that that user
        # I will have to search the entire list, so use set as the value            structure in our following_map, set is O(1) for lookups, remove is O(1)
        self.following_map[followerId].discard(followeeId)



# two separate hash maps, one for tweets the user id, 
# tweets_map
# {
#     user_id : [all tweets made]
#     user_id : [all tweets made]
# }
# following_map
# {
#     user_id : {all people they follow}
#     user_id : {all people they follow}
# }






