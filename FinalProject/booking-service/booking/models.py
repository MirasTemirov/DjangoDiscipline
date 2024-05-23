from django.db import models
from utils import models as utils_models
from datetime import datetime
from handbook.models import Object, Group


class Schedule(utils_models.AbstractModel):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='object_schedules')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_schedules')
    start = models.DateTimeField()
    end = models.DateTimeField()
    comment = models.TextField(null=True)

    def soft_delete(self):
        self.deleted_on = datetime.now()
        self.is_active = False
        self.save()


class BusinessHour(utils_models.AbstractModel):
    mon = models.BooleanField(default=False)
    mon_start = models.CharField(max_length=5, default='00:00')
    mon_end = models.CharField(max_length=5, default='23:59')

    tue = models.BooleanField(default=False)
    tue_start = models.CharField(max_length=5, default='00:00')
    tue_end = models.CharField(max_length=5, default='23:59')

    wen = models.BooleanField(default=False)
    wen_start = models.CharField(max_length=5, default='00:00')
    wen_end = models.CharField(max_length=5, default='23:59')

    thu = models.BooleanField(default=False)
    thu_start = models.CharField(max_length=5, default='00:00')
    thu_end = models.CharField(max_length=5, default='23:59')

    fri = models.BooleanField(default=False)
    fri_start = models.CharField(max_length=5, default='00:00')
    fri_end = models.CharField(max_length=5, default='23:59')

    sat = models.BooleanField(default=False)
    sat_start = models.CharField(max_length=5, default='00:00')
    sat_end = models.CharField(max_length=5, default='23:59')

    sun = models.BooleanField(default=False)
    sun_start = models.CharField(max_length=5, default='00:00')
    sun_end = models.CharField(max_length=5, default='23:59')
