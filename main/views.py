import datetime
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from well.models import *
from plan_fact.models import Plan


url = 'http://127.0.0.1:8000'
test = 'test'

def index(request):
    try:
        if request.POST['spec'] == 'master':
            masters = Master.objects.filter(username=request.POST['username'], password=request.POST['password'])
            if len(masters) == 0:
                return render(request, 'index.html')
            else:
                master = masters[0]
                response = redirect(url + '/master/' + str(master.username) + '/report')
                # response.set_cookie('logged', str(int(time.time())))
                response.set_cookie('logged', 'True')
                return response
                # return master(request, master)

    except Exception as error:
        print(error)
        return render(request, 'index.html')


def master(request, username):
    operationcodes = OperationCode.objects.all()
    groups = []
    for i in operationcodes:
        groups.append(i.group)
    operations = []
    for i in operationcodes:
        operations.append(i.operation)

    try:
        if request.COOKIES['logged'] == 'True':
            master = Master.objects.get(username=username)
            well = Well.objects.get(master=username)
            dispathcer = Dispatcher.objects.get(complex=well.complex)
            return render(request, 'master.html', {'master': master, 'well': well, 'dispatcher': dispathcer, 'groups': groups, 'operations': operations})
    except Exception as error:
        print(error)
        return redirect('http://127.0.0.1:8000')
    return redirect('http://127.0.0.1:8000')


def makereport(request, master_username):
    master = Master.objects.get(username=master_username)
    well = Well.objects.get(name=master.current_well)
    report = Report()
    report.well = request.POST['well']
    report.master = request.POST['master']
    report.fact = int(request.POST['fact'])
    well.fact = int(request.POST['fact'])
    report.last_column = int(request.POST['last_column'])
    report.next_column = int(request.POST['next_column'])
    report.last_drilled = int(request.POST['last_drilled'])
    report.to_drill = int(request.POST['to_drill'])
    report.drilled = int(request.POST['drilled'])
    report.drilled24 = int(request.POST['drilled24'])
    report.diameter = int(request.POST['diameter'])
    report.days_after_uncountable_case = int(request.POST['days_after_uncountable_case'])
    report.days_without_incident = int(request.POST['days_without_incident'])
    report.number = int(request.POST['number'])
    report.days = int(request.POST['days'])
    report.meeting = request.POST['meeting']
    report.date = datetime.datetime.date(datetime.datetime.now())
    report.save()
    well.fact = int(request.POST['drilled'])
    well.save()
    return redirect('http://127.0.0.1:8000/master/' + str(master.username) + '/report')


def addoperation(request, master_username):
    master = Master.objects.get(username=master_username)
    operations = Operation.objects.filter(well=master.current_well)
    number = len(operations) + 1
    operation = Operation()
    operation.well = master.current_well
    operation.number = number
    operation.begin_time = request.POST['from_time']
    operation.end_time = request.POST['to_time']
    operation.group = request.POST['group']
    operation.notes = request.POST['note']
    operation.description = request.POST['description']
    code = OperationCode.objects.get(group=request.POST['group'], operation=request.POST['operation'])
    operation.code = request.POST['group'][0] + request.POST['operation'][0] + code.code
    operation.type = code.type
    operation.operation = request.POST['operation']
    operation.save()
    return redirect('http://127.0.0.1:8000/master/' + str(master.username) + '/report')


def reports(request, master_username):
    well = Well.objects.get(master=master_username)
    reports = Report.objects.filter(well=well.name)
    master = Master.objects.get(username=master_username)
    return render(request, 'reports.html', {'reports': reports, 'master': master})


def viewreport(request, number):
    return HttpResponse('test')


def balance(request, master_username):
    master = Master.objects.get(username=master_username)
    operations = Operation.objects.filter(date='2021-07-15', well=master.current_well)
    return render(request, 'balance.html', {'master': master, 'operations': operations})


def consumptions(request, master_username):
    master = Master.objects.get(username=master_username)
    consumptions = Consumptions.objects.filter(well=master.current_well)
    return render(request, 'consumptions.html', {'master': master, 'consumptions': consumptions})


def addconsumptions(request, master_username):
    master = Master.objects.get(username=master_username)
    consumption = Consumptions()
    consumption.well = master.current_well
    consumption.type = request.POST['type']
    consumption.type_m = request.POST['type_m']
    consumption.name = request.POST['name']
    consumption.date = datetime.date.today()
    consumption.count = request.POST['count']
    consumption.save()
    return redirect('http://127.0.0.1:8000/master/' + str(master.username) + '/addconsumptions')


def analytics(request, master_username):
    master = Master.objects.get(username=master_username)
    well = Well.objects.get(master=master_username)
    operations = Operation.objects.filter(well=well.name, type='Н')
    reports = Report.objects.filter(well=well.name)
    last_reports = []
    if len(reports) < 30:
        last_reports = reports
    else:
        for i in range(len(last_reports)):
            last_reports.append(reports[i])

    drilled = 0
    for i in last_reports:
        drilled = drilled + i.fact

    date = datetime.datetime.date(datetime.datetime.now())
    print(date)
    print(well.name)
    plan = Plan.objects.get(well=well.name, date=str('2021-07-21'))
    print(test)
    print(plan)
    print(test)
    one_day_speed = drilled / len(last_reports)
    prognosis = well.plan / one_day_speed
    plan_fact = {
        'by_percent': (plan.fact/plan.plan) * 100,
        'commerce_speed': drilled,
        'mechanic_speed': 0,
        'plan': plan.plan,
        'fact': well.fact,
        'prognosis': prognosis,
        'difference': plan.fact - plan.plan
    }
    return render(request, 'analytics.html', {'master': master, 'well': well, 'operations': operations, 'plan_fact': plan_fact})


def applications(request, master_username):
    master = Master.objects.get(username=master_username)
    return render(request, 'applications.html', {'master': master})
