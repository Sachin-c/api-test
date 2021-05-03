from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from django.contrib.auth.models import User
from advisor.models import Advisor, Booking
from rest_framework.response import Response
from rest_framework.decorators import api_view
from auth.serializers import AdvisorSerializer, BookingSerializer, ShowBookingSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET', ])
def api_advisor_view(request, userid=None):
    advisor = Advisor.objects.all()
    for a in advisor:
        print(a)
    if request.method == "GET":
        serializer = AdvisorSerializer(advisor, many=True, read_only=True)
        return Response(serializer.data)


@api_view(['POST', ])
def api_advisor_view_post(request, userid, advisorid):
    ad = Advisor.objects.get(advisor_id=advisorid)

    request.data.update({'advisor_name': ad.name, 'advisor_id': ad.advisor_id, 'advisor_image': ad.image})
    print(request.data)
    print(ad)
    print(ad.name)
    if request.method == "POST":
        serializer = BookingSerializer(data=request.data)

        # serializer.context["advisor_name"] = ad.name
        # serializer.context["advisor_id"] = ad.advisor_id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', ])
def api_booking_view(request, userid=None):
    booking = Booking.objects.all()
    if request.method == "GET":
        serializer = BookingSerializer(booking, many=True, read_only=True)
        return Response(serializer.data)
