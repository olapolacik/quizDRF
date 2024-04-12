import importlib
import logging
from django.core.management.base import AppCommand
from django_seed import Seed
from django_seed.exception import SeederCommandError
import random
from .models import Quizzes, Question, Answer, Category

#uzycie logger
logger = logging.getLOgger(__name__)

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
                    # self.stdout.write(self.style.SUCCESS(f"Successfully seeded {app}"))
                    logger.info(f"Successfully seeded {app}")
                else:
                # self.stdout.write(self.style.WARNING(f"No 'seed' function found in {app}.seeder module"))
                    logger.warning(f"No 'seed' function found in {app}.seeder module")
            except ImportError:
                # self.stdout.write(self.style.WARNING(f"No seeder found for {app}"))
                logger.warning(f"No seeder found for {app}") 


