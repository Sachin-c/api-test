from django.urls import path
from advisor.api.views import (
    # api_advisor_view,
    api_advisor_view_post,
)

app_name = 'advisor'

urlpatterns = [
    path('admin/advisor/', api_advisor_view_post, name="post"),
    # path('user/<int:id>/advisor/', api_advisor_view, name="detail"),
]
