from django import forms
from .models import Review, SpaService, SpecificDate, TimeSlot, TimeSlotAvailability


class reviewForm(forms.ModelForm):
    """ Lets users review spa services. From Blog walkthroug"""
    class Meta:
        model = Review
        fields = ('body',)


class MultiDateInput(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control', 'placeholder': 'Select multiple dates'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

class SpecificDateAdminForm(forms.ModelForm):
    dates = forms.CharField(
        widget=MultiDateInput(attrs={'id': 'specific_dates_picker'}),
        help_text='Enter multiple dates separated by commas (e.g., 2024-08-01, 2024-08-02)'
    )

    class Meta:
        model = SpecificDate
        fields = []

    def clean_dates(self):
<<<<<<< HEAD
        dates = self.cleaned_data['dates']
        date_list = [date.strip() for date in dates.split(',') if date.strip()]

        if len(date_list) != len(set(date_list)):
            raise forms.ValidationError("You have entered duplicate dates.")

        existing_dates = SpecificDate.objects.filter(date__in=date_list).values_list('date', flat=True)
        if existing_dates:
            existing_dates_str = ", ".join([date.strftime('%Y-%m-%d') for date in existing_dates])
            raise forms.ValidationError(f"The following dates already exist: {existing_dates_str}")

        return date_list

    def save(self, commit=True):
        date_list = self.cleaned_data['dates']
        specific_date_objects = []
        for date in date_list:
            specific_date = SpecificDate(date=date)
            specific_date_objects.append(specific_date)
        if commit:
            SpecificDate.objects.bulk_create(specific_date_objects)
        return specific_date_objects
=======
        dates = self.cleaned_data.get('dates')
        if dates:
            date_list = [date.strip() for date in dates.split(',') if date.strip()]
            unique_dates = set(date_list)
            for date in unique_dates:
                if SpecificDate.objects.filter(date=date).exists():
                    raise forms.ValidationError(f"The date {date} already exists.")
            return unique_dates
        return []

    def save(self, commit=True):
        unique_dates = self.cleaned_data['dates']
        specific_date_objects = [SpecificDate(date=date) for date in unique_dates]
        SpecificDate.objects.bulk_create(specific_date_objects)
        return specific_date_objects
        
>>>>>>> 16de44819b15276aab4d09fc699661d1f8919c58

    class Media:
        js = ('https://cdn.jsdelivr.net/npm/flatpickr', 'admin/js/init_flatpickr.js')
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css',)
        }

