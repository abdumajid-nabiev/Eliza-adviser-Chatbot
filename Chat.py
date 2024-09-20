import re
import random

import re
import random

class Chat:
    def __init__(self, pairs):
        # Using re.search instead of re.match for flexibility
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]

    def respond(self, user_input):
        # Iterate through pairs to find a pattern that matches part of the user input
        for (pattern, responses) in self._pairs:
            match = pattern.search(user_input)  # Using search instead of match for partial matching
            if match:
                response = random.choice(responses)
                response = self._substitute(response, match)
                return response

        return "Bunga javob bera olmayman!"  # Default response for unhandled inputs
    
    def _substitute(self, response, match):
        # Substitute placeholders in the response
        for index, group in enumerate(match.groups(), 1):
            placeholder = "%" + str(index)
            response = response.replace(placeholder, group)
        return response
