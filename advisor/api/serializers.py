from rest_framework import serializers

from advisor.models import Advisor


class AdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advisor
        fields = ['advisor_id', 'name', 'image']
