from django.shortcuts import render


def homepage(request):
    data = {"header":"Homepage", "message":"Welcome to site!"}
    return render(request, "homepage.html", context=data)

def about(request):
    header = "About us"
    staff = ['John Nichols', 'Jhon Rogers', 'Timothy Smith']
    directors = {"name":"David Lee", "img":'/director.jpg'}
    address = ['20 W 34th St.', 'New York', 'NY 10001', 'USA']
    data = {"header":header, "staff":staff, "directors":directors, "address":address}
    return render(request, "about.html", context=data)