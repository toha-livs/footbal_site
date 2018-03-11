from django.db.models import QuerySet
from django.shortcuts import render, redirect
from .models import AllAttr, Coef, Bookmaker


def scan(request):
    bookma = AllAttr.objects.all()
    context = {'all': bookma}
    print(context)
    return render(request, 'first.html', context)


def cof(request, user_id):
    print(user_id)
    pere = 0
    match = AllAttr.objects.filter(id=user_id)
    print(match)
    coefe = Coef.objects.filter(match_id=user_id).select_related('bookmaker')
    print(coefe)
    context = {'cof': coefe, 'match': match, 'pere': pere}
    return render(request, 'cof.html', context)




# {{match.0.team_1}} {{match.0.team_2}}
# {%for row in cof%} {{row.bookmaker.name}} {{row.one}} {{row.x}} {{row.two}} {%endfor%}