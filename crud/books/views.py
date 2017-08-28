from django.views import generic
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Book
from .forms import BookForm


class IndexView(generic.ListView):
    template_name = 'books/book_list.html'
    queryset = Book.objects.all()


def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            book_list = Book.objects.all()
            data['html_book_list'] = render_to_string(
                'books/includes/partial_book_list.html',
                { 'book_list': book_list },
            )
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()

    context = {'form': form}
    data['html_form'] = render_to_string(
        'books/includes/partial_book_create.html',
        context,
        request=request,
    )

    return JsonResponse(data)
