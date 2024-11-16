
from django.db import models

class PolicyDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)  
    file = models.FileField(upload_to='policies/')       
    analysis_result = models.TextField(null=True, blank=True)  

    def __str__(self):
        return f"Policy Document {self.id}"
