
class Goal(object):
    def __init__ (self):
        # Create the list of steps required
        self._steps = []

    def add_step(self, step):
        pass

    def start(self):
        print(f'Steps count: {len(self._steps)}')
        if len(self._steps) == 0:
            raise GoalException(ERR_NO_STEPS, f'No steps created for goal: {self}')
            

'''
    Goal Object Error codes
'''
ERR_SUCCESS  = 0
ERR_FAIL     = 1
ERR_NO_STEPS = 2

class GoalException(Exception):
    def __init__(self, error_code, message):
        super().__init__()
        self._error_code = error_code
        self._message = message


if __name__ == '__main__':
    g = Goal()
    try:
        g.start()
        x = 1
    except GoalException as e:
        print(f'ERROR: {e._error_code}\t{e._message}')
