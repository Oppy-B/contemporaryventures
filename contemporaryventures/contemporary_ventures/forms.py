from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            "class":"text-input"
            
        }

        )
    )

    your_email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            "class":"text-input"
            
        }
        )
    )
    
    your_phone = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            "class":"text-input"
            
        }
        )
    )   

    message = forms.CharField(
        widget=forms.Textarea(attrs={
        'rows':0,
        'cols':0
        
        }
        )
    )