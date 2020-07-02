from django.shortcuts import render

posts = [
    {
        'author': 'Anski',
        'title': 'Posting!!!',
        'content': 'Shitty content here',
        'date_posted': 'July 2nd 2020'
    },
    {
        'author': 'WhoHere',
        'title': '2nd Post wow',
        'content': 'Crappy content here',
        'date_posted': 'July 3nd 2020'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})