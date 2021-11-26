from aiogram.utils.helper import Helper, HelperMode, Item
class TestStates(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_LOGIN = Item()
    TEST_STATE_PASSWORD = Item()
    TEST_STATE_IN = Item()
    TEST_STATE_ACC = Item()
