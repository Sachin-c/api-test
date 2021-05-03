from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from account.models import account
from advisor.models import Advisor
from auth.serializers import AdvisorSerializer


@api_view(['POST', ])
def api_advisor_view_post(request):

    if request.method == "POST":
        serializer = AdvisorSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
