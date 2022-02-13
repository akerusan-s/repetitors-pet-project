from django.shortcuts import render, redirect
from .models import *

# con = sqlite3.connect('repetitors.db')
# cur = con.cursor()
# teachers = cur.execute("""SELECT * FROM who""").fetchall()
# rating = cur.execute("""SELECT * FROM rating""").fetchall()
# subject = cur.execute("""SELECT * FROM subject""").fetchall()
# a = teachers[:]
# for i in range(len(a)):
#     a[i] = list(a[i])
# for i in range(len(a)):
#     a[i][0] = subject[a[i][0] - 1][1]
#     a[i][1] = rating[a[i][1] - 1][1]

def name(request):
    subs = Subject.objects.all()
    if request.method == 'POST':
        subject = request.POST["subject_selection"]
        price = request.POST["price_selection"]
        form = request.POST["form_selection"]
        rate = request.POST["rate_selection"]
        year = request.POST["year_selection"]

        teachers = Teacher.objects.filter(subject_id=subject)
        if price != "0":
            if price == "1":
                teachers = teachers.filter(salary__lte=1000)
            if price == "2":
                teachers = teachers.filter(salary__lte=2000)
            if price == "3":
                teachers = teachers.filter(salary__lte=3000)
            if price == "4":
                teachers = teachers.filter(salary__gte=3000)

        teachers = teachers.filter(place_id=int(form))

        if rate != "0":
            if rate == "1":
                teachers = teachers.filter(rate__lte=1)
            if rate == "2":
                teachers = teachers.filter(rate__lte=2).filter(rate__gte=1)
            if rate == "3":
                teachers = teachers.filter(rate__lte=3).filter(rate__gte=2)
            if rate == "4":
                teachers = teachers.filter(rate__lte=4).filter(rate__gte=3)
            if rate == "5":
                teachers = teachers.filter(rate__lte=5).filter(rate__gte=4)
        if year != "0":
            if year == "1":
                teachers = teachers.filter(year__lte=3)
            if year == "2":
                teachers = teachers.filter(year__gte=3).filter(year__lte=5)
            if year == "3":
                teachers = teachers.filter(year__gte=5)

        return render(request, 'pages/result.html', {'teachers': teachers})

    return render(request, 'pages/page.html', {"subs": subs})


def main(request):
    return render(request, 'pages/mainpage.html')


def categories(request, data):
    print(data)
    return render(request, 'pages/repetitors.html')


'''{'leaf': a[:100]}'''
