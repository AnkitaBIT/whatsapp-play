from googlesearch import search
def Bot(last_Message):
    print('\n Bot activated')
    first_last_Message= "".join(last_Message.split())
    simple_menu = {                                 # function requires no extra arguments
                "hi": say_hi,
                "help": _help_commands,
                "goodmorning": say_goodmorning,
                "goodnight": say_goodnight,
                "howareyou?": say_fine,
            }
    simple_menu_keys = simple_menu.keys()
    result = []

    try:
        command_args = first_last_Message[1:].split(" ", 1)
        command_arg = last_Message[1:].split(" ", 1)

        if len(command_args) == 1 and command_args[0] in simple_menu_keys:
            return simple_menu[command_args[0]]()

        elif command_arg[0] == 'google':
            query = "".join(command_arg[1])
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                result.append(j)
            print("Sending links for query")
            return result

        else:
            return "Wrong command. Send me /help to see a list of valid commands"

    except KeyError as e:
            print("Key Error Exception: {err}".format(err=str(e)))


def say_hi():
    print("Saying hi")
    return "Wplay chatbot says hi! Hope you are having a nice day..."

def say_goodmorning() :
    print("Saying good morning")
    return "Bot says Good Morning! Have a Good Day..."

def say_goodnight() :
    print("Saying good night")
    return "Bot says Good Night! Sweet Dreams..."

def say_fine() :
    print("Saying I am Fine!")
    return "Bot says I am Fine Thank You! How are you?"

def _help_commands():
        print("Asking for help")
        return "How may I assist you with help\n"\
               "List of commands:\n" \
               "/hi (bot says hi), " \
               "/all_commands (ist of all commands), " \
               "/good morning, " \
               "/good night, " \
               "/how are you?"


