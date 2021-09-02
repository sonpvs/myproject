from django.shortcuts import render
from django.http import HttpResponse
from .forms import Post_Form, Baby_Form, Khaosat_Form
from .models import Baby, Khaosat
from .utils import get_simple_plot
import json
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "news/index.html")

# Create your views here.
def chart_01(request):
    return render(request, "news/chart01.html")

# Create your views here.
def chart_select_view( request): 
    graph = None 
    error_message=None 
    df = None 
    khaosat_df = pd.DataFrame(Khaosat.objects.all().values()) 

    if khaosat_df.shape[0] > 0: 
        if request.method == 'POST': 
            chart_type = request.POST.get('style') 
            #diaban = request.POST['diaban'] 
            nut = request.POST['nut'] 
            
            #print("Dia ban :", diaban, ' : Nút bấm :', nut)            
            #date_to = request.POST['date_to'] 
            #print(chart_type) 
            if chart_type != "": 
                #df1 = khaosat_df['gioitinh'].describe()
                df1 = khaosat_df.groupby('hocvan')
                print(df1.describe()['tuoi'])
                
                # function to get a graph 
                graph = get_simple_plot(chart_type, x=khaosat_df['gioitinh'], y=khaosat_df['hocvan'], data=khaosat_df) 
            else: 
                error_message = 'Please select a chart type to continue' 
        else: 
            error_message = "No records in the database"

    context = {
        'graph' : graph,
        'error_message': error_message, 
        }
    if nut =='1':
        return render(request, 'news/chrt.html', context)
    else:
        return chart(request)    





# Create your views here.
def view_describe(request): 
    df = None 
    khaosat_df = pd.DataFrame(Khaosat.objects.all().values()) 

    if khaosat_df.shape[0] > 0: 
        if request.method == 'GET': 
            df1 = khaosat_df.groupby('hocvan')
            data =df1['gioitinh'].describe()
            #print(data)
            title = "Mô tả dữ liệu giữa Nhóm học vấn và giới tính"
    context = {
        'data' : data,
        'title' : title,
        }
    return render(request, 'news/view_describe.html', context)





def chart(request):
    data_arr = [['tuoi', 'hocvan']]
    for item in Khaosat.objects.all():
        data_arr.append([item.tuoi, item.hocvan])
        #print(data_arr)
    return render(request,'news/chart.html',{'item':json.dumps(data_arr)})
    #json.dumps(data_arr)


def add_post(request):
    a = Post_Form()
    return render(request, "news/add_news.html", {'f': a})

def save_news(request):
    if request.method == "POST":
        g = Post_Form(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Luu OK")
        else:
            return HttpResponse("Loi du lieu")
    else:
        return HttpResponse("Khong phai POST request")


def add_baby(request):
    f = Baby_Form()
    return render(request, "news/add_Baby.html", {'form': f})


def save_baby(request):
    if request.method == "POST":
        g = Baby_Form(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Luu Baby OK")
        else:
            return HttpResponse("Loi du lieu")
    else:
        return HttpResponse("Khong phai POST request")

def add_khaosat(request):
    a = Khaosat_Form()
    return render(request, "news/add_khaosat.html", {'f': a})


def save_khaosat(request):
    if request.method == "POST":
        g = Khaosat_Form(request.POST)
        #print(g)
        if g.is_valid():
            g.save()
            return view_khaosat(request) #render(request, "news/view_khaosat.html")
        else:
            return HttpResponse("Loi du lieu")
    else:
        return HttpResponse("Khong phai POST request")


def view_khaosat(request):
    ks = Khaosat.objects.all().values() #values_list
    df = pd.DataFrame(ks)
    df = df.reset_index().to_json(orient ='records')
    #df1 = df.describe()
    #print(df['hocvan'].describe())
    data = []
    data = json.loads(df)
    context ={
        'khaosat': data,
        #'describe': df1.to_html(),
    }
    return render(request, "news/view_khaosat.html", context)


# Create your views here.
def chuanhoa(request):
    return render(request, "news/chuanhoa.html")
