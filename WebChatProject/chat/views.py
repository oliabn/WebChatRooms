from django.shortcuts import render, redirect


def chatPage(request, *args, **kwargs):
    """If user is authenticated he gets chatPage.
    If user isn't authenticated he gets LoginView"""

    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)
