from django.db import models


class Division(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
class District(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='districts')
    
    def __str__(self) -> str:
        return self.name
    
    
class Upazilla(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="upazillas")
    
    def __str__(self) -> str:
        return self.name
    
    
class UnionArea(models.Model):
    name = models.CharField(max_length=100)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE, related_name='unions')
    
    def __str__(self) -> str:
        return self.name
    
    
class Village(models.Model):
    name = models.CharField(max_length=100)
    union_area = models.ForeignKey(UnionArea, on_delete=models.CASCADE, related_name='villages')
    
    def __str__(self) -> str:
        return self.name


# class Address(models.Model):
    