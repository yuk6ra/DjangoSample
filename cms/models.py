from django.db import models


class Habit(models.Model):
    """Habit"""
    habit_name = models.CharField('Habit Name', max_length=255)
    goal = models.CharField('Goal', max_length=255)
    start_date = models.DateField('Start date', blank=False)

    def __str__(self):
        return self.habit_name


class Record(models.Model):
    """Record　記録"""
    name = models.ForeignKey(Habit, verbose_name='Habit', related_name='records', on_delete=models.CASCADE)
    count = models.IntegerField('Count', blank=False, )
    comment = models.CharField('Comment', blank=True, max_length=255)
    date = models.DateField('Date', blank=False, )

    def __str__(self):
        # self.nameではなぜかエラーがでる
        return self.comment


class SmallGoal(models.Model):
    """Small Goals"""
    goal_name = models.CharField('Small Goal', max_length=255)
    comment = models.CharField('Comment', max_length=255)
    date = models.DateField('date',)

    def __str__(self):
        return self.goal_name

