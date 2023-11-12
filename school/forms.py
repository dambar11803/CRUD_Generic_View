from django import forms 
from .models import Student 

GENDER_CHOICES=[ ('M', 'Male'), ('F','Female'),]

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student 
        fields= '__all__'
      
        gender= forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
        widgets = {
            'dob': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'myclass'})}
        
        widgets={'name':forms.TextInput(attrs={'class':'myclass'}), 
                'address':forms.TextInput(attrs={'class':'myclass'}),
                'roll':forms.NumberInput(attrs={'class':'myclass'}),
                'grade':forms.NumberInput(attrs={'class':'myclass'}),
                'email':forms.EmailInput(attrs={'class':'myclass'}),
                'gender':forms.RadioSelect(attrs={'class':'myclass'}),
                'pic':forms.RadioSelect(attrs={'class':'myclass'})
                }
        
        