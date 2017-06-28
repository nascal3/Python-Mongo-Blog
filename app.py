from app.blog import Blog
from database import Database


Database.initialize()

blog = Blog(
            title="This is the blog",
            description="Lorem Ipsum stuff",
            author="John Blog"
            )

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(from_database)
