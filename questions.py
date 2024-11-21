from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL
class OptionType(models.Model):
    """
    Model representing the type of an option for a form input field.

    Fields:
    - name: Descriptive name of the option type (e.g., 'Multi-select', 'Radio').
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AnswerType(models.Model):
    """
    Model representing the type of an answer for a form input field.

    Fields:
    - name: Descriptive name of the answer type ('Essay', 'Short Text', 'Yes/No', 'Number', 'Boolean', 'Email', 'Options').
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomForm(models.Model):
    """
    Model representing a custom registration form for users interested in an event.

    Fields:
    - title: Title of the registration form.
    - user: ForeignKey to User model representing the user who created the form.
    """
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registration Form: {self.title}"


class FormQuestion(models.Model):
    """
    Model representing a question in a custom registration form.

    Fields:
    - form: ForeignKey to CustomForm model representing the form to which the question belongs.
    - question: The question to be displayed in the form.
    - answer_type: ForeignKey to AnswerType model representing the type of answer expected for the question.
    - required: BooleanField indicating whether the question is mandatory.
    """
    form = models.ForeignKey(CustomForm, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=500)
    answer_type = models.ForeignKey(AnswerType, on_delete=models.SET_NULL, null=True, blank=True)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Option(models.Model):
    """
    Model representing an option for a form input field.

    Fields:
    - question: ForeignKey to FormQuestion model representing the question to which the option belongs.
    - value: Value of the option.
    - option_type: ForeignKey to OptionType model representing the type of the option.
    """
    question = models.ForeignKey(FormQuestion, on_delete=models.CASCADE, related_name='options')
    value = models.CharField(max_length=100)
    option_type = models.ForeignKey(OptionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class ShortAnswer(models.Model):
    """
    Model representing a short answer to a form question.

    Fields:
    - question: ForeignKey to FormQuestion model representing the question answered.
    - value: The short answer provided by the user.
    """
    question = models.ForeignKey(FormQuestion, on_delete=models.CASCADE, related_name='short_answers')
    value = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.value


class EssayAnswer(models.Model):
    """
    Model representing an essay answer to a form question.

    Fields:
    - question: ForeignKey to FormQuestion model representing the question answered.
    - value: The essay answer provided by the user.
    """
    question = models.ForeignKey(FormQuestion, on_delete=models.CASCADE, related_name='essay_answers')
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.value
