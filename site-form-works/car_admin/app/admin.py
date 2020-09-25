from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from django import forms
from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')
    search_fields = ('brand', 'model')
    list_filter = ('brand', 'model')

# class ReviewAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = Review
#         fields = '__all__'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title')
    search_fields = ('car', 'title')
    list_filter = ('car', 'title')
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
