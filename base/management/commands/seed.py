import os

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from faker import Faker

from base.management.commands.dummy_data import (
    dev_bios,
    topic_names,
)
from base.models import Message, Room, Topic


class Command(BaseCommand):
    help = "Seeding the database with users, topcis and rooms"

    def handle(self, *args, **options):
        User = get_user_model()
        fake = Faker()
        media_dir = settings.MEDIA_ROOT

        print("Deleting database entries...")
        for filename in os.listdir(media_dir):
            file_path = os.path.join(media_dir, filename)
            if filename.endswith(".jpg") and os.path.isfile(file_path):
                os.remove(file_path)

        Message.objects.all().delete()
        Room.objects.all().delete()
        Topic.objects.all().delete()
        User.objects.all().delete()
        print("Deletion done!")

        print("Creating users...")

        users = []
        for i in range(len(dev_bios)):
            is_female = i % 4 == 0
            first_name = (
                fake.first_name_female() if is_female else fake.first_name_male()
            )
            last_name = fake.last_name()
            name = f"{first_name} {last_name}"
            username = f"{first_name[0]}{last_name}".lower()
            email = (
                f"{first_name[0]}.{last_name}".lower() + "@" + fake.free_email_domain()
            )

            avatar_url = f"https://randomuser.me/api/portraits/{'women' if is_female else 'men'}/{i % 100}.jpg"

            response = requests.get(avatar_url)
            if response.status_code == 200:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()

                user = User.objects.create_user(
                    username=username,
                    name=name,
                    email=email,
                    password="password123",
                    bio=dev_bios[i],
                )

                avatar_filename = f"{username}.jpg"
                user.avatar.save(avatar_filename, File(img_temp), save=True)

                users.append(user)
        print("User creation done!")

        print("Creating topics...")
        topics = [Topic.objects.create(name=name) for name in topic_names]
        print("Topics creation done!")

        print("Creating rooms...")
        rooms = [
            # JavaScript
            {
                "host": users[
                    8
                ],  # "Full-stack engineer. Coffee enthusiast. Code is poetry."
                "topics": topics[0],
                "name": "Async/Await Demystified",
                "desc": "Async/Await, Promises, and callbacks — let’s talk async in JS.",
            },
            {
                "host": users[18],  # "I dream in TypeScript."
                "topics": topics[0],
                "name": "Modern JavaScript Patterns",
                "desc": "Discuss best practices, quirks, and modern ES features in JavaScript.",
            },
            {
                "host": users[19],  # "🚀 Scaling apps and frying CPUs."
                "topics": topics[0],
                "name": "Vanilla JS Power",
                "desc": "No frameworks, just pure JavaScript: DOM, events, and closures.",
            },
            {
                "host": users[25],  # "Functional programming changed my brain."
                "topics": topics[0],
                "name": "Functional Programming in JS",
                "desc": "Dive into map, reduce, and functional purity in JavaScript.",
            },
            {
                "host": users[31],  # "Async all the things!"
                "topics": topics[0],
                "name": "Event Loop Explained",
                "desc": "Demystify the JavaScript event loop, call stack, task queue, and microtasks.",
            },
            # Python
            {
                "host": users[
                    1
                ],  # "Backend engineer specializing in Python and Django."
                "topics": topics[1],
                "name": "Pythonic Code Lab",
                "desc": "Learn how to write more Pythonic and maintainable code.",
            },
            {
                "host": users[4],  # "AI researcher exploring LLMs and NLP."
                "topics": topics[1],
                "name": "Data Science with Python",
                "desc": "Discuss pandas, NumPy, and machine learning workflows in Python.",
            },
            {
                "host": users[
                    9
                ],  # "Pythonista with a love for clean syntax and bad puns."
                "topics": topics[1],
                "name": "Async IO in Python",
                "desc": "Explore asyncio, aiohttp, and concurrency in Python.",
            },
            {
                "host": users[3],  # "DevOps engineer automating all the things."
                "topics": topics[1],
                "name": "Python for Automation",
                "desc": "Share scripts and ideas for automating daily tasks using Python.",
            },
            # Rust
            {
                "host": users[
                    13
                ],  # "Rustacean trying not to fight the borrow checker."
                "topics": topics[2],
                "name": "Rustaceans' Hub",
                "desc": "Ownership, safety, and speed: Welcome to Rust discussions.",
            },
            {
                "host": users[32],  # "Learning Rust to forget JavaScript."
                "topics": topics[2],
                "name": "Borrow Checker Battles",
                "desc": "Conquer Rust’s borrow checker and lifetime challenges.",
            },
            {
                "host": users[12],  # "Frontend by day, backend by night. Pizza always."
                "topics": topics[2],
                "name": "Zero-Cost Abstractions",
                "desc": "Talk about generics, traits, and zero-cost abstractions in Rust.",
            },
            # Django
            {
                "host": users[15],  # "Django is my spirit animal 🦄."
                "topics": topics[3],
                "name": "Django ORM Deep Dive",
                "desc": "Explore the power of Django’s ORM, views, and templates.",
            },
            {
                "host": users[
                    1
                ],  # "Backend engineer specializing in Python and Django."
                "topics": topics[3],
                "name": "DRF & APIs",
                "desc": "Discuss REST API development with Django REST Framework.",
            },
            {
                "host": users[3],  # "DevOps engineer automating all the things."
                "topics": topics[3],
                "name": "Django Signals & Middleware",
                "desc": "Advanced patterns using Django’s signals and middleware.",
            },
            {
                "host": users[20],  # "DevOps by accident, YAML by choice."
                "topics": topics[3],
                "name": "Django Deployment Tricks",
                "desc": "Troubleshoot deployment with Docker, Gunicorn, and Nginx.",
            },
            # C++
            {
                "host": users[26],  # "C++ dev surviving in a garbage-collected world."
                "topics": topics[4],
                "name": "Modern C++ (C++11/14/17/20)",
                "desc": "Explore modern C++ features like move semantics and lambdas.",
            },
            {
                "host": users[29],  # "One commit away from greatness."
                "topics": topics[4],
                "name": "Memory Management 101",
                "desc": "Talk smart pointers, RAII, and dynamic allocation.",
            },
            {
                "host": users[19],  # "🚀 Scaling apps and frying CPUs."
                "topics": topics[4],
                "name": "Real-time Systems in C++",
                "desc": "C++ for games, embedded systems, and high-performance apps.",
            },
            # Ruby on Rails
            {
                "host": users[5],  # "Coding since 12, addicted to clean code."
                "topics": topics[5],
                "name": "Convention Over Configuration",
                "desc": "Explore Rails conventions, gems, and productivity hacks.",
            },
            {
                "host": users[31],  # "Async all the things!"
                "topics": topics[5],
                "name": "ActiveRecord Wizards",
                "desc": "Migrations, associations, and querying in Rails.",
            },
            # SolidJS
            {
                "host": users[14],  # "React dev with a soft spot for SolidJS."
                "topics": topics[6],
                "name": "Reactive Systems with SolidJS",
                "desc": "Talk about fine-grained reactivity and JSX compilation.",
            },
            {
                "host": users[14],  # same user fits well
                "topics": topics[6],
                "name": "Signals vs State",
                "desc": "Explore Solid’s signal model and performance implications.",
            },
            {
                "host": users[14],
                "topics": topics[6],
                "name": "SolidJS for React Devs",
                "desc": "Compare Solid’s mental model to React’s.",
            },
            # React
            {
                "host": users[2],  # "Frontend enthusiast who loves React and Tailwind."
                "topics": topics[7],
                "name": "React Hooks HQ",
                "desc": "Discuss hooks, effects, and component lifecycles in React.",
            },
            {
                "host": users[18],  # "I dream in TypeScript."
                "topics": topics[7],
                "name": "React + TypeScript",
                "desc": "Best practices and patterns for React apps using TypeScript.",
            },
            {
                "host": users[30],  # "Tabs over spaces. Yes, I said it."
                "topics": topics[7],
                "name": "State Management Wars",
                "desc": "Redux, Zustand, Recoil, Jotai — which one and why?",
            },
            {
                "host": users[34],  # "Building side projects I’ll never deploy."
                "topics": topics[7],
                "name": "React Performance Tips",
                "desc": "Memoization, suspense, and profiling your components.",
            },
        ]

        for room_data in rooms:
            room = Room.objects.create(
                host=room_data["host"],
                topic=room_data["topics"],
                name=room_data["name"],
                description=room_data["desc"],
            )
            room.participants.add(room_data["host"])
        print("Rooms creation done!")
