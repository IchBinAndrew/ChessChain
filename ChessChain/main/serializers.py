from rest_framework import serializers
from .models import Room

#class RoomModel:
#    def __init__(self, title, max_amount_of_members, private, status):
#        self.title = title
#       self.max_amount_of_members = max_amount_of_members
#       self.private = private
#        self.status = status

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("title", "creation_time", "max_amount_of_members", "private", "owner", "status")