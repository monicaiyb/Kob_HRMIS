from django.db import models
from common.models import BaseModel, BaseUserTrackedModel, BaseTimestampedModel

SEX = ["MALE", "FEMALE"]
# Create your models here.
class Department(BaseModel, BaseUserTrackedModel, BaseTimestampedModel):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(BaseModel, BaseUserTrackedModel, BaseTimestampedModel):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(BaseModel, BaseUserTrackedModel, BaseTimestampedModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField(null=True)
    SEX = models.TextChoices("Sex", " ".join(SEX))
    sex = models.CharField(
        max_length=6, choices=SEX.choices, default="MALE"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"