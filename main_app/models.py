from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# List Type for designating Lists as containing Items or Tasks
LISTTYPES = (
    ('I', 'Items'),
    ('T', 'Tasks'),
)

# Item Type for designating items as an Item or a Task
ITEMTYPES = (
    ('I', 'Item'),
    ('T', 'Task'),
)

# Time Estimates to add to tasks
TIMEESTIMATES = (
    ('0', ''),
    ('2', '2 Mins'),
    ('5', '5 Mins'),
    ('10', '10 Mins'),
    ('15', '15 Mins'),
    ('20', '20 Mins'),
    ('30', '30 Mins'),
    ('45', '45 Mins'),
    ('60', '1 Hr'),
    ('120', '2 Hrs'),
    ('180', '3 Hrs'),
    ('240', '4 Hrs'),
    ('300', '5 Hrs'),
    ('360', '6 Hrs'),
)

# Time Estimates to add to all list items items
PRIORITYLEVELS = (
    ('N/A', ''),
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
    ('HH', 'Highest'),
)


# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    type = models.CharField(
        max_length = 5,
        choices=LISTTYPES,
        default=LISTTYPES[0][0]
    )

   # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ListItem(models.Model):
    name = models.CharField(max_length=75)
    details = models.CharField(max_length=250)
    type = models.CharField(
        max_length = 3,
        choices=ITEMTYPES,
        default=ITEMTYPES[0][0]
    )
    time_estimate = models.CharField(
        max_length = 14,
        choices=TIMEESTIMATES,
        default=TIMEESTIMATES[0][0]
    )
    priority =  models.CharField(
        max_length = 5,
        choices=PRIORITYLEVELS,
        default=PRIORITYLEVELS[0][0]
    )
    created_at =  models.DateTimeField(auto_now_add=True)
    completed =  models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="lists")

   # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']