from django import forms


class MissionForm(forms.Form): #this is the core of the mission planning form

    template = forms.CharField() # Define all the fields of the form

    prior = [('1', 'Yes'), ('2', 'No')]

    priority = forms.ChoiceField(label='Priority task', widget=forms.RadioSelect,choices=prior)

    morepasses = [('1', 'Yes'), ('2', 'No')]

    passes = forms.ChoiceField(label='Can be split in multiple passes?', widget=forms.RadioSelect, choices=CHOICES2)

    startfirst = forms.BooleanField(label='First available pass')

    startcustom = forms.BooleanField(label='Enter custom value')

    customtime = forms.IntegerField(label='Custom value')

    commands = forms.CharField(label='Command line interface',
                               widget=forms.Textarea(attrs={"placeholder": "Write your commands here"}))

    ADCS_state = forms.CharField(label='Set ADCS state')

    maneuvertype = [('1', 'Nadir'), ('2', 'Slew')]

    maneuver = forms.ChoiceField(label='Choose maneuver', widget=forms.RadioSelect, choices=maneuvertype)

    firstN = forms.FloatField(label='1 ')

    firstE = forms.FloatField(label='')

    secondN = forms.FloatField(label='2 ')

    secondE = forms.FloatField(label='')

    numberframes = forms.IntegerField(label='HSI '
    'Number of frames')

    hsiparam = [('1', 'Default'), ('2', 'Enter custom values')]

    parameters = forms.ChoiceField(label='Camera parameters', widget=forms.RadioSelect, choices=hsiparam)

    naming = [('1', 'Default'), ('2', 'Enter custom values')]

    file_naming = forms.ChoiceField(widget=forms.RadioSelect, choices=naming)

    rgbfile = [('1', 'Default'), ('2', 'Upload custom config file')]

    RGBinit = forms.ChoiceField(label='RGB'
    'Initialization', widget=forms.RadioSelect, choices=rgbfile)

    rgbparam = [('1', 'Default'), ('2', 'Upload custom values')]

    camera_parameters = forms.ChoiceField(widget=forms.RadioSelect, choices=rgbparam)

    trigger = [('1', 'On'), ('2', 'Off')]

    hardware_trigger = forms.ChoiceField(widget=forms.RadioSelect, choices=trigger)

    demoption = [('1', 'rgb'), ('2', 'raw')]

    demosaic_options = forms.ChoiceField(widget=forms.RadioSelect, choices=demoption)

    image_format = forms.CharField()

    rgbname = [('1', 'Default'), ('2', 'Enter custom values')]

    rgbfilename = forms.ChoiceField(label='File naming', widget=forms.RadioSelect, choices=rgbname)
