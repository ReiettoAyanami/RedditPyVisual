import praw

class from_subreddit:
    def __init__(self,sub_name,l):
        self. r = praw.Reddit(

            client_id="uRhfZiYd4eJcPw",
            client_secret="WfzjyAuLiW8LlQU7L8Qx_8zAJDGt4g",
            user_agent="gasjasgavbsdkjavsdjhvads",
        )
        self.name = sub_name
        self.subreddit = self.r.subreddit(self.name)
        self.limit = l

    def get_posts(self):    
        posts = []
        
        for post in self.subreddit.hot(limit = self.limit):
            
            if post.url.endswith('.jpg') or post.url.endswith('.png'):

                posts.append(post)

        return posts


    def get_url_list(self):
        urls = []
        for post in self.subreddit.hot(limit=self.limit):
            if post.url.endswith('.jpg') or post.url.endswith('.png'):
                urls.append(post.url)
        return urls

