from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
registro_cuota = [
    {
        'monto': '64541',
        'tasa': '12',
        'plazo': '12',
        'cuota': '15',
        'total': '2000'
    },
]

def cuota(request):
    if request.method == 'POST':
        #Aquí vendra la información del Usuario
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        t = tasa / 100 / 12
        p = plazo * 12

        c = (monto * t) / (1 - (1 + t) ** - p)

        total = c * p

        registro_cuota.append({
            'monto': monto,
            'tasa': tasa,
            'plazo': plazo,
            'cuota': round(c,2),
            'total': round(total,2)
        })
        #return HttpResponse('El participante ha sido registrado')
        ctx = {
            'registro_cuota': registro_cuota
        }
        return render(request, 'registro/cuota.html', ctx)
    else:
        #El metodo GET
        ctx = {
            'registro_cuota': registro_cuota
        }
        return render(request, 'registro/cuota.html', ctx)
