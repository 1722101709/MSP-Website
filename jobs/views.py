from django.shortcuts import render, redirect
from .models import Database, Company, Eligibilities, Internships, Contest, ContestDatabase, User
import time
import datetime

# Create your views here.

# Home page
def home(request):
    time.sleep(0.3)
    return render(request, 'home.html')


# Job description page for job with id = pk
def company(request, pk):
    data = Database.objects.filter(stringId=pk).order_by('no')
    flag = True if len(data) > 0 else False
    image = Company.objects.filter(stringId=pk)[0].image
    company = Company.objects.filter(stringId=pk)[0].company
    link = Company.objects.filter(stringId=pk)[0].link
    time.sleep(0.3)
    return render(request, 'company.html',
                  {'data': data, 'company': company, 'flag': flag, 'image': image, 'link': link})


# All job notifications
def jobNotifications(request):
    data = Company.objects.all().order_by('-postTime')
    flag = True
    query = ''
    if request.method == 'POST':
        query = request.POST['query'].lower()
        data = list(Company.objects.filter(company=query).order_by('-postTime'))
        for item in Company.objects.filter(info__icontains=query):
            if item not in data:
                data.append(item)
        if not data:
            flag = False
        print(data)
    Data = {'data': data, 'flag': flag, 'query': query}
    time.sleep(0.3)
    return render(request, 'job_notifications.html', Data)


# All internships
def internships(request):
    data = Internships.objects.all().order_by('-postTime')
    flag = True
    query = ''
    if request.method == 'POST':
        query = request.POST['query'].lower()
        data = list(Internships.objects.filter(company=query).order_by('-postTime'))
        for item in Internships.objects.filter(info__icontains=query):
            if item not in data:
                data.append(item)
        if not data:
            flag = False
    Data = {'data': data, 'flag': flag, 'query': query}
    time.sleep(0.3)
    return render(request, 'internships.html', Data)


# details of internship with id = pk
def internship(request, pk):
    data = Database.objects.filter(stringId=pk.lower()).order_by('no')
    flag = True if len(data) > 0 else False
    image = Internships.objects.filter(stringId=pk.lower())[0].image
    company = Internships.objects.filter(stringId=pk.lower())[0].company
    link = Internships.objects.filter(stringId=pk)[0].link
    time.sleep(0.3)
    return render(request, 'company.html',
                  {'data': data, 'company': company, 'flag': flag, 'image': image, 'link': link})


# Eligibility page for job
def eligibility(request, pk):
    data = Eligibilities.objects.filter(stringId=pk).order_by('no')
    link = Company.objects.filter(stringId=pk)
    if len(link) == 0:
        link = Internships.object.filter(stringId=pk)[0].link
        company = Internships.object.filter(stringId=pk)[0].company
    else:
        link = Company.objects.filter(stringId=pk)[0].link
        company = Company.objects.filter(stringId=pk)[0].company
    return render(request, 'eligibility.html', {'data': data, 'link': link, 'company': company})


# Interview topics page
def interviewTopics(request):
    time.sleep(0.3)
    return render(request, 'InterviewTopics.html')


# interview questions of subject pk
def interview(request, pk):
    time.sleep(0.3)
    return render(request, pk + 'Interview' + '.html')


# authentication page
def contests(request):
    time.sleep(0.3)
    return render(request, 'authentication.html')


# user registration
def contestsRegistration(request):
    old = False
    user_already_exist = False
    register_success = False
    isreg = True
    if request.method == 'POST':
        old = True
        name = request.POST['reg-name']
        year = request.POST['reg-year']
        email = request.POST['reg-mail']
        password = request.POST['reg-pass']
        if User.objects.filter(email=email).exists():
            user_already_exist = True
        else:
            User.objects.create(username=name, year=year, email=email, password=password)
            register_success = True
            isreg = False
        print("user_already_exist =", user_already_exist)
    time.sleep(0.3)
    return render(request, 'authentication.html',
                  {'old': old, 'user_already_exist': user_already_exist, 'register_success': register_success,
                   'isreg': isreg})


# user login
def contestsLogin(request):
    old = False
    user_not_exist = False
    wrong_details = False
    if request.method == 'POST':
        old = True
        email = request.POST['log-mail']
        password = request.POST['log-pass']
        if User.objects.filter(email=email).exists():
            if User.objects.filter(email=email, password=password).exists():
                print("Login Success")
                time.sleep(0.3)
                return redirect('/contests/home', kwargs = {'authorized' : True})
            else:
                wrong_details = True
                print("Wrong Details")
        else:
            user_not_exist = True
            print("User Doesn't exist")
        time.sleep(0.3)
    return render(request, 'authentication.html',
                  {'old': old, 'user_not_exist': user_not_exist, 'wrong_details': wrong_details})


# user forgot password
def forgotPassword(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['reg-mail']
        password = request.POST['reg-pass']
        if User.objects.filter(email=email).exists():
            User.objects.filter(email=email).update(password=password)
            print("updated")
            time.sleep(0.3)
            return render(request, 'authentication.html', {'old': True, 'register_success': True})
        else:
            time.sleep(0.3)
            return render(request, 'authentication.html', {'old': True, 'user_not_exist': True})
    return render(request, 'forgotPassword.html')


# contests page (play with coding + Brain Boost)
def contestsHome(request, **kwargs):
    if 'authorized' in kwargs and kwargs['authorized'] == True:
        PWCdata = Contest.objects.values('name', 'startDateTime', 'EndDateTime', 'link')
        for i in range(len(PWCdata)):
            now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)
            active = PWCdata[i]['EndDateTime'] > now
            PWCdata[i].update({'active': active})
        return render(request, 'contests.html', {'PWCdata': PWCdata})
    else:
        return redirect('/contests/register')


# solutions for contests
def solutions(request):
    contestData = Contest.objects.all().order_by('-startDateTime')
    data = []
    Data = ContestDatabase.objects.all().order_by('no')
    for i in range(len(contestData)):
        heading = contestData[i].name
        solutions = []
        for row in Data:
            if row.stringId == contestData[i].stringId:
                solutions.append(row)
        data.append({'heading': heading, 'solutions': solutions})
    time.sleep(0.3)
    return render(request, 'solutions.html', {'data': data})


# about us page
def about_us(request):
    time.sleep(0.3)
    return render(request, 'about_us.html')

# Challenge Response function
def challenge_response(n):
    s = str(n)
    ans = s[-1] + s[0] + str(int(s[-2]) + int(s[1])) + str(int(s[-3]) + int(s[2]))
    return ans


#admin page
def admin(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        answer = request.POST.get('answer')
        res = challenge_response(query)
        print(query, answer, res, res == answer)
        if answer == res:
            return redirect('/1729-ADMIN-1729-ADMIN-1729-ADMIN-1729')
    return render(request, 'admin_authentication.html')