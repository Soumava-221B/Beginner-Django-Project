from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    like_numbers = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def count_likes(self):
        counter = len(Like.objects.filter(note=self))
        self.likes = counter
        self.save()
        return counter
    
class Like(models.Model):
    liker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_likes') 
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.liker.username} liked {self.note.title}" 