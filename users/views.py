from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer
from users.services import create_price, create_session


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


class PaymentsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['date_payment']


class PaymentsCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        new_price = create_price(payment.payment_amount)
        session_id, link_payment = create_session(new_price)
        payment.session_id = session_id
        payment.link_payment = link_payment
        payment.save()


