
STATUS_DICT = {
    "PASSED": 1,
    "BLOCKED": 2,
    "UNTESTED": 3,
    "RETEST": 4,
    "FAILED": 5
}


class TestCase:
    def __init__(self):
        self.id = None
        self.case_id = None
        self.title = None
        self.status_id = None
        self.comment = None
        self.elapsed = None
        self.defects = None
        self.assignedto_id = None
        self.version = None
        self.custom_steps = None

    def load_test_case(self, tc_dict: dict):
        for key in tc_dict.keys():
            if key in self.__dict__ and key != 'custom_steps_separated':
                setattr(self, key, tc_dict[key])

        if not tc_dict["custom_steps_separated"] is None:
            self.custom_steps = list()
            for step in tc_dict["custom_steps_separated"]:
                self.custom_steps.append(StepResult(step["content"], step["expected"]))

        return self

    def add_tc_result(self, status_id: int, comment: str, elapsed: str = None, defects: str = None, version: str = None):
        for k,v in locals().items():
            setattr(self, k, v)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)


class StepResult:
    def __init__(self, content, expected, actual=None, status_id=None):
        self.content = content
        self.expected = expected
        self.actual = actual
        self.status_id = status_id

    def add_step_result(self, actual, status_id):
        self.actual = actual
        self.status_id = status_id
