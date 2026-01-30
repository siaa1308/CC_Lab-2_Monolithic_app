from locust import HttpUser, task, between


class EventsComparisonUser(HttpUser):
    """
    User that hits both /events and /my-events
    so their RPS and avg response time can be compared.
    """

    wait_time = between(1, 2)
    base_user = "locust_user"

    @task(1)
    def view_events(self):
        with self.client.get(
            f"/events?user={self.base_user}",
            name="/events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"/events failed: {response.status_code}")

    @task(1)
    def view_my_events(self):
        with self.client.get(
            f"/my-events?user={self.base_user}",
            name="/my-events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"/my-events failed: {response.status_code}")
