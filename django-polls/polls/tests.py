from django.test import TestCase
import datetime
# Create your tests here.
from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTest(TestCase):

    def test_was_published_with_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date = time)
        self.assertIs(past_question.was_published_recently(), False);


