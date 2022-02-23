from DatabaseInterface import DBInterface
import sys


DATABASE_FILE = "databases/main.db"

def main(action_arg):
    """ available commands are write and write_long """
    dbi = DBInterface(db_file=DATABASE_FILE)
    if action_arg == "write":
        dbi.write_db()
        print("A data is written in database")
        dbi.close()
    elif action_arg == "write_long":
        row_count = int(sys.argv[2])
        dbi.write_db_loop(row_count)
    else:
        print("Invalid command. ")
    
if __name__ == "__main__":
    """ to run program, write $ python writer_main.py write """
    action_arg = sys.argv[1]
    main(action_arg)
    
