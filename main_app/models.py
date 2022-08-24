from django.db import models

LISTTYPES = (
    ('I', 'Items'),
    ('T', 'Tasks'),
)


# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length = 5,
        choices=LISTTYPES,
        default=LISTTYPES[0][0]
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']