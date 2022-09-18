from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response

from time_series.models import DailyReturns

   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        print(request.POST)
        return render(request, 'chart.html')
   
   

   
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        x_ = DailyReturns.objects.filter(equity_id=request.session['selected_eq']).order_by('date').values()
        labels, chartdata = [], []
        for row in x_:
            labels.append(row['date'])
            chartdata.append(row['returns'])
        # labels = [
        #     'January',
        #     'February', 
        #     'March', 
        #     'April', 
        #     'May', 
        #     'June', 
        #     'July'
        #     ]
        chartLabel = "Equity return"
        # chartdata = [0, 10, 5, 2, 20, 30, 45]
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)