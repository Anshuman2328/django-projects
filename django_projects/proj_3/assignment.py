# to retrieve all users
User.objects.all()

# get last user
User.objects.last()

# create few records for users
User.objects.create(first_name="name",last_name="lname",email_address="fname@company.com",age=30)


# How to get first user
User.objects.first()

# How to sort by frst name
User.objects.order_by("first_name")

# To update the last name
x=User.objects.get(id=4)
x.last_name ="new_last_name"
x.save


# To delete a records
user.objects.delete(id=3)


Ninja-Dojo Assignment

# Create the Dojo and Ninja's same way as above, Created three dojo and create 3 ninja in each of the Dojo. 
# To create a dojo use the command

# Dojo.objects.create(field="value",field="value,field="value"). 

# Provide a foreign key relationship for ninja class as one ninja can have only one dojo but a dojo can have many ninjas
# This is done so that when we create a ninja, we can specify which dojo it belongs to


# to create a ninja, 

# Ninja11 = Ninja.objects.create(fname="value", lname="value", dojo=Dojo.objects.get(id=1)). This will ensure that ninja goes to the right dojo. 





Authors and Books Assignment




#  Authors.objects.get(id=2).books.all()

# #   this shows all the books written by the Author with id =2

#  Authors.objects.get(id=3)


#  #   this shows all the books written by the Author with id =3

#   a.authors.all()

#   retrieves all the authors for this particular books

# Books.objects.get(id=3).authors.remove(Authors.objects.get(id=2))

# removes a particular author for the particular book

#  x.books.add(Books.objects.get(id=4))

# x is the particular author who is being added to a particular book


Books/Likes Assignment


# 1. User.objects.create(name="variable name")

# 2. Book.objects.create(name="Variable book name", upload_by=User.objects.get(id=1)) This will allow first user to upload/create a book

#  Book.objects.first().user_liked.add(x)------ This gets the first book and then gets liked by user = x. 
#  x is the particular user that you want to have. basically the user who liked this book.

# To display all the users who liked one book, select that book and do a query for user_liked and all
# Book.objects.last().user_liked.all()--- this gets the last book and shows all those who liked it

#  Book.objects.first().user_upload  This shows the user who uploaded first book
#  User.objects.first().book_uploaded.all(). This shows all the books that were uploaded by the user










