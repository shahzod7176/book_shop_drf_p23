from django.core.management import BaseCommand
from faker import Faker

from users.models import Author, Address, Country, User


class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    model_list = {'author', 'address'}

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        self.f = Faker()
        super().__init__(stdout, stderr, no_color, force_color)

    def add_arguments(self, parser):
        for model in self.model_list:
            parser.add_argument(f'--{model}', type=int, default=0)

    def _author(self, count=0):
        author_list = list()
        for _ in range(count):
            author_list.append(Author(
                first_name=self.f.first_name(),
                last_name=self.f.last_name(),
                description=self.f.text(max_nb_chars=100),
            ))
        Author.objects.bulk_create(author_list)
        self.stdout.write(self.style.SUCCESS("Author  malumotlari qoshildi"))

    def _address(self, count=0):
        address_list = list()
        for _ in range(count):
            address_list.append(Address(
                first_name=self.f.first_name(),
                last_name=self.f.last_name(),
                address_line_1=self.f.address(),
                address_line_2=self.f.address(),
                city=self.f.city(),
                state=self.f.state(),
                postal_code=self.f.postalcode(),
                phone_number=self.f.phone_number(),
                country=Country.objects.first(),
                user=User.objects.first(),
            ))
        Address.objects.bulk_create(address_list)
        self.stdout.write(self.style.SUCCESS("Address malumotlari qoshildi"))

    def handle(self, *args, **options):
        for name in self.model_list & set(options):
            getattr(self, f'_{name}')(options[name])

        self.stdout.write(self.style.SUCCESS("Barcha malumotlar qoshildi"))
