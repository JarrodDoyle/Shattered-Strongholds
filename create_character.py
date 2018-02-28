from bearlibterminal import terminal
from ui import Generic_Text_Window
import components.fighter as fighter
import re

class Character_Creation:
    def choose_name(self):
        name = ""
        menu = Generic_Text_Window(1, 1, 94, 62, "Character Creation")
        invalid_text = ""
        while True:
            terminal.clear()
            text = "Please enter your name:\n{}\n{}".format(name, invalid_text)
            menu.render(text)
            terminal.refresh()
            invalid_text = ""
            key = terminal.read()

            if (key == terminal.TK_RETURN or key == terminal.TK_ESCAPE):
                if re.match("^[A-Za-z]+$", name) and len(name) > 0:
                    break
                else:
                    invalid_text = "That name is not valid."
            elif key == terminal.TK_BACKSPACE and len(name) > 0:
                name = name[:-1]
            elif terminal.check(terminal.TK_CHAR) and len(name) < 8:
                name += chr(terminal.state(terminal.TK_CHAR))
        return name

    def choose_class(self):
        menu = Generic_Text_Window(1, 1, 94, 62, "Character Creation")
        classes = [fighter.Barbarian, fighter.Wizard, fighter.Rogue, fighter.Ranger]
        text = "Please select a class:\n a) Barbarian:\n{}\n[color=black]█[\color]\n b) Wizard:\n{}\n[color=black]█[\color]\n c) Rogue:\n{}\n[color=black]█[\color]\n d) Ranger:\n{}".format(classes[0].description, classes[1].description, classes[2].description, classes[3].description)
        menu.render(text)
        terminal.refresh()
        valid_choice = False
        while not valid_choice:
            key = terminal.read()
            if key - terminal.TK_A in range(len(classes)):
                valid_choice = True
                choice = key - terminal.TK_A
        return classes[choice]()
