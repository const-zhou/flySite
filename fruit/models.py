from __future__ import unicode_literals

from django.db import models

# Create your models here.
import sys
reload(sys)
sys.setdefaultencoding("utf8")
# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length = 512)
    description = models.TextField()
    def __str__(self):
        return self.name

class SectionItem(models.Model):
    section = models.CharField(max_length = 512)
    content = models.TextField()
    itemType = models.IntegerField()
    sectionItem = models.ForeignKey(Fruit, related_name='fruit_section') 
    def __str__(self):
        return self.section