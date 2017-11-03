# -*- coding: utf-8 -*-
from polls.models import Question
from polls.views import IndexView
from django.utils import timezone


class ExtendedIndexView(IndexView):

    def get_queryset(self):
        """
        Return the last ten published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]
