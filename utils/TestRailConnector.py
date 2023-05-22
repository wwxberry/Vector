from utils.testrail import *
import json


class TestRailConnector:
    def __init__(self):
        self._base_url = "https://xberry.testrail.io"
        self._user = "{YOUR_EMAIL}"
        self._password = "{YOUR_PASSWORD}"
        self._client = None
        self.init_client()

    def init_client(self):
        if not isinstance(self._client, APIClient):
            self._client = APIClient(self._base_url)
            self._client.user = self._user
            self._client.password = self._password

    def get_test_case(self, id : str) -> str:
        self.init_client()
        return self._client.send_get("get_test/" + id)

    def get_test_cases_list_from_run(self, run_id : str) -> str:
        self.init_client()
        data = self._client.send_get("get_tests/" + run_id)

        return data["tests"]

    # TODO below methods are still under development to be finished after designing and developing TestCase class
    #
    # def add_result(self, test_id : int, status_id : int, comment : str, defects : str, assigned_to : str ):
    #     self.init_client()
    #     try:
    #         data = self._client.send_post(f"add_result/{test_id}", TestCaseObject )
    #     except Exception as e:
    #         print("Sending results to TestRail failed with error: {}".format(e.args))
    #
    #
    # def add_results(self, run_id):
    #     self.init_client()
    #     try:
    #         data = self._client.send_post(f"add_result/{test_id}", TestCasesObjectsList )
    #     except Exception as e:
    #         print("Sending results to TestRail failed with error: {}".format(e.args))
    