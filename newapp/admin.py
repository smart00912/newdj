# coding: utf8
from django.contrib import admin
from newapp2.models import Book,Libary,BookType,Authers,FirstModel


# 设置Choice表的显示样式
class ChoiceInline(admin.TabularInline):
	model = Book
	extra = 3

admin.site.register(Book)
admin.site.register(Libary)
admin.site.register(BookType)
admin.site.register(Authers)
admin.site.register(FirstModel)