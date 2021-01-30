from locust import HttpUser, between, task


class GhostUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")
        self.client.get("/tag/getting-started/")
        self.client.get("/author/ghost/")

    @task
    def ghost(self):
        self.client.get("/ghost/")

    @task
    def about(self):
        self.client.get("/about/")
