from django.shortcuts import render


def greeting(request):
    name = {"name": "unknown"}
    if "name" in request.GET:
        name["name"] = request.GET["name"]

    return render(request, "home.html", name)
