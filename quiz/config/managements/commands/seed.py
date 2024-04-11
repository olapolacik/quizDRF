from django.core.management.base import AppCommand
from django_seed import Seed
from django_seed.exception import SeederCommandError
import random
from .models import Quizzes, Question, Answer, Category


class Command(AppCommand):
    help = "Seed your Django databade with fake data"

    def handle(self, *args, **options):
        apps = [
            app_config.name for app_config in apps.get_app_configs()
        ]
        for app in apps:
            try:
                seeder_module = importlib.import_module(f"{app}.seeder")
                if hasattr(seeder_module, "seed"):
                    seeder_module.seed()
                    self.stdout.write(self.style.SUCCESS(f"Successfully seeded {app}"))
                else:
                    self.stdout.write(self.style.WARNING(f"No 'seed' function found in {app}.seeder module"))
            except ImportError:
                self.stdout.write(self.style.WARNING(f"No seeder found for {app}"))

    # logger 

# from django.core.management.base import AppCommand
# from django_seed import Seed
# from django_seed.exception import SeederCommandError
# from importlib import import_module
# from django.apps import apps
# from quizzes.seed_script import generate_data   # zaimportuj funkcję generującą dane z Twojego skryptu seeder'a

# class Command(AppCommand):
#     help = "Seed your Django database with fake data"

#     def handle_app(self, app, *args, **options):
#         try:
#             seeder_module = import_module(f"{app}.seeder")
#             if hasattr(seeder_module, "seed"):
#                 seeder_module.seed()
#                 self.stdout.write(self.style.SUCCESS(f"Successfully seeded {app}"))
#             else:
#                 self.stdout.write(self.style.WARNING(f"No 'seed' function found in {app}.seeder module"))
#         except ImportError:
#             self.stdout.write(self.style.WARNING(f"No seeder found for {app}"))

#     def handle(self, *args, **options):
#         for app_config in apps.get_app_configs():
#             self.handle_app(app_config.name, *args, **options)

#     def handle_app(self, app, *args, **options):
#         try:
#             seeder_module = import_module(f"{app}.seeder")
#             if hasattr(seeder_module, "seed"):
#                 seeder_module.seed()
#                 self.stdout.write(self.style.SUCCESS(f"Successfully seeded {app}"))
#             else:
#                 self.stdout.write(self.style.WARNING(f"No 'seed' function found in {app}.seeder module"))
#         except ImportError:
#             self.stdout.write(self.style.WARNING(f"No seeder found for {app}"))

#     def handle(self, *args, **options):
#         generate_data(15)
