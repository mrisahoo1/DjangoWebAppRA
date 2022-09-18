from http.client import HTTPResponse
from django.shortcuts import render
from .models import DailyReturns, Equities, Document
from .forms import DocumentForm
import csv
import matplotlib
import matplotlib.pyplot as plt
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def data_entry(request):
    # with open('../data/daily_returns.csv') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         _, created = DailyReturns.objects.get_or_create(
    #             date = row[0],
    #             returns = row[1],
    #             equity_id = row[2],
    #             open_v = row[3],
    #             high = row[4],
    #             low = row[5],
    #             close = row[6],
    #             adj_close = row[7],
    #             )
    # with open('../data/equities.csv') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         _, created = Equities.objects.get_or_create(
    #             equity_id = row[0],
    #             name = row[1],
    #             ticker = row[2],
    #             description = row[3],
    #             start_date = row[4],
    #             end_date = row[5],
    #             sector = row[6],
    #             industry = row[7],
    #             employees_count = row[8],
    #             sic_no = row[9],
    #             location = row[10],
    #             exchange_id = row[11],
    #             cik_no = row[12],
    #             cusip = row[13],
    #             currency_id = row[14],
    #             data_source_id = row[15],
    #             ckr_log = row[16],
    #             similar_fund_log = row[17],
    #             address = row[18],
    #             company_name = row[19],
    #             phone_no = row[20],
    #             website= row[21],
    #             is_active = row[22],
    #             url_slug = row[23],
    #             delisted_date = row[24],
    #             delisted_reason = row[25],
    #             image_name  = row[26],
    #             image_aspect_ratio = row[27],
    #             cumulative_return_update = row[28]
    #             )
    # x_ = DailyReturns.objects.filter(equity_id='10286').order_by('date').values()
    # x, y = [], []
    # for row in x_:
    #     x.append(row['date'])
    #     y.append(row['returns'])
    # matplotlib.use('agg')
    # plt.plot(x,y)
    # plt.show()
    # print('plot done')
    # return HTTPResponse("hi")
    if request.method == 'GET':
        return render(request, 'input.html')
    else:
        request.session['selected_eq'] = request.POST['eq']
        equities = {
            '10277':'Agilent Technologies Inc',
            '10278':'Alcoa Inc', 
            '10279':'Yahoo! Inc' ,
            '10280':'American Addiction Centers',
            '10281':'American Airlines Group Inc', 
            '10282':'Altisource Asset Management Corp',
            '10283':'Atlantic American Corp', 
            '10284':"Aaron's, Inc",
            '10285':'Applied Optoelectronics Inc',
            '10286':"AAON, Inc" 
        }
        # print(request.session['selected_eq'])
        context = {
            'eq': equities[request.session['selected_eq']],
        }
        return render(request, 'chart.html', context=context)


def show_equities(request):
    records = DailyReturns.objects.filter(equity_id=request.session['selected_eq']).order_by('date').values() 
    equities = {
            '10277':'Agilent Technologies Inc',
            '10278':'Alcoa Inc', 
            '10279':'Yahoo! Inc' ,
            '10280':'American Addiction Centers',
            '10281':'American Airlines Group Inc', 
            '10282':'Altisource Asset Management Corp',
            '10283':'Atlantic American Corp', 
            '10284':"Aaron's, Inc",
            '10285':'Applied Optoelectronics Inc',
            '10286':"AAON, Inc" 
        }
    context = {
        'records': records,
        'eq': equities[request.session['selected_eq']]
    }
    return render(request, 'display-records.html', context=context)


def list_(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'list.html',
        {'documents': documents, 'form': form}
    )