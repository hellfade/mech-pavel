from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from .models import Training, Schedule, User, Discipline
from .forms import CursantPostScheduleForm, SignupForm


class HomeView(View):

    def showPage(request):
        if request.method == 'GET':
            return render(request, 'index.html')


@login_required()
class ProfileView(View):

    def showPage(request):

        if request.user.is_authenticated:
            user = request.user

            if request.user.is_cursant:
                training = Training.objects.get(id_cursant=user.id)

                return render(request, 'cursant/profile.html', {'user': user, 'training': training})

            elif request.user.is_worker:
                if request.user.id_post == 'Инструктор':
                    return render(request, 'worker/profile.html', {'user': user})

                else:
                    return render(request, 'worker/profile-2.html', {'user': user})

        else:
            return redirect('login')


@login_required()
class ScheduleView(View):

    def showPage(request):

        form = CursantPostScheduleForm(request.POST)

        if request.user is not None and request.user.is_cursant:
            user = request.user
            schedule = Schedule.objects.filter(id_cursant=user.id)

            return render(request, 'cursant/schedule.html', {'schedule': schedule, 'form': form})

        elif request.user is not None and request.user.is_worker:
            user = request.user
            schedule = Schedule.objects.filter(id_worker=user.id)

            return render(request, 'worker/schedule.html', {'schedule': schedule})

        else:
            return redirect('login')

    def deletePage(request, id):
        remove = Schedule.objects.filter(id_cursant=request.user.id).filter(id=id).delete()

        return redirect('schedule')

    def postPage(request):
        date = request.POST['date_class']
        time = request.POST['time_class']

        if Schedule.objects.filter(date_class=date) and Schedule.objects.filter(time_class=time):
            message = 'На данное время инструктор занят! Выберите другой день или время.'
            return render(request, 'cursant/schedule.html', {'message': message})

        else:
            schedule_new = Schedule(id_worker=User.objects.get(id=request.POST['id_worker']),
                                    id_discipline=Discipline.objects.get(id=request.POST['id_discipline']),
                                    id_cursant=request.user,
                                    date_class=date,
                                    time_class=time)

            schedule_new.save()

        return redirect('schedule')


@login_required()
class ControlView(View):

    def showPage(request):

        return render(request, 'worker/control.html')


class RedirectProfile(View):

    def showPage(request):
        return redirect('/profile/')


class SignupView(View):

    def showPage(request):
        message = ""

        if request.user.is_authenticated:
            return redirect("/profile/")
        else:
            if request.method == "GET":
                form = SignupForm()

            if request.method == "POST":
                form = SignupForm(request.POST)

                print(request.POST)

                if form.is_valid():
                    user = form
                    user.save()
                    message = "Успешная регистрация!"
                    return redirect('/profile/')
                else:
                    message = "Введите корректные данные"
                    form = SignupForm()

            return render(request, "registration/signup.html", {"form": form, "message": message})
