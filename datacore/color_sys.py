# coding = utf-8
# using namespace std


class LoadInColor(object):
    """

    """

    # thanks to Raccoon Ninja: https://raccoon.ninja
    _colors = {
        "red": "\033[1;31m",
        "blue": "\033[1;34m",
        "green": "\033[1;32m",
        "black": "\033[1;30m",
        "reset": "\033[0;0m",
        "yellow": "\033[1;33m",
        "purple": "\033[1;35m"
    }

    def set_with_color(self, msg: str, color: str, new_line=False) -> str:
        """
        Return a string with the choose color
        :param msg: The string
        :param color: The new color, only the keys from self._colors
        :param new_line: if the system will add a new line ('\n') to the string. default False
        :type msg: str
        :type color: str
        :type new_line: bool
        :return: The colored string!
        """
        result = self._colors[color] + msg + self._colors["reset"]
        if new_line:
            result += "\n"
        return result

