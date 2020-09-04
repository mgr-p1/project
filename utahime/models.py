from django.db import models

class S_Idol(models.Model):
    idol   = models.CharField(max_length = 64)
    illust = models.CharField(max_length = 128)
    vocal  = models.IntegerField()
    dance  = models.IntegerField()
    visual = models.IntegerField()

    def __str__(self):
        return self.idol + ':' + self.illust + '(' + str(self.vocal) + ', ' + str(self.dance) + ', ' + str(self.visual) + ')'
