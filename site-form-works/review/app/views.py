from django.views.generic import ListView, DetailView

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


class ProductListView(ListView):
    template_name = 'app/product_list.html'
    model = Product


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    text = Review.objects.select_related('product')

    form = ReviewForm
    if request.method == 'POST' and ("pause" not in request.session):
        rev_form = ReviewForm(request.POST)
        if rev_form.is_valid():
            comment = rev_form.save(commit=False)
            comment.product = Product.objects.get(id=pk)
            rev_form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True

    context = {
        'form': form,
        'product': product,
        'reviews': text,
    }

    return render(request, template, context)
