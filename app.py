from database import Database
from post import Post

Database.initialize()

# post = Post(blog_id="123",
#             title="This is the title",
#             content="Lorem Ipsum stuff",
#             author="John Doe"
#             )

post = Post.from_blog('123')

print(post)
