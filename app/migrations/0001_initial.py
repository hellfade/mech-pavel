# Generated by Django 4.1.7 on 2023-03-29 14:06

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "patronymic",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Отчество"
                    ),
                ),
                (
                    "date_of_birthday",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "passport_series",
                    models.IntegerField(blank=True, null=True, verbose_name="Серия"),
                ),
                (
                    "passport_number",
                    models.IntegerField(blank=True, null=True, verbose_name="Номер"),
                ),
                (
                    "date_references",
                    models.DateField(blank=True, null=True, verbose_name="Дата выдачи"),
                ),
                (
                    "by_whom",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Кем выдан"
                    ),
                ),
                (
                    "house",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="Дом"
                    ),
                ),
                (
                    "apartment",
                    models.IntegerField(blank=True, null=True, verbose_name="Квартира"),
                ),
                (
                    "tel",
                    models.CharField(
                        blank=True, max_length=12, null=True, verbose_name="Телефон"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Статус"
                    ),
                ),
                (
                    "is_cursant",
                    models.BooleanField(default=False, verbose_name="Курсант"),
                ),
                (
                    "is_worker",
                    models.BooleanField(default=False, verbose_name="Сотрудник"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
            ],
            options={
                "verbose_name": "пользователи",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gos_number",
                    models.CharField(max_length=8, verbose_name="Гос. номер"),
                ),
                ("model", models.CharField(max_length=255, verbose_name="Модель")),
                ("mark", models.CharField(max_length=255, verbose_name="Марка")),
                ("date_release", models.DateField(verbose_name="Дата выпуска")),
            ],
            options={
                "verbose_name": "автомобили",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_category",
                    models.CharField(max_length=155, verbose_name="Название"),
                ),
            ],
            options={
                "verbose_name": "категории",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="Стоимость")),
                ("start_date_education", models.DateField(verbose_name="Дата начала")),
                ("end_date_education", models.DateField(verbose_name="Дата окончания")),
                (
                    "id_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "курсы",
            },
        ),
        migrations.CreateModel(
            name="Discipline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_discipline",
                    models.CharField(
                        max_length=255, verbose_name="Название дисциплины"
                    ),
                ),
                ("count_hourse", models.IntegerField(verbose_name="Часов")),
                (
                    "type_class",
                    models.CharField(max_length=255, verbose_name="Тип класса"),
                ),
            ],
            options={
                "verbose_name": "дисциплины",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
            ],
            options={
                "verbose_name": "должности",
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
            ],
            options={
                "verbose_name": "регионы",
            },
        ),
        migrations.CreateModel(
            name="Street",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
            ],
            options={
                "verbose_name": "улицы",
            },
        ),
        migrations.CreateModel(
            name="Training",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "agreement_number",
                    models.IntegerField(verbose_name="Номер договора"),
                ),
                ("date_agreement", models.DateTimeField(verbose_name="Дата договора")),
                (
                    "certificate",
                    models.CharField(max_length=255, verbose_name="Свидетельство"),
                ),
                ("date_record", models.DateField(verbose_name="Дата зачисления")),
                ("price", models.IntegerField(verbose_name="Стоимость")),
                ("payment_status", models.BooleanField(verbose_name="Статус оплаты")),
                (
                    "id_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.course",
                        verbose_name="Курс",
                    ),
                ),
                (
                    "id_cursant",
                    models.ForeignKey(
                        limit_choices_to={"is_cursant": 1},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cursant",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Курсант",
                    ),
                ),
            ],
            options={
                "verbose_name": "обучения",
            },
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_class", models.DateField(verbose_name="Дата занятия")),
                ("time_class", models.TimeField(verbose_name="Время занятия")),
                (
                    "id_cursant",
                    models.ForeignKey(
                        limit_choices_to={"is_cursant": 1},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Cursant",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Курсант",
                    ),
                ),
                (
                    "id_discipline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.discipline",
                        verbose_name="Дисциплина",
                    ),
                ),
                (
                    "id_worker",
                    models.ForeignKey(
                        limit_choices_to={"is_worker": 1, "post": 2},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Worker",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Сотрудник",
                    ),
                ),
            ],
            options={
                "verbose_name": "расписания",
            },
        ),
        migrations.CreateModel(
            name="Driving",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("result", models.CharField(max_length=255, verbose_name="Результат")),
                (
                    "id_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.car",
                        verbose_name="Автомобиль",
                    ),
                ),
                (
                    "id_cursant",
                    models.ForeignKey(
                        limit_choices_to={"is_cursant": 1},
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Курсант",
                    ),
                ),
                (
                    "id_schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.schedule",
                        verbose_name="Расписание",
                    ),
                ),
            ],
            options={
                "verbose_name": "вождения",
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "id_region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.region",
                        verbose_name="Регион",
                    ),
                ),
            ],
            options={
                "verbose_name": "города",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="id_city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.city",
                verbose_name="Город",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="id_post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.post",
                verbose_name="Должность",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="id_region",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.region",
                verbose_name="Регион",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="id_street",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.street",
                verbose_name="Улица",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
