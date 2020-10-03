from rest_framework import serializers
from ghostpost_app.models import BoastsRoastsModel


# Worked with Sohail and Albina too on the planning/beginning stage before finishing separately
class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastsRoastsModel
        fields = [
            'id',
            'is_boast',
            'post_content',
            'upvotes',
            'downvotes',
            'post_datetime',
            'privatesecret_key',
            'vote_sum'
        ]
