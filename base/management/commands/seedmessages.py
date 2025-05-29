import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from base.management.commands.dummy_data import host_messages, participants_messages
from base.models import Message, Room


class Command(BaseCommand):
    help = "Seed contextual messages for each room"

    def handle(self, *args, **options):
        print("Deleting messages...")
        Message.objects.all().delete()
        print("Deletion done!")

        User = get_user_model()
        users = User.objects.all()
        rooms = Room.objects.all()

        print("Creating messages...")
        for index, room in enumerate(rooms):
            host_message = host_messages[index]

            for message in participants_messages[index]:
                participant = random.choice([u for u in users if u != room.host])
                Message.objects.create(user=participant, room=room, body=message)
                room.participants.add(participant)

            Message.objects.create(user=room.host, room=room, body=host_message)
        print("Messages creation done!")
