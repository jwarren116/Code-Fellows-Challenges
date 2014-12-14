from django.db import models

class UserDetail(models.Model):

    class Meta:
        verbose_name_plural = "User Details"

    fname = models.CharField('First Name', max_length=100)
    lname = models.CharField('Last Name', max_length=100, blank=True)
    email = models.EmailField('Email')

    def __unicode__(self):
        return "%s %s" % (self.fname, self.lname)
