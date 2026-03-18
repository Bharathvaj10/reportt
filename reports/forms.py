from django import forms
from .models import MedicalReport, EmergencyContact, Reminder

class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['title', 'file', 'category', 'doctor_name', 'hospital_name', 'report_date']
        widgets = {
            'report_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'glass'})

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['name', 'phone', 'relationship']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'glass'})

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['medicine_name', 'dosage', 'dosage_count', 'contact_info', 'time', 'start_date', 'end_date']
        labels = {
            'contact_info': 'Email Address (for reminder)',
        }
        widgets = {
            'contact_info': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'glass'})
