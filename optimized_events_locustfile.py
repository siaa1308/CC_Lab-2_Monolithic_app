from locust import HttpUser, task, between


class EventsUser(HttpUser):
    """
    Simulates a user who repeatedly views events.
    """
    
    wait_time = between(1, 2)
    base_user = "locust_user"

    @task
    def view_events(self):
        with self.client.get(
            f"/events?user={self.base_user}",
            name="/events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed with status code {response.status_code}")
