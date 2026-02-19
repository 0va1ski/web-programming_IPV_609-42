from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>Home</h1>')

def about(request, company_name, company_phone):
    return HttpResponse(f"""<h1>About</h1>
    <div> Company Name: {company_name}</div>
    <div> Company Phone: {company_phone}</div>""")