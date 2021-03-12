
from django.views import generic
from django.shortcuts import render, redirect

#from django.contrib.auth import authenticate, login
#from .forms import ClientForm,UserForm
from django.template import loader
from django.db import transaction
from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView,DetailView

#from client.forms import UserForm, ClientForm
from client.models import Client, Questionnaire, AnxietyMeasure, DepressionMeasure, Case_File

class IndexView(DetailView):
    model = Client
    template_name = 'client/index.html'


class NewClient(CreateView):
    model = Client
    template_name = 'client/client_form.html'
    fields = ['name', 'nsu_id', 'password', 'designation', 'department',
              'gender', 'mobile_number', 'emergency_contact_number', 'email_id', 'monthly_income',
              'marital_status', 'religion', 'present_address', 'permanent_address', 'income_sources',
              'referred_by', 'cgpa']
'''
class CaseView(DetailView):
    model = Case_File
    template_name = 'client/case_view.html'
'''
def case_view(request, client_id):
    try:
        c = Client.objects.get(pk=client_id)
        case_file = Case_File(client=c, status='Open', category='')
    except Case_File.DoesNotExist:
        raise Http404("Case File hasn't been created yet.")
    return render(request, 'client/case_view.html', {'case_file': case_file})


'''
class ClientFormView(View):
    template_name = 'client/client_form'

    def get(self, request):
        user_form = UserForm(instance=request.user)
        client_form = ClientForm(instance=request.user.client)
        return render(request, self.template_name, {'user_form': user_form,
                                                    'client_form': client_form})

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        client_form = ClientForm(request.POST, instance=request.user.client)

        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save(commit=False)
            client = client_form.save(commit=False)

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            date_of_birth = client_form.cleaned_data['date_of_birth']

            user.set_password(password)

            user.save()
            client.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('client:index')

        return render(request, self.template_name, {'user_form': user_form,
                                                    'client_form': client_form})


class NewQuestionnaire(CreateView):
    template_name = 'client/book_appointment.html'
    model = Questionnaire
    fields = ['present_concern', 'total_duration_of_problems', 'duration_of_severity',
              'have_you_previously_recieved_any_type_of_mental_health_services']



def client(request):
    message = "Hello"
    return HttpResponse(message)

   #Attribute error
class IndexView(generic.DetailView):
        model = Client
        template_name = 'client/index.html'

'''

class NewQuestionnaire(CreateView):
    model = Questionnaire
    template_name = 'client/book_appointment.html'

    fields = ['present_concern', 'total_duration_of_problems', 'duration_of_severity',
              'have_you_previously_recieved_any_type_of_mental_health_services',
              'are_you_currently_taking_any_prescribed_psychiatric_medication',
              'have_you_ever_taken_psychiatric_medication', 'are_you_currently_experiencing_anxiety',
              'are_you_currently_experiencing_overwhelming_sadness_grief_or_depression',
              'are_you_having_frequent_suicidal_ideation_recently', 'have_you_taken_any_attempt_to_commit_suicide',
              'date_of_last_attempt']


class NewAnxietyMeasure(CreateView):
    template_name = 'client/anxiety_measure.html'
    model = AnxietyMeasure
    fields = ['i_breath_fast', 'i_feel_suffocated', 'i_feel_burden_on_my_chest', 'i_feel_giddy_in_my_chest',
              'i_feel_chest_pain', 'my_body_shivers', 'my_hand_and_leg_shakes', 'i_cant_sense_my_hand_or_leg',
              'my_hand_or_leg_burns','i_feel_dizziness', 'my_head_spins', 'i_have_headache', 'my_head_heats_up',
              'my_throat_gets_dry_and_i_feel_thirsty', 'i_feel_like_getting_sick', 'i_am_worried_about_my_health',
              'i_feel_weak', 'i_have_digesting_issues', 'i_feel_trouble_in_my_stomach', 'i_feel_like_vomiting',
              'i_sweat_a_lot_but_not_from_heat', 'i_cant_take_rest',
              'i_find_it_difficult_to_converse_in_a_social_environment', 'i_get_worried_about_one_matter_over_and_over',
              'i_feel_like_something_bad_will_happen', 'i_feel_stressed', 'i_get_startled', 'i_feel_agitated',
              'i_am_afraid_of_losing_self_control', 'i_get_so_nervous_that_i_feel_like_everything_is_getting_messier',
              'i_cannot_have_patience', 'i_am_suffering_from_indecisiveness', 'i_lack_confidence',
              'i_cant_concentrate_on_one_matter', 'i_feel_like_dying_right_now','i_am_afraid_of_dying'
              ]

class NewDepressionMeasure(CreateView):
    template_name = 'client/depression_measure.html'
    model = DepressionMeasure
    fields = ['i_feel_unrest', 'nowadays_i_am_gloomy', 'i_feel_my_future_is_dark',
              'in_future_my_condition_will_get_worse', 'i_feel_everything_has_fallen_apart',
              'i_feel_like_my_life_is_very_difficult_now', 'i_feel_like_i_am_totally_a_disappointment_as_a_human',
              'i_cant_find_happiness_in_anything', 'i_feel_inferior', 'my_confidence_has_fallen_down',
              'i_feel_like_people_pity_me', 'life_is_meaningless', 'i_often_feel_like_crying',
              'i_often_feel_irritated', 'i_dont_find_interest_in_anything', 'nowadays_i_cant_think_and_take_decisions',
              'currently_i_cant_give_my_concentration_on_anything', 'i_feel_trouble_remembering',
              'i_feel_weak_and_get_tired_easily', 'i_sleep_less_nowadays', 'i_sleep_more_nowadays',
              'my_temper_gets_irritable', 'my_appetite_has_decreased', 'my_appetite_has_increased',
              'i_lost_weight_not_by_diet_or_exercise', 'i_think_my_work_pace_has_decreased',
              'i_cant_laugh_at_funny_incidents', 'i_lost_lost_interest_in_sexual_matters',
              'i_cant_participate_in_social_activities_anymore_like_before',
              'i_cant_do_my_educational_or_occupational_work_like_before']

'''
class Client:
    def __init__(self):
        return ClientFormView

class Client:
    def __init__(self):
        return IndexView

class Client:
    def __init__(self):
        return  NewQuestionnaire
'''

