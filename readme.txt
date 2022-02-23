To run program for read opation, type 

$ python reader_main.py read 
$ python reader_main.py read_long


To run program for write operation, type 

$ python write_main.py read
$ python write_main.py write_long



manual checkpoint


self.execute_count_query("PRAGMA journal_size_limit=0")
self.execute_count_query("PRAGMA wal_checkpoint(TRUNCATE)")