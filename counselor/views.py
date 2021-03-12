from django.shortcuts import render
from .models import Counselor,TimeSlot
from django.template import loader
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.views.generic import DetailView,CreateView,DeleteView


def index(request):
    all_counselors = Counselor.objects.all()
    template = loader.get_template('counselor/counselors.html')
    context = {
        'all_counselors': all_counselors,
    }
    return HttpResponse(template.render(context,request))

class ProfileView(DetailView):
    model = Counselor
    template_name = 'counselor/profile.html'

class CreateTimeSlot(CreateView):
    model = TimeSlot
    template_name = 'counselor/timeslot_form.html'
    fields = ['date', 'slot', 'availability']


def slotlist(request,counselor_id):
    try:
        counselor = Counselor.objects.get(pk=counselor_id)
    except ObjectDoesNotExist:
        raise Http404("No slot available")

    return render(request,'counselor/timeslot_manage',{'counselor':counselor})
