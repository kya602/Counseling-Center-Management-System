from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from counselor.models import Counselor,TimeSlot
from django.db.models.signals import post_save
from django.dispatch import receiver

'''def has_related_object(self):
       has_client = False
       try:
           has_client = (self.client is not None)
       except Client.DoesNotExist:
           pass
       return has_client and (self.nsu_id is not None)'''


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    email_id = models.CharField(max_length=50)
    password = models.CharField(max_length=10, null=True)

    MALE = 0
    FEMALE = 1
    MARRIED = 0
    UNMARRIED = 1

    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    MARITAL_STATUS = ((MARRIED, 'Married'), (UNMARRIED, 'Unmarried'))
    DESG = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
    )

    nsu_id = models.CharField(max_length=12)
    designation = models.CharField(max_length=10, choices=DESG)
    department = models.CharField(max_length=50, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    emergency_contact_number = models.CharField(max_length=15)

    monthly_income = models.IntegerField(null=True, blank=True)
    marital_status = models.IntegerField(choices=MARITAL_STATUS, blank=True, null=True)
    religion = models.CharField(max_length=20, blank=True)
    present_address = models.CharField(max_length=300, default='0', blank=True)
    permanent_address = models.CharField(max_length=300, default='0', blank=True)
    income_sources = models.CharField(max_length=1000, blank=True)
    referred_by = models.CharField(max_length=250, blank=True)
    cgpa = models.FloatField(default=0, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('client:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nsu_id


@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)
        instance.client.save()
    else:
        return


@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    instance.client.save()



class Questionnaire(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, parent_link=True)
    present_concern = models.CharField(max_length=1000)
    total_duration_of_problems = models.DurationField()
    duration_of_severity = models.DurationField()

    YES = 1
    NO = 0
    CHOICES = ((YES, 'Yes'), (NO, 'No'))

    have_you_previously_recieved_any_type_of_mental_health_services = models.NullBooleanField(choices=CHOICES)
    are_you_currently_taking_any_prescribed_psychiatric_medication = models.NullBooleanField(choices=CHOICES)
    have_you_ever_taken_psychiatric_medication = models.NullBooleanField(choices=CHOICES)
    are_you_currently_experiencing_anxiety = models.NullBooleanField(choices=CHOICES)
    are_you_currently_experiencing_overwhelming_sadness_grief_or_depression = models.NullBooleanField(choices=CHOICES)
    are_you_having_frequent_suicidal_ideation_recently = models.NullBooleanField(choices=CHOICES)
    have_you_taken_any_attempt_to_commit_suicide = models.NullBooleanField(choices=CHOICES)

    date_of_last_attempt = models.DateField(blank=True,null=True)



    def get_absolute_url(self):
        return reverse('client:anxiety')
'''
    def timeslot_choices():
        timeslots = TimeSlot.objects.all()
        choice = []
        for timeslot in timeslots:
            if timeslot.availability is True:
                choice = timeslot
        return choice

    TIME = timeslot_choices()
    choose_timeslot = models.OneToOneField(TimeSlot, choices=TIME, null=True)
'''

class AnxietyMeasure(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, parent_link=True)

    HAPPENS_NEVER = 0
    HAPPENS_MODERATELY = 1
    NEUTRAL = 2
    HAPPENS_PLENTY = 3
    HAPPENS_EXCESSIVELY = 4

    CHOICES = ((HAPPENS_NEVER, 'Happens Never'),
               (HAPPENS_MODERATELY, 'Happens Moderately '),
               (NEUTRAL, 'Neutral'),
               (HAPPENS_PLENTY, 'Happens Plenty '),
               (HAPPENS_EXCESSIVELY, 'Happens Excessively'),

               )
    i_breath_fast = models.IntegerField(choices=CHOICES, default=0)
    i_feel_suffocated = models.IntegerField(choices=CHOICES, default=0)
    i_feel_burden_on_my_chest = models.IntegerField(choices=CHOICES, default=0)
    i_feel_giddy_in_my_chest = models.IntegerField(choices=CHOICES, default=0)
    i_feel_chest_pain = models.IntegerField(choices=CHOICES, default=0)
    my_body_shivers = models.IntegerField(choices=CHOICES, default=0)
    my_hand_and_leg_shakes = models.IntegerField(choices=CHOICES, default=0)
    i_cant_sense_my_hand_or_leg = models.IntegerField(choices=CHOICES, default=0)
    my_hand_or_leg_burns = models.IntegerField(choices=CHOICES, default=0)
    i_feel_dizziness = models.IntegerField(choices=CHOICES, default=0)
    my_head_spins = models.IntegerField(choices=CHOICES, default=0)
    i_have_headache = models.IntegerField(choices=CHOICES, default=0)
    my_head_heats_up = models.IntegerField(choices=CHOICES, default=0)
    my_throat_gets_dry_and_i_feel_thirsty = models.IntegerField(choices=CHOICES, default=0)
    i_feel_like_getting_sick = models.IntegerField(choices=CHOICES, default=0)
    i_am_worried_about_my_health = models.IntegerField(choices=CHOICES, default=0)
    i_feel_weak = models.IntegerField(choices=CHOICES, default=0)
    i_have_digesting_issues = models.IntegerField(choices=CHOICES, default=0)
    i_feel_trouble_in_my_stomach = models.IntegerField(choices=CHOICES, default=0)
    i_feel_like_vomiting = models.IntegerField(choices=CHOICES, default=0)
    i_sweat_a_lot_but_not_from_heat = models.IntegerField(choices=CHOICES, default=0)
    i_cant_take_rest = models.IntegerField(choices=CHOICES, default=0)
    i_find_it_difficult_to_converse_in_a_social_environment = models.IntegerField(choices=CHOICES, default=0)
    i_get_worried_about_one_matter_over_and_over = models.IntegerField(choices=CHOICES, default=0)
    i_feel_like_something_bad_will_happen = models.IntegerField(choices=CHOICES, default=0)
    i_feel_stressed = models.IntegerField(choices=CHOICES, default=0)
    i_get_startled = models.IntegerField(choices=CHOICES, default=0)
    i_feel_agitated = models.IntegerField(choices=CHOICES, default=0)
    i_am_afraid_of_losing_self_control = models.IntegerField(choices=CHOICES, default=0)
    i_get_so_nervous_that_i_feel_like_everything_is_getting_messier = models.IntegerField(choices=CHOICES, default=0)
    i_cannot_have_patience = models.IntegerField(choices=CHOICES, default=0)
    i_am_suffering_from_indecisiveness = models.IntegerField(choices=CHOICES, default=0)
    i_lack_confidence = models.IntegerField(choices=CHOICES, default=0)
    i_cant_concentrate_on_one_matter = models.IntegerField(choices=CHOICES, default=0)
    i_feel_like_dying_right_now = models.IntegerField(choices=CHOICES, default=0)
    i_am_afraid_of_dying = models.IntegerField(choices=CHOICES, default=0)

    @property
    def anxiety_level(self):

        return self.i_breath_fast+self.i_feel_suffocated+self.i_feel_burden_on_my_chest+self.i_feel_giddy_in_my_chest\
        +self.i_feel_chest_pain+self.my_body_shivers+self.my_hand_and_leg_shakes+self.i_cant_sense_my_hand_or_leg\
        +self.my_hand_or_leg_burns+self.i_feel_dizziness+self.my_head_spins+self.i_have_headache\
        +self.my_head_heats_up+self.my_throat_gets_dry_and_i_feel_thirsty+self.i_feel_like_getting_sick\
        +self.i_am_worried_about_my_health+self.i_feel_weak+self.i_have_digesting_issues+self.i_feel_trouble_in_my_stomach\
        +self.i_feel_like_vomiting+self.i_sweat_a_lot_but_not_from_heat+self.i_cant_take_rest\
        +self.i_find_it_difficult_to_converse_in_a_social_environment+self.i_get_worried_about_one_matter_over_and_over\
        +self.i_feel_like_something_bad_will_happen+self.i_feel_stressed+self.i_feel_agitated+self.i_get_startled\
        +self.i_am_afraid_of_losing_self_control+self.i_get_so_nervous_that_i_feel_like_everything_is_getting_messier\
        +self.i_cannot_have_patience+self.i_am_suffering_from_indecisiveness+self.i_lack_confidence\
        +self.i_cant_concentrate_on_one_matter+self.i_feel_like_dying_right_now+self.i_am_afraid_of_dying

    def get_absolute_url(self):
        return reverse('client:depression')


class DepressionMeasure(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    ABSOLUTELY_NOT_APPLICABLE = 1
    NOT_APPLICABLE = 2
    NEUTRAL = 3
    MILDLY_APPLICABLE = 4
    FULLY_APPLICABLE = 5

    CHOICES = ((ABSOLUTELY_NOT_APPLICABLE, 'Absolutely Not Applicable'),
               (NOT_APPLICABLE, 'Not Applicable'),
               (NEUTRAL, 'Neutral'),
               (MILDLY_APPLICABLE, 'Mildly Applicable'),
               (FULLY_APPLICABLE, 'Fully Applicable'),

               )

    i_feel_unrest = models.IntegerField(choices=CHOICES, default=0)
    nowadays_i_am_gloomy = models.IntegerField(choices=CHOICES, default=0)
    i_feel_my_future_is_dark = models.IntegerField(choices=CHOICES, default=0)
    in_future_my_condition_will_get_worse = models.IntegerField(choices=CHOICES, default=0)
    i_feel_everything_has_fallen_apart = models.IntegerField(choices=CHOICES, default=0)
    i_feel_like_my_life_is_very_difficult_now = models.IntegerField(choices=CHOICES, default=0)
    i_feel_like_i_am_totally_a_disappointment_as_a_human = models.IntegerField(choices=CHOICES, default=0)
    i_cant_find_happiness_in_anything = models.IntegerField(choices=CHOICES, default=0)
    i_feel_inferior = models.IntegerField(choices=CHOICES, default=0)
    my_confidence_has_fallen_down = models.IntegerField(choices=CHOICES, default=0)
    i_feel_like_people_pity_me  = models.IntegerField(choices=CHOICES, default=0)
    life_is_meaningless = models.IntegerField(choices=CHOICES, default=0)
    i_often_feel_like_crying = models.IntegerField(choices=CHOICES, default=0)
    i_often_feel_irritated = models.IntegerField(choices=CHOICES, default=0)
    i_dont_find_interest_in_anything = models.IntegerField(choices=CHOICES, default=0)
    nowadays_i_cant_think_and_take_decisions = models.IntegerField(choices=CHOICES, default=0)
    currently_i_cant_give_my_concentration_on_anything = models.IntegerField(choices=CHOICES, default=0)
    i_feel_trouble_remembering  = models.IntegerField(choices=CHOICES, default=0)
    i_feel_weak_and_get_tired_easily  = models.IntegerField(choices=CHOICES, default=0)
    i_sleep_less_nowadays = models.IntegerField(choices=CHOICES, default=0)
    i_sleep_more_nowadays = models.IntegerField(choices=CHOICES, default=0)
    my_temper_gets_irritable = models.IntegerField(choices=CHOICES, default=0)
    my_appetite_has_decreased = models.IntegerField(choices=CHOICES, default=0)
    my_appetite_has_increased = models.IntegerField(choices=CHOICES, default=0)
    i_lost_weight_not_by_diet_or_exercise = models.IntegerField(choices=CHOICES, default=0)
    i_think_my_work_pace_has_decreased  = models.IntegerField(choices=CHOICES, default=0)
    i_cant_laugh_at_funny_incidents = models.IntegerField(choices=CHOICES, default=0)
    i_lost_interest_in_sexual_matters = models.IntegerField(choices=CHOICES, default=0)
    i_cant_participate_in_social_activities_anymore_like_before  = models.IntegerField(choices=CHOICES, default=0)
    i_cant_do_my_educational_or_occupational_work_like_before = models.IntegerField(choices=CHOICES, default=0)

    @property
    def depression_level(self):
        return self.i_feel_unrest+self.nowadays_i_am_gloomy+self.i_feel_my_future_is_dark\
               +self.in_future_my_condition_will_get_worse+self.i_feel_everything_has_fallen_apart\
               +self.i_feel_like_my_life_is_very_difficult_now+self.i_feel_like_i_am_totally_a_disappointment_as_a_human\
               +self.i_cant_find_happiness_in_anything+self.i_feel_inferior+self.my_confidence_has_fallen_down\
               +self.i_feel_like_people_pity_me+self.life_is_meaningless+self.i_often_feel_like_crying\
               +self.i_often_feel_irritated+self.i_dont_find_interest_in_anything+self.nowadays_i_cant_think_and_take_decisions\
               +self.currently_i_cant_give_my_concentration_on_anything+self.i_feel_trouble_remembering\
               +self.i_feel_weak_and_get_tired_easily+self.i_sleep_less_nowadays+self.i_sleep_more_nowadays\
               +self.my_temper_gets_irritable+self.my_appetite_has_decreased+self.my_appetite_has_increased\
               +self.i_lost_weight_not_by_diet_or_exercise+self.i_think_my_work_pace_has_decreased\
               +self.i_cant_laugh_at_funny_incidents+self.i_lost_interest_in_sexual_matters\
               +self.i_cant_participate_in_social_activities_anymore_like_before\
               +self.i_cant_do_my_educational_or_occupational_work_like_before



class Case_File(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, parent_link=True)
    CLOSE = 0
    OPEN = 1

    STATUS = ((CLOSE, 'Closed'), (OPEN, 'Open'))

    status = models.BooleanField(choices=STATUS, default=0)
    category = models.CharField(max_length=25, blank=True, null=True)

    @property
    def anxiety(self):
        level = self.client.anxietymeasure.anxiety_level()

        if level <= 54:
            return "Mild"
        elif level >= 55 or level <= 66:
            return "Moderate"
        elif level >= 67 or level <= 77:
            return "Severe"
        elif level >= 78:
            return "Profound"
        else:
            return "Not suffering from Anxiety"

    @property
    def depression(self):
        level = self.client.depressionmeasure.depression_level()

        if level > 24 or level < 30:
            return "Depressed"
        elif level >= 30 or level <=100:
            return "Minimal"
        elif level >= 101 or level <= 114:
            return "Mild"
        elif level >= 115 or level <= 123:
            return "Moderate"
        elif level >= 124 or level <=150:
            return "Severe"
        else:
            return "Not suffering from Anxiety"

    def __str__(self):
        return "%s" % self.client.name


'''
def has_perm(self, perm, obj=None):
    return True


def has_module_perms(self, app_label):
    return True

# def keyboardInterruptHandler(signal, frame):
# print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
# exit(0)

# signal.signal(signal.SIGINT, keyboardInterruptHandler)

# while True:
# pass
'''