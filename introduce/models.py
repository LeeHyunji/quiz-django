from django.db import models

# Create your models here.
class AccessLog(models.Model):
    class Meta:
        db_table = "access_log"

    location = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        print(f'{self.created_at} / {self.location}')