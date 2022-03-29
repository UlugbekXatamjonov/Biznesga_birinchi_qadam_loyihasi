from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Info
from .forms import InfoForm
import datetime as dt
from django.contrib import messages
import xlwt

# Create your views here.

def InfoView(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            loyiha = form.cleaned_data['loyiha_nomi']
            if not Info.objects.filter(loyiha_nomi=loyiha).exists():
                # new_data = form.save(commit=False)
                form.save()
            messages.success(request, "Ma’lumotlaringiz muvaffaqiyatli saqlandi.")
            
        else:
            messages.error(request, "Ma’lumotaringiz saqlanmadi!!! Qayta yuboring.")
    context = {'form':form}
    return render(request, 'sorovnoma.html', context)

class ResultView(ListView):
    template_name =  "result.html"
    queryset = Info.objects.all()
    context_object_name = "results"

    def result_list(request):
        results = Info.objects.all()
        context = {
            "results": results
        }
        return render(request, "result.html", context)

class WinnerView(ListView):
    template_name =  "winners.html"
    queryset = Info.objects.all()
    context_object_name = "winners"

    def winner_list(request):
        winners = Info.objects.all()
        context = {
            "winners": winners
        }
        return render(request, "winners.html", context)



def export_result(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="natijalar.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Results')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Ism','Familya', 'Tuman', 'Loyiha nomi', 'Sana']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = Info.objects.all().values_list('ism', 'familya', 'tuman', 'loyiha_nomi', 'created')
    
    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response
