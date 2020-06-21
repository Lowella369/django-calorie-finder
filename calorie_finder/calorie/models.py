from django.db import models

# Create your models here.
class Food_PercentValue(models.Model):
  food_name = models.CharField(max_length=100)
  food_img = models.CharField(max_length=1000)
  food_serving_qty = models.IntegerField()
  food_serving_unit = models.CharField(max_length=100)
  food_calories = models.IntegerField()
  food_total_fat = models.FloatField()
  food_sat_fat = models.FloatField()
  food_cholesterol = models.FloatField()
  food_sodium = models.FloatField()
  food_carbo = models.FloatField()
  food_fiber = models.FloatField()
  food_sugar = models.FloatField()
  food_protein =  models.FloatField()
  rec_calorieIntake = 2000
  rec_dailyValueTotalFat = 65
  rec_dailyValueSatFat = 20
  rec_dailyValueCholesterol = 300
  rec_dailyValueSodium = 2400
  rec_dailyValueCarbo = 300
  rec_dailyValueFiber = 25
  rec_dailyValueCalcium = 1300
	
