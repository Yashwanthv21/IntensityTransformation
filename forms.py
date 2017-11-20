from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField()

# TODO dynamically generate form fields based on selection or you can write in JavaScript
# class TestCharField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super(TestCharField, self).__init__(*args, **kwargs) # Needs * and **
#     def clean(self, value):
#         super(TestCharField, self).clean(value)
#         # Do custom validation in here
#         return value
# https://stackoverflow.com/questions/6154580/django-dynamic-form-example
#https://stackoverflow.com/questions/6142025/dynamically-add-field-to-a-form
# class Operationsform(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(Operationsform, self).__init__(*args, **kwargs)
#
#         # args should be a list with the single QueryDict (GET or POST dict)
#         # that you passed it
#         for k,v in args[0].items():
#             if k.startswith('Q') and k not in self.fields.keys():
#                 self.fields[k] = TestCharField(initial=v, required=True)

class OperationsForm(forms.Form):
    CHOICES=((1,'Histogram Matching'),(2,'Hist'))
    operation = forms.ChoiceField(choices=CHOICES)