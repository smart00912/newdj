from django.db import models
from datetime import datetime



class FirstModel(models.Model):
	GENDER_CHOICE = (
	(u'M' , u'Male'),
	(u'F' , u'Famile'),
)
	# custom primary key instead of default id colume and have to spicify auto_created here
	cid = models.AutoField(auto_created=True, primary_key=True)
	name = models.CharField(max_length=10)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=2,choices=GENDER_CHOICE)
	date = models.DateField(default=datetime.now, blank=True)


class BookType(models.Model):
	bookname = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.bookname

# one to one
class Libary(models.Model):
	numbers = models.IntegerField(null=True)
	AveragePrice = models.IntegerField(null=True)
	type =  models.ForeignKey(BookType)
	
	def __unicode__(self):
#have to convert int to unicode otherwise will get error : coercing to Unicode: need string or buffer, long found
		return unicode( self.numbers)

# many to many
class Book(models.Model):
	book_name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.book_name
	

class Authers(models.Model):
	name = models.CharField(max_length=200)
	age = models.SmallIntegerField(null=True,help_text='Must between 20 to 100')
	books = models.ManyToManyField(Book)
	
	def __unicode__(self):
		return self.name
	

	