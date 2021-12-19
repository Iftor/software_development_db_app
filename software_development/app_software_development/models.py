from django.db import models



class ProgrammingLanguage(models.Model):
    programming_language_name = models.CharField(max_length=30, null=False, verbose_name='Название')

    def __str__(self) -> str:
        return self.programming_language_name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
        db_table = 'programming_languages'


class PersonalityFile(models.Model):
    firstname = models.CharField(max_length=30, null=False, verbose_name='Имя')
    lastname = models.CharField(max_length=30, null=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=100, null=False, verbose_name='Электронная почта', unique=True)

    def __str__(self) -> str:
        return f'{self.lastname} {self.firstname}'

    class Meta:
        verbose_name = 'Личное дело'
        verbose_name_plural = 'Личные дела'
        db_table = 'personality_files'



class Client(models.Model):
    orders_number = models.IntegerField(null=False, default=0, verbose_name='Количество заказов')
    personality_file = models.OneToOneField(PersonalityFile, null=False, on_delete=models.CASCADE, verbose_name='Личное дело')

    def __str__(self) -> str:
        return str(self.personality_file)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'clients'


class Employee(models.Model):
    salary = models.IntegerField(null=False, verbose_name='Зарплата')
    personality_file = models.OneToOneField(PersonalityFile, null=False, on_delete=models.CASCADE, verbose_name='Личное дело')

    def __str__(self) -> str:
        return str(self.personality_file)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        db_table = 'employees'


class Tester(models.Model):
    employee = models.OneToOneField(Employee, null=False, on_delete=models.CASCADE, verbose_name='Сотрудник')
    programming_language = models.ForeignKey(ProgrammingLanguage, null=True, on_delete=models.SET_NULL, verbose_name='Язык программирования')

    def __str__(self) -> str:
        return f'Тестировщик на {self.programming_language}: {self.employee}'

    class Meta:
        verbose_name = 'Тестировщик'
        verbose_name_plural = 'Тестировщики'
        db_table = 'testers'


class Programmer(models.Model):
    employee = models.OneToOneField(Employee, null=False, on_delete=models.CASCADE, verbose_name='Сотрудник')
    programming_language = models.ForeignKey(ProgrammingLanguage, null=True, on_delete=models.SET_NULL, verbose_name='Язык программирования')

    def __str__(self) -> str:
        return f'Программист на {self.programming_language}: {self.employee}'

    class Meta:
        verbose_name = 'Программист'
        verbose_name_plural = 'Программисты'
        db_table = 'programmers'


class Teamlead(models.Model):
    employee = models.OneToOneField(Employee, null=False, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self) -> str:
        return str(self.employee)

    class Meta:
        verbose_name = 'Тимлид'
        verbose_name_plural = 'Тимлиды'
        db_table = 'teamleads'


class Order(models.Model):
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE, verbose_name='Клиент')
    required_programming_language = models.ForeignKey(ProgrammingLanguage, null=True, on_delete=models.SET_NULL, verbose_name='Требуемый язык программирования')
    receiving_date = models.DateField(null=False, auto_now_add=True, verbose_name='Дата получения заказа')
    deadline = models.DateField(null=True, verbose_name='Крайний срок')

    def __str__(self) -> str:
        return f'Заказ №{self.id}. Заказчик: {self.client}. Дата заказа {self.receiving_date}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'orders'


class Project(models.Model):
    teamlead = models.ForeignKey(Teamlead, null=True, on_delete=models.SET_NULL, verbose_name='Тимлид')
    programming_language = models.ForeignKey(ProgrammingLanguage, null=True, on_delete=models.SET_NULL, verbose_name='Язык программирования')
    order = models.OneToOneField(Order, null=False, on_delete=models.CASCADE, verbose_name='Заказ')
    beginning_date = models.DateField(null=False, auto_now_add=True, verbose_name='Дата начала')
    ending_date = models.DateField(null=True, verbose_name='Дата завершения', blank=True)
    programmers = models.ManyToManyField(Programmer, db_table='programmers_in_projects', verbose_name='Программисты')
    testers = models.ManyToManyField(Tester, db_table='testers_in_projects', verbose_name='Тестировщики')

    def __str__(self) -> str:
        return f'Проект по заказу №{self.order.id}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        db_table = 'projects'
