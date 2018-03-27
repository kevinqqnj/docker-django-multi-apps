# from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Question, Choice

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'question_text', 'pub_date')


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.ReadOnlyField(source='question.question_text')

    class Meta:
        model = Choice
        fields = ('url', 'question', 'choice_text', 'votes')

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
