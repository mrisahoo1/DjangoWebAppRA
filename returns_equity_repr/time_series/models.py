from django.db import models

# Create your models here.
class DailyReturns(models.Model):
    date = models.DateField()
    returns = models.FloatField()
    equity_id = models.CharField(max_length=5)
    open_v = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()

class Equities(models.Model):
    equity_id = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField() 
    sector = models.CharField(max_length=100),
    industry = models.CharField(max_length=100)
    employees_count = models.IntegerField()
    sic_no = models.IntegerField()
    location = models.CharField(max_length=100)
    exchange_id = models.IntegerField()
    cik_no = models.CharField(max_length=100)
    cusip = models.CharField(max_length=100)
    currency_id = models.CharField(max_length=100)
    data_source_id = models.CharField(max_length=100)
    ckr_log = models.CharField(max_length=100)
    similar_fund_log = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    website= models.CharField(max_length=100)
    is_active = models.CharField(max_length=100)
    url_slug = models.CharField(max_length=100)
    delisted_date = models.DateField()
    delisted_reason = models.CharField(max_length=100)
    image_name  = models.CharField(max_length=100)
    image_aspect_ratio = models.FloatField()
    cumulative_return_update = models.CharField(max_length=100)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')