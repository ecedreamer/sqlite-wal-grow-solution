from DatabaseInterface import DBInterface
import sys


DATABASE_FILE = "databases/main.db"

def main(action_arg):
    """ available commands are read and read_long """
    dbi = DBInterface(db_file=DATABASE_FILE)
    if action_arg == "read":
        count = dbi.read_db()
        print(count)
        dbi.close()
    elif action_arg == "read_long":
        row_count = int(sys.argv[2])
        dbi.read_db_loop(row_count)
    else:
        print("Invalid command. ")
    
if __name__ == "__main__":
    action_arg = sys.argv[1]
    main(action_arg)