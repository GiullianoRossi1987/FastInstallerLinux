# coding = utf-8
# using namespace std


"""

"""


class PackagesBeauty(object):
    """
    Contains all the Beauty Graphics from the packages system
    """

    camps_to = ("ID", "Name", "Command Unix")


    @classmethod
    def shows_one_data(cls, data: tuple) -> str:
        """

        :param data: (cd_pack, nm_pack, command)
        :return: The string that contains the data
        """
        results = "\n"+data[1] + " -> \n"
        vl_ident_bar_r = " "*4
        results += "   |" + vl_ident_bar_r + "ID -> "+str(data[0]) + "\n"
        results += "   |" + vl_ident_bar_r + "Package Name -> "+data[1] + "\n"
        results += "   |"+ vl_ident_bar_r + "Command -> "+data[2] + "\n"
        results += "   |----->\n"
        return results

    @classmethod
    def shows_all_data(cls, query: list) -> str:
        """

        :return: The string with all the data!
        """
        rs = ""
        for item in query:
            rs += cls.shows_one_data(item)
        return rs


class GitterBeauty(object):

    """

    """

    @classmethod
    def shows_one_data(cls, data: tuple) -> str:
        """

        :param data: (cd_pack, nm_pack, command)
        :return: The string that contains the data
        """
        results = "\n"+data[1] + " -> \n"
        vl_ident_bar_r = " "*4
        results += "   |" + vl_ident_bar_r + "ID -> "+str(data[0]) + "\n"
        results += "   |" + vl_ident_bar_r + "Git Name -> "+data[1] + "\n"
        results += "   |"+ vl_ident_bar_r + "Host Link -> "+data[2] + "\n"
        results += "   |"+vl_ident_bar_r + "Remote Name -> "+data[3]+"\n"
        results += "   |"+vl_ident_bar_r + "Email User -> "+data[4]+"\n"
        results += "   |" + vl_ident_bar_r + "User Name -> " + data[5] + "\n"
        results += "   |----->\n"
        return results

    @classmethod
    def shows_all_data(cls, query: list) -> str:
        """

        :return: The string with all the data!
        """
        rs = ""
        for item in query:
            rs += cls.shows_one_data(item)
        return rs


class RepoBeuaty(object):
    """

    """

    @classmethod
    def shows_one_data(cls, data: tuple) -> str:
        """"""
        results = "\n"+data[1]+"\n"
        vl_ident = " "*4
        results += "   |"+ vl_ident + "ID => "+str(data[0]) + "\n"
        results += "   |" + vl_ident + "Repository Name => " + str(data[1]) + "\n"
        results += "   |" + vl_ident + "Host => " + str(data[2]) + "\n"
        if data[3] == 1:
            results += "   |" + vl_ident + "PPA => Yes \n"
        else:
            results += "   |" + vl_ident + "PPA => No \n"
        results += "   |----->\n"
        return results

    @classmethod
    def shows_all_data(cls, query: list) -> str:
        """

        :param query:
        :return:
        """
        rs = ""
        for item in query:
            rs += cls.shows_one_data(item)
        return rs

















