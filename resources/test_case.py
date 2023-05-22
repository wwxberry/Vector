
STATUS_DICT = {
    "PASSED": 1,
    "BLOCKED": 2,
    "UNTESTED": 3,
    "RETEST": 4,
    "FAILED": 5
}


class TestCase:
    def __init__(self):
        self._id = None
        self._case_id = None
        self._title = None
        self._status_id = None
        self._comment = None
        self._elapsed = None
        self._defects = None
        self._assigned_to_id = None
        self._version = None
        self._custom_steps = None

    def add_custom_step(self):
        self._custom_steps = StepResult("Nazwa", "Oczekiwane", "Było", STATUS_DICT["BLOCKED"])

    def print_test_case(self):
        step_res = self._custom_steps
        print(f"cont {step_res.content}, oczekiwane {step_res.expected}, rezultat {step_res.actual}, wynik {step_res.status_id}")

    def load_test_case(self, tc_dict):
        self._id = tc_dict["id"]
        self._case_id = tc_dict["case_id"]
        self._assigned_to_id = tc_dict["assignedto_id"]
        self._title = tc_dict["title"]
        if not tc_dict["custom_steps_separated"] is None:
            self._custom_steps = list()
            for step in tc_dict["custom_steps_separated"]:
                self._custom_steps.append(StepResult(step["content"], step["expected"]))
        return self


class StepResult:
    def __init__(self, content, expected, actual=None, status_id=None):
        self.content = content
        self.expected = expected
        self.actual = actual
        self.status_id = status_id

    def add_result(self, actual, status_id):
        self.actual = actual
        self.status_id = status_id
