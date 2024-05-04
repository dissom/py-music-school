from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        ]

    def create(self, validated_data) -> Musician:
        return Musician.objects.create(**validated_data)

    def retrieve(self, pk):
        instance = get_object_or_404(Musician, pk=pk)
        return instance

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )
        instance.instrument = validated_data.get(
            "instrument", instance.instrument
        )
        instance.age = validated_data.get(
            "age", instance.age
        )
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
