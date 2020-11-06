from django.db import models

# Create your models here.
class Project(models.Model):
        proj_name = models.CharField(max_length=16)
        gen_date = models.DateTimeField('date account created')
        creator_handle = models.CharField(max_length=20, null=True)
        def __str__(self):
            return self.proj_name + ' - ' + str(self.gen_date) + " " + str(self.creator_handle)
class Drawing(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    filetype = models.CharField(max_length=10)
    drawing_name = models.CharField(max_length=20)
    drawing_date = models.DateTimeField('date published')
    misc_data = models.CharField(max_length=20)
    
    def __str__(self):
        return self.drawing_name + ' - ' + str(self.drawing_date)
class Essay(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    filetype = models.CharField(max_length=10)
    essay_title = models.CharField(max_length=30)
    essay_date = models.DateTimeField('date published')
    misc_data = models.CharField(max_length=20)
    
    def __str__(self):
        return self.essay_title + ' - ' + str(self.essay_date)
class Video(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    filetype = models.CharField(max_length=10)
    video_name = models.CharField(max_length=20)
    video_date = models.DateTimeField('date published')
    misc_data = models.CharField(max_length=20)

    def __str__(self):
        return self.video_name + ' - ' + str(self.video_date)
