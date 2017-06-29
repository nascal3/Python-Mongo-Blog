import uuid

from app.blog import Blog
from database import Database


class Menu(object):

    def __init__(self):
        self.user = input("Please insert your author name: ")
        self.user_blog=None
        if self._user_has_account():
            print("Welcome user {} ".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
       blog = Database.find_one(collection='blogs', query={'author': self.user})

       if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
       else:
           return False


    def _prompt_user_for_account(self):
        title = input("Enter Blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title = title,
                    description=description,
                    id=uuid.uuid4().hex
                    )

        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (r) or write (w) blog: ")

        if read_or_write == "r":
            self._list_blogs()
            self._view_blogs()
        elif read_or_write == "w":
            self.user_blog.new_post()
        else:
            print("Thank you for visiting")


    def _list_blogs(self):
        blogs =  Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID:{}, Title:{}, Author:{} ".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = input("enter ID of blog you want to see: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date:{}, Title:{}\n\n{}".format(post['created_date'], post['title'], post['content']))