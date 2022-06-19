from django.db import models


class DotList(models.Model):
    name = models.TextField(blank=True, null=True)
    computability = models.BooleanField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Coordinates(models.Model):
    dot = models.ForeignKey(DotList, models.DO_NOTHING)
    research = models.ForeignKey('visor.Research', models.DO_NOTHING)
    x_value = models.IntegerField()
    y_value = models.IntegerField()
    z_value = models.IntegerField()

    def __str__(self):
        return f'{self.x_value=}, {self.y_value=}, {self.z_value=}'


class DotPairs(models.Model):
    dot_1 = models.ForeignKey(DotList, models.DO_NOTHING, related_name='DotPairs_dot_1')
    dot_2 = models.ForeignKey(DotList, models.DO_NOTHING, related_name='DotPairs_dot_2')
    active = models.BooleanField(blank=True, null=True)
    line = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.dot_1} : {self.dot_2}"
