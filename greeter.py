from errbot.botplugin import BotPlugin
from errbot import botcmd
import logging

log = logging.getLogger('errbot.botplugin.Greeter')

class Greeter(BotPlugin):
    def activate(self):
        BotPlugin.activate(self)
        if 'greeting' not in self:
            self['greeting'] = "Hello, %s, welcome to the channel!  Type !help for more information."
        if 'greeted' not in self:
            self['greeted'] = []

    def was_greeted(self, username):
        pass

    def set_user(self, username, phone_number):
        users = self['users']
        users[username] = {'phone_number': phone_number}
        self['users'] = users

    @botcmd
    def greeter_set_greeting(self, message, args):
        """Set the channel greeting.  Use '%s' to put the new user's name in the greeting"""
        self['greeting'] = args

    @botcmd 
    def greet(self, message, user):
        """Greet a user"""
        self.was_greeted(user)
        return(self['greeting'] % user)

    def callback_message(self, connection, message):
        log.info(message.getBody())
