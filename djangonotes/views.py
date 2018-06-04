from django.shortcuts import render


def test(request):
    return render(request, 'notes/post_add.html')
