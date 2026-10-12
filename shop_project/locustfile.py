
from faker import Faker
from locust import HttpUser, task, TaskSet, constant_throughput

fake = Faker('fr_FR')


class AdminTests(TaskSet):

    @task(5)
    def get_categories(self):
        self.client.get('/api/categories/')

    @task(5)
    def get_collections(self):
        self.client.get('/api/collections/')

    @task(5)
    def get_artists(self):
        self.client.get('/api/artists/')

    @task(5)
    def get_labels(self):
        self.client.get('/api/labels/')

    @task(5)
    def get_genres(self):
        self.client.get('/api/genres/')

    @task(1)
    def add_category(self):
        category_data = {
            'name': fake.unique.word().capitalize(),
            'description': fake.text(max_nb_chars=100)
        }

        self.client.post('/api/categories/', json=category_data)

    @task(1)
    def add_artist(self):
        artist_data = {
            'name': fake.name(),
            'description': fake.text(max_nb_chars=100),
            'country': fake.country()
        }

        self.client.post('/api/artists/', json=artist_data)


class WebsiteUser(HttpUser):
    wait_time = constant_throughput(2)
    tasks = [AdminTests]
