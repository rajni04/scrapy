# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class QuotetPipeline:
    #For database connection
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=sqlite3.connect("myquotet.db")
        self.curr=self.conn.cursor()

    #For creating table
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotet_tb""")
        self.curr.execute("""create table quotet_tb(title text,
                          author text,
                          tag text)""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotet_tb values(?,?,?)""",(
            item['title'][0],item['author'][0], item['tag'][0]
        ))
        self.conn.commit()