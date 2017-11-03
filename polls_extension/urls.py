# -*- coding: utf-8 -*-
from polls.urls import urlpatterns
from polls_extension.views import ExtendedIndexView

urlpatterns = list(urlpatterns)

for url in urlpatterns:
    if url.name == 'index':
        url.callback = ExtendedIndexView.as_view()