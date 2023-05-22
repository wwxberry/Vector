from utils.TestRailConnector import TestRailConnector

TRConn = TestRailConnector()


def get_tcs_list():
    return TRConn.get_test_cases_list_from_run("2")
