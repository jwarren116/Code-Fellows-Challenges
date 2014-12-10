#!/usr/bin/env python

"""This module manages a user-created Library with Shelf and Book 
classes.  The library can report all books it contains (book_report), 
as well as all shelves (shelf_report).  Each shelf can report all books 
it contains (book_report).  The user can (enshelf) or (unshelf) each 
book appropriately."""


class Library(object):

    def __init__(self, library_name):
        self.library_name = library_name
        self.list_of_shelves = []
        self.list_of_books = []

    def __str__(self):
        return self.library_name

    def shelf_report(self):
        print "There are %i shelves in the %s library." % (len(self.list_of_shelves), self.library_name)
        print "The shelves in %s are: %s" % (self.library_name, ", ".join(self.list_of_shelves))

    def book_report(self):
        print "Books in %s library: %s" % (self.library_name, "; ".join(self.list_of_books))


class Shelf(object):

    def __init__(self, shelf_name, library_name):
        self.shelf_name = shelf_name
        self.library_name = library_name
        self.library_name.list_of_shelves.append(shelf_name)
        self.books = []

    def __str__(self):
        return "%s shelf in the %s library" % (self.shelf_name, self.library_name)

    def book_report(self):
        print "Books on shelf %s: %s" % (self.shelf_name, "; ".join(self.books))


class Book(object):

    def __init__(self, book_name, library_name):
        self.book_name = book_name
        self.library_name = library_name
        self.library_name.list_of_books.append(book_name)

    def __str__(self):
        return "%s is on the %s" % (self.book_name, self.shelf_name)

    def enshelf(self, shelf_name):
        self.shelf_name = shelf_name
        self.shelf_name.books.append(self.book_name)

    def unshelf(self, shelf_name):
        self.shelf_name = shelf_name
        self.shelf_name.books.remove(self.book_name)


############
###Tests!###
############
burien = Library("Burien")
s1 = Shelf("S1", burien)
s2 = Shelf("S2", burien)
catch22 = Book("Catch 22", burien)
huckfinn = Book("The Adventures of Huckleberry Finn", burien)

catch22.enshelf(s1)
print catch22
s1.book_report()
huckfinn.enshelf(s1)
print huckfinn
s1.book_report()
catch22.unshelf(s1)
catch22.enshelf(s2)
s2.book_report()

burien.shelf_report()
burien.book_report()