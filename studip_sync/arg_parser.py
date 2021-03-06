import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Synchronize Stud.IP files")

    parser.add_argument("-c", "--config", type=argparse.FileType('r'), metavar="FILE",
                        default=None,
                        help="set the path to the config file (Default is "
                        "'~/.config/studip-sync/config.json')")

    parser.add_argument("-d", "--destination", nargs="?", metavar="DIR", default=None,
                        help="synchronize files to the given destination directory (If no config is present this argument implies --full)")

    parser.add_argument("-m", "--media", nargs="?", metavar="DIR", default=None,
                        help="synchronize media to the given destination directory")

    parser.add_argument("--init", action="store_true",
                        help="create new config file interactively")

    parser.add_argument("--full", action="store_true", help="downloads all courses instead of only new ones")

    parser.add_argument("--recent", action="store_true", help="only download the courses of the recent semester")

    parser.add_argument("--new", action="store_true",
                        help="use new rsync client by only downloading new files instead of bulk")


    return parser.parse_args()


ARGS = parse_args()
