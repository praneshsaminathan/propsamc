from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class GeoCodeSerializer(serializers.Serializer):
    file = serializers.FileField(allow_empty_file=False)

    class Meta:
        fields = ('file',)

    def validate_file(self, data):
        if data.name.split('.')[1] in ['csv']:
            return data

        raise serializers.ValidationError(_('Invalid Format. Please upload only CSV'))
