from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __repr__(self):
        return f'Name of the User is {self.fname}{self.lname} and the email is {self.email}'














# Inside models.py
# # Create your models here.



# class Book(models.Model):
#     name = models.CharField(max_length=255)
#     # city = models.CharField(max_length=255)
#     # state = models.CharField(max_length=255)
#     # desc = models.CharField(max_length=500)
#     content = models.TextField()
#     user_upload = models.ForeignKey(User, related_name="book_uploaded", on_delete=models.CASCADE)
#     user_liked = models.ManyToManyField(User, related_name="book_liked")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)


#     def __repr__(self):
#         return f'Name of the Book is {self.name} and  its content is  {self.content} and uploaded by {self.user_upload} and liked by {self.user_liked}'




# class Dojo(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     # desc = models.CharField(max_length=500)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)


#     def __repr__(self):
#         return f'Name of the Dojo is {self.name} and  it located in {self.city} and it is in the state of {self.state}'



# class Ninja(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     dojo = models.ForeignKey(Dojo, related_name="ninja", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)


#     def __repr__(self):
#         return f'Name of the Ninja is {self.first_name}{self.last_name} and belongs to  {self.dojo}'

# class Comment(models.Model):
#     comment = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     # Notice the association made with ForeignKey for a one-to-many relationship
#     # There can be many comments to one blog
#     blog = models.ForeignKey(Blog, related_name = "comments", on_delete= models.CASCADE)

# Create your models here.   Below model was for user assignment
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # email_address = models.CharField(max_length=255)
    # age = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)
