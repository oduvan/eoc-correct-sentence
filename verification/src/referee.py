from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "correct_sentence"
    FUNCTION_NAMES = {
        "python_3": "correct_sentence",
        "js_node": "correctSentence"
    }
    ENV_COVERCODE = {
        
    }