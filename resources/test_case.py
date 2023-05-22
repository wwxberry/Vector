
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
        self._comment = None
        self._elapsed = None
        self._defects = None
        self._assigned_to_id = None
        self._version = None
        self._custom_steps = None

    def add_custom_step(self):
        self._custom_steps = self.StepResult("Nazwa", "Oczekiwane", "Było", STATUS_DICT["BLOCKED"])

    def print_test_case(self):
        step_res = self._custom_steps
        print(f"cont {step_res.content}, oczekiwane {step_res.expected}, rezultat {step_res.actual}, wynik {step_res.status_id}")

    class StepResult:
        def __init__(self, content, expected, actual, status_id):
            self.content = content
            self.expected = expected
            self.actual = actual
            self.status_id = status_id


tc = TestCase()
tc.add_custom_step()
tc.print_test_case()
