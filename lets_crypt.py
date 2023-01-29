"""A python script that allows you to encrypt your personal files.

Usage:
======
    python lets_crypt.py [OPTIONS] [TARGET]

    OPTIONS:
    -d (or --decrypt): to decrypt the specified target.
        Be aware of using the same algorithm you used for encryption.
    -a (or --algorithm) <algo_code>: to specify the wanted algorithm for encryption.
        See 'Algo Codes' section below for possible algorithms.
    -? (TO DEFINE): needed informations to encrypt.
    -k (or --keep): keeps the original file intact and encrypts its content into a copy.
    -v (or --version): display the current version of the program.
    -h (or --help): display the possible options.

    TARGET:
      file_name: the name of the file to encrypt (or decrypt).
    | dir_name: the name of the directory to encrypt (or decrypt).

    Algo Codes:
    There are two possible types of encryption algorithms:
    - Symmetric-key algorithm:
        codes = {aes, twofish, idea}
            aes -> (TO DEFINE)
            twofish -> (TO DEFINE)
            idea -> (TO DEFINE)
    - Asymmetric-key algorithm:
        codes = {rsa, ecc}
            rsa -> (TO DEFINE)
            ecc -> (TO DEFINE)

License:
======
    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

__author__ = "Alexandre Quéré aka Ryo Deyn"
__version__ = "v1.0.0-alpha"
__license__ = "MPL-2.0 license"
__copyright__ = "Copyright (C) 2023 Alexandre Quéré"

import sys
import getopt


class TColor:
    """
    Store the different possible colors if we want to display colored text in the terminal.
    """
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    light_grey = '\033[37m'
    darkgrey = '\033[90m'
    light_red = '\033[91m'
    light_green = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    light_cyan = '\033[96m'
    end = '\033[0m'


welcome_text = ("\n=============== CryptThemAll ===============\n"
                "=========== Let's crypt everything ! ===========\n"
                "---------------------------------------------")

pain_hint = "Did you know that 'pain' means 'bread' in french ?\n"

usage_text = "Usage : lets_crypt [OPTION] [TARGET]\n"

options_text = ("OPTIONS :\n"
                "-d (or --decrypt)                  to decrypt the specified target. Be aware of using the same\n"
                "                                   algorithm you used for encryption.\n\n"
                "-a (or --algorithm) <algo_code>    to specify the wanted algorithm for encryption. See 'Algo Codes'\n"
                "                                   section below for possible algorithms.\n\n"
                "-? (TO DEFINE)                     needed informations to encrypt.\n\n"
                "-k (or --keep)                     keeps the original file intact and encrypts its content into a\n"
                "                                   copy.\n\n"
                "-v (or --version)                  display the current version of the program.\n\n"
                "-h (or --help)                     display the possible options (this menu).\n")

target_text = ("TARGET :\n"
               "file_name       the name of the file to encrypt (or decrypt).\n"
               "| dir_name      the name of the directory to encrypt (or decrypt).\n")

algo_codes_text = """
Algo Codes:
There are two possible types of encryption algorithms:
- Symmetric-key algorithm:
    codes = {aes, twofish, idea}
        aes -> (TO DEFINE)
        twofish -> (TO DEFINE)
        idea -> (TO DEFINE)
- Asymmetric-key algorithm:
    codes = {rsa, ecc}
        rsa -> (TO DEFINE)
        ecc -> (TO DEFINE)
"""

project_title = r"""
 ______  ______  __  __  ______ ______     ______ __  __  ______  __    __       ______  __      __        
/\  ___\/\  == \/\ \_\ \/\  == /\__  _\   /\__  _/\ \_\ \/\  ___\/\ "-./  \     /\  __ \/\ \    /\ \       
\ \ \___\ \  __<\ \____ \ \  _-\/_/\ \/   \/_/\ \\ \  __ \ \  __\\ \ \-./\ \    \ \  __ \ \ \___\ \ \____  
 \ \_____\ \_\ \_\/\_____\ \_\    \ \_\      \ \_\\ \_\ \_\ \_____\ \_\ \ \_\    \ \_\ \_\ \_____\ \_____\ 
  \/_____/\/_/ /_/\/_____/\/_/     \/_/       \/_/ \/_/\/_/\/_____/\/_/  \/_/     \/_/\/_/\/_____/\/_____/ 
                                                                                                  """

version_text = "CryptThemAll version 1.0.0-alpha (https://github.com/RyoDeyn/CryptThemAll)\n"

# def process_options():
#     """Manage script options and parameters."""
#
#     try:
#         couples, args_after = getopt.getopt(sys.argv[1:], "bivh", ["basic", "intelligentia", "version", "help"])
#     except getopt.GetoptError as error:
#         # Display error message :
#         print("\nError : ", error)
#         # We end the execution of the script :
#         sys.exit("Use the option -h (or --help) to view the usage and possible options.\n")
#
#     # If we run the script without any parameters or options :
#     if len(couples) == 0 and len(args_after) == 0:
#         welcome_message()
#     # If we run the script with additional parameters :
#     elif len(args_after) != 0:
#         print("\nError : pureforce do not accept additional parameters")
#         sys.exit("Use the option -h (or --help) to view the usage and possible options.\n")
#     # If we run the script with several options at the same time :
#     elif len(couples) > 1:
#         print("\nError : pureforce do not accept several options at the same time.\n"
#               "Example of correct use : python pureforce -b\n"
#               "Example of incorrect use : python pureforce -b -i\n")
#     # Case where the usage is correct :
#     else:
#         for option, value in couples:
#             if option in ("-h", "--help"):
#                 help_option()
#             elif option in ("-v", "--version"):
#                 version_option()
#             elif option in ("-b", "--basic"):
#                 basic_option()
#             elif option in ("-i", "--intelligentia"):
#                 print(f"{TColor.pink}The pain is cooking ...\n"
#                       f"(The intelligent mode is not available yet.){TColor.end}")


def main():
    """Main function."""
    #process_options()


if __name__ == '__main__':
    main()
