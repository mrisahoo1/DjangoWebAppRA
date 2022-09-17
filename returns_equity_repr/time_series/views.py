from http.client import HTTPResponse
from django.shortcuts import render
from .models import DailyReturns
import csv

# Create your views here.
def data_entry(req):
    with open('../data/daily_returns.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = DailyReturns.objects.get_or_create(
                date = row[0],
                returns = row[1],
                equity_id = row[2],
                open_v = row[3],
                high = row[4],
                low = row[5],
                close = row[6],
                adj_close = row[7],
                )
    return HTTPResponse("<h1>hi</h1>")