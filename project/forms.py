from django import forms


class CustomerForm(forms.Form):
    SUBSCRIPTION_TYPES = (
        ("Free", "Free"),
        ("Plus", "Plus"),
        ("Pro", "Pro")
    )
    customer_name = forms.CharField(max_length=100, required=True)
    subscription_type = forms.ChoiceField(choices=SUBSCRIPTION_TYPES, required=True)
    email_address = forms.EmailField(required=True)
