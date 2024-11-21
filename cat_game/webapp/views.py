from django.shortcuts import render, redirect


def index_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            context = {
                'name': name,
                'age': 1,
                'satiety': 40,
                'happy_scale': 40,
            }
            return render(request, 'cat.html', context=context)
    return render(request, 'index.html')


def cat_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = int(request.POST.get('age', 1))
        satiety = int(request.POST.get('satiety', 40))
        happy_scale = int(request.POST.get('happy_scale', 40))

        action = request.POST.get('action')
        if action == 'feed':
            satiety = min(satiety + 10, 100)
            happy_scale = min(happy_scale + 5, 100)
        elif action == 'play':
            happy_scale = min(happy_scale + 15, 100)
            satiety = max(satiety - 10, 0)
            if satiety == 0:
                happy_scale = max(happy_scale - 30, 0)
        elif action == 'sleep':
            satiety = max(satiety - 5, 0)
            happy_scale = max(happy_scale - 5, 0)


        context = {
            'name': name,
            'age': age,
            'satiety': satiety,
            'happy_scale': happy_scale,
        }
        return render(request, 'cat.html', context=context)
    else:
        return redirect('/')
