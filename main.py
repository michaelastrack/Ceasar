#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from ceasar import encrypt


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Ceasar</title>

</head>
<body>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        response = "<form action = '/encrypt'>"
        response += "<h2> Enter in some text to rotate </h2>"
        response += "<input type = text name = user_input/>"
        response += "<input type = submit />"
        response += "<br> <br>"
        response += "<h4> Enter in an amount to rotate the above text </h4>"
        response += "<input type = text name = rot_amount />"
        response += "</form>"
        full_response = page_header + response + page_footer
        self.response.write(full_response)

class EncryptHandler(webapp2.RequestHandler):
    def get (self):
        user_input = self.request.get("user_input")
        rotate = int(self.request.get("rot_amount"))
        answer = encrypt(user_input, rotate)

        #escape_answer = cgi.escape(answer, quote = True)
        # Does not handle spaces
        response = "<form action = '/encrypt'>"
        response += "<h2> Enter in some text to rotate </h2>"
        response += "<input type = text name = user_input value ={0} >".format(answer)
        response += "<input type = submit />"
        response += "<br> <br>"
        response += "<h4> Enter in an amount to rotate the above text </h4>"
        response += "<input type = text name = rot_amount />"
        response += "</form>"
        full_response = page_header + response + page_footer
        self.response.write(full_response)

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/encrypt', EncryptHandler)
], debug=True)
