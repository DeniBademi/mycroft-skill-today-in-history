# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
import requests
from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'eward'

LOGGER = getLogger(__name__)


class TodayHistorySkill(MycroftSkill):
    def __init__(self):
        super(TodayHistorySkill, self).__init__(name="TodayHistorySkill")

    def initialize(self):

        random_event_intent = IntentBuilder("RandomEventIntent"). \
            require("RandomEventKeyword").build()
        self.register_intent(random_event_intent, self.handle_random_event_intent)
    
    

        random_event_intent = IntentBuilder("CompanyEventIntent"). \
            require("CompanyEventKeyword").build()
        self.register_intent(company_event_intent, self.handle_company_event_intent)



    def handle_random_event_intent(self, message):
        url =" http://history.muffinlabs.com/date"
        r=requests.get(url)
        json_output=r.json()
        output=json_output['data']
        events=output["Events"]

        self.speak_dialog("Today in history event {} occured".format(events[0]['text']))
        
    def handle_company_event_intent(self, message):
        self.speak_dialog("# Never Settle")

    

    def stop(self):
        pass


def create_skill():
    return TodayHistorySkill()
