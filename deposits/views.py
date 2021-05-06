from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy
from deposits.models import  Deposit
from deposit import Deposit as Interest




# Create your views here.
def index(request):

    depositAll = Deposit.objects.all()

    context = {"object_list": depositAll}

    return render(template_name="index.html", request=request, context=context)

def add_deposit(request):

    if request.method == "POST":

        deposit =  request.POST["deposit"]
        term = request.POST["term"]
        rate = request.POST["rate"]
        result = Interest(deposit=deposit, term=term, rate=rate)
        interest = result.interest()

        deposit = Deposit(
            deposit= deposit,
            term = term,
            rate = rate,
            interest = interest,
        )
        print(Interest().interest())
        deposit.save()

        depositAll = Deposit.objects.all()

        context = {"object_list": depositAll}

        return render(template_name="index.html", request=request, context=context)



    return render(template_name="add_deposit.html", request=request, )

def chekDeposit(request, id):

    deposit = Deposit.objects.get(pk=id)
    content = {"deposit": deposit.deposit,
        "term": deposit.term,
        "rate": deposit.rate,
        "interest": deposit.interest,}

    return render(template_name="deposit_chek.html", request=request, context=content)
