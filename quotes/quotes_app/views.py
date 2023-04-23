import os

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote


# Create your views here.
def main(request):
    return render(request, 'quotes_app/index.html', context={"title": "Quotes main!"})


@login_required
def add_quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    form = QuoteForm(instance=Quote())
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            quote = form.save()
            tags = Tag.objects.filter(tag__in=request.POST.getlist('tags'))
            for tag in tags.iterator():
                quote.tags.add(tag)
            author = Author.objects.get(id=request.POST.get('author'))
            quote.author = author
            quote.save()
            return redirect(to="quotes_app:quotes")
    return render(request, 'quotes_app/add_quote.html',
                  context={"title": "Add quotes!", "tags": tags, "authors": authors, "form": form})


@login_required
def add_tag(request):
    form = TagForm(instance=Tag())
    if request.method == "POST":
        form = TagForm(request.POST, instance=Tag())
        if form.is_valid():
            form.save()
            return render(request, 'quotes_app/add_tag.html',
                          context={"title": "Add tags!", "form": TagForm(instance=Tag())})
    return render(request, 'quotes_app/add_tag.html', context={"title": "Add tags!", "form": form})


@login_required
def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            form.save()
            return render(request, 'quotes_app/add_author.html',
                          context={"title": "Add authors!", "form": AuthorForm(instance=Author())})
    return render(request, 'quotes_app/add_author.html', context={"title": "Add authors!", "form": form})


def quotes(request):
    all_quotes = Quote.objects.all()
    for quote in all_quotes:
        quote.tags_to_show = quote.tags.all()
    return render(request, 'quotes_app/quotes.html', context={"title": "Quotes", "quotes": all_quotes})
