import subprocess
from os import path, listdir, environ
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from .env_var import get_env_var


class Message:
    """ Represent a simple message as string returned by the bot """

    def __init__(self, message=None):
        self.body = message

    def __str__(self):
        return self.body

    def __call__(self):
        async def callback(ctx):
            await ctx.send(self.body)

        return callback


class MessageCommandList:
    """ TODO """

    def __init__(self, bot):
        self.bot = bot
        self.command_files = []
        cmd_files = get_env_var("CMD_FILES")

        for filename in listdir(cmd_files):
            if filename.endswith(".md"):
                filename_without_extension = filename.split(".")[0]
                self.command_files.append(filename_without_extension)

    def get_message_objects(self):
        for command_name in self.command_files:
            yield MessageCommand(self.bot, command_name, to_edit=False)


class MessageCommand:
    def __init__(self, bot: Bot, name: str, to_edit=False):
        self.bot = bot
        self.name = name
        self.path = environ.get("CMD_FILES") + name + ".md"
        self.message = Message()
        self._set_message_from_command_file(open_vim=to_edit)

    def _read_command_file(self):
        with open(self.path, "r") as _file:
            return _file.read()

    def add_message_commmand(self):
        """
        Simply reproduce this :


        @bot.command()
        async def ping(ctx):
            await ctx.send('pong')
        """

        self.bot.command(name=self.name)(self.message())

    def _set_message_from_command_file(self, open_vim: bool):
        """
        Set a message by writing this on a file.
        We can open vim to do this or juste read
        the file without modifications.
        """
        if open_vim:
            subprocess.call(["vi", self.path])

        self.message.body = self._read_command_file()
