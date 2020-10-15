import os
import argparse
from pathlib import Path
from discord.ext.commands.bot import Bot
from message_bot.utils import MessageCommand, MessageCommandList

bot = Bot("!")
msg_command_list = MessageCommandList(bot)
cmd_files = os.environ.get("CMD_FILES")


def required_command_exist(fn):
    def wrapper(args):
        if not args.command_name in msg_command_list.command_files:
            raise Exception("This command name doesn't exist ...")

        fn(args)

    return wrapper


@required_command_exist
def on_remove(args):
    path = Path(cmd_files, f"{args.command_name}.md")
    os.remove(path)


@required_command_exist
def on_commit(args):
    message_cmd = MessageCommand(bot, args.command_name, to_edit=True)
    message_cmd.add_message_commmand()


def on_list(*args):
    [print(f"| {cmd_files}") for cmd_files in msg_command_list.command_files]


def on_add(args):
    message_cmd = MessageCommand(bot, args.command_name, to_edit=True)
    message_cmd.add_message_commmand()


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

add = subparsers.add_parser("add", help="add a new message command")
add.add_argument("command_name")
add.set_defaults(func=on_add)

commit = subparsers.add_parser("commit", help="commit a existing message command")
commit.add_argument("command_name")
commit.set_defaults(func=on_commit)

list_ = subparsers.add_parser("list", help="list some message command")
list_.set_defaults(func=on_list)

remove = subparsers.add_parser("remove", help="remove a existing message command")
remove.add_argument("command_name")
remove.set_defaults(func=on_remove)

args = parser.parse_args()

try:
    args.func(args)

except AttributeError:
    parser.print_help()

run_the_bot = input("Run the bot ? [N/y] ")

if run_the_bot == "y":
    msg_command_list = MessageCommandList(bot)

    for msg_command in msg_command_list.get_message_objects():
        msg_command.add_message_commmand()

    token = os.environ.get("TOKEN")

    if token is None:
        raise Exception("You need a TOKEN environnement variable.") 
    
    bot.run(token)
