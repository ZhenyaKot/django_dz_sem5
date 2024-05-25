from django.core.management.base import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    help = 'Get all product'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write(f'{products}')