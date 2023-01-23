from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def main(request):
    html = '<html>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'Django Test Page\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    return HttpResponse(html)




