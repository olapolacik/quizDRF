import importlib
import logging
from django.core.management.base import AppCommand

logger = logging.getLogger(__name__)

class Command(AppCommand):
    help = "Seed your Django database with fake data"

    def handle(self, *args, **options):
        # Importuj apps, której używasz w kodzie
        from django.apps import apps

        apps_to_seed = [
            app_config.name for app_config in apps.get_app_configs()
        ]

        for app in apps_to_seed:
            try:
                seeder_module = importlib.import_module(f"{app}.seeder")
                if hasattr(seeder_module, "seed"):
                    seeder_module.seed()
                    logger.info(f"Successfully seeded {app}")
                else:
                    logger.warning(f"No 'seed' function found in {app}.seeder module")
            except ImportError:
                logger.warning(f"No seeder found for {app}")
