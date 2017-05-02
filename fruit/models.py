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
    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description
    def __str__(self):
        return self.name

class SectionItem(models.Model):
    section = models.CharField(max_length = 512)
    content = models.TextField()
    itemType = models.IntegerField()
    image = models.CharField(max_length = 512, null=True, blank = True)
    sectionItem = models.ForeignKey(Fruit, related_name='fruit_section') 
    def __str__(self):
        return self.section
    
    # def __init__(self, section, content, sectionItem, itemType = 1):
    #     self.section = section
    #     self.content = content
    #     self.sectionItem = sectionItem
    #     self.itemType = itemType

    def convert2Dictionary(self):
        return {"section":self.section, "content":self.content, "itemType":self.itemType , "image":self.image}