class TestopiaTestRun(object):

    def __init__(self, testopia):
        self.testopia = testopia

    def get_testrun_list(self, test_plan_id, summary_name, environment_id=None):
        if environment_id:
            testruns = self.testopia.testrun_list(plan_id=test_plan_id, summary=summary_name, environment_id=environment_id)
        else:
            testruns = self.testopia.testrun_list(plan_id=test_plan_id, summary=summary_name)
        return testruns

    def _check_if_testrun_exist(self, testplan_id, summary_name, environment_id):
        tr = self.get_testrun_list(testplan_id, summary_name, environment_id)
        if tr:
            return True
        else:
            return False

    def create_testrun(self, build_id, environment_id, testplan_id, summary, manager_id, product_version, logger=None):
        if self._check_if_testrun_exist(testplan_id, summary, environment_id):
            if logger:
                logger.info('%s does exist. Skipped the creation step.' % summary)
            return None
        else:
            if logger:
                logger.info('%s does not exist, attempt to create now.' % summary)
            return self.testopia.testrun_create(build_id, environment_id, testplan_id, summary, manager_id, product_version=product_version)

    def get_testcase_ids(self, testrun_id):
        tcs = self.testopia.testrun_get_test_cases(testrun_id)
        return [tc['case_id'] for tc in tcs]

    def add_testcases_to_testrun(self, testcase_ids, testrun_id):
        self.testopia.testrun_add_cases(testcase_ids, testrun_id)
