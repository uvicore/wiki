from uvicore import app, config, http
from uvicore.http import APIRouter as API
from uvicore.http import controller

# New router for this controller
route = API().router

# Class based Controller
@controller(route)
class Home:

    @route.get('/')
    def home(self):
        return self.get_home()

    def get_home(self):
        return {
            'Page': 'Home',
            'Config': config(),
        }

