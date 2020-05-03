from django import forms


class MissionForm(forms.Form):

    template = forms.CharField()

    CHOICES1 = [('1', 'Yes'), ('2', 'No')]

    choice_field = forms.ChoiceField(label='Priority task', widget=forms.RadioSelect, choices=CHOICES1)

    CHOICES2 = [('1', 'Yes'), ('2', 'No')]

    passes = forms.ChoiceField(label='Can be split in multiple passes?', widget=forms.RadioSelect, choices=CHOICES2)

    startfirst = forms.BooleanField(label='First available pass')

    startcustom = forms.BooleanField(label='Enter custom value')

    customtime = forms.IntegerField(label='Custom value')

    commands = forms.CharField(label='Command line interface',
                               widget=forms.Textarea(attrs={"placeholder": "Write your commands here"}))


