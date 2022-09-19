"""Demo code for Lab 7 SQLAlchemy

Author: Luke Chang (xcha011@aucklanduni.ac.nz)
Date: 19/09/2022

NOTE: Tested on Python 3.9.14

Install
```
# Go to the project directory
cd lab7

python3.9 -m venv venv

# On Linux and Mac:
source ./venv/bin/activate

# On Windows
venv\Scripts\activate.bat

pip install -r requirements.txt
```
"""

import datetime
from sqlalchemy import (Column, Date, Integer, MetaData, String, Table,
                        create_engine)

engine = create_engine('sqlite:///covid-19.db')
meta = MetaData()

articles_table = Table(
    'articles',
    meta,
    Column('id', Integer, primary_key=True),
    Column('date', Date),
    Column('title', String),
    Column('first_paragraph', String),
    Column('hyperlink', String),
    Column('image_hyperlink', String),
)
connection = engine.connect()


def demo_select_all():
    """Select all rows from articles."""
    select = articles_table.select()
    # To access generated SQL SELECT query
    print('Query:\n', select)  # Same as: select.__str__()

    result = connection.execute(select)  # LegacyCursorResult object
    article_list = result.all()

    for article in article_list[:5]:
        print(article)


def demo_pagination():
    """Simulate pagination, where 2nd page shows articles with id >= 10 and < 20."""
    # Note the logic operator here
    select = articles_table.select() \
        .where((articles_table.c.id >= 10) & (articles_table.c.id < 20))
    print('Query:\n', select)

    result = connection.execute(select)  # LegacyCursorResult object
    article_list = result.all()

    for article in article_list:
        print(article)


def demo_insert(article_date, title, first_paragraph, hyperlink, image_hyperlink):
    """Insert an article."""
    insert = articles_table.insert().values(
        date=article_date,
        title=title,
        first_paragraph=first_paragraph,
        hyperlink=hyperlink,
        image_hyperlink=image_hyperlink,
    )
    print('Query:\n', insert)
    connection.execute(insert)


def demo_update(article_title='Updated title!'):
    """Update the title where id == 1."""
    update = articles_table.update() \
        .where(articles_table.c.id == 1) \
        .values(title=article_title)
    print('Query:\n', update)
    connection.execute(update)

    select = articles_table.select().where(articles_table.c.id == 1)
    result = connection.execute(select)
    print(result.all())


def demo_delete(article_id=1):
    """Delete an article with a given id."""
    delete = articles_table.delete().where(articles_table.c.id == article_id)
    print('Query:\n', delete)
    connection.execute(delete)

    select = articles_table.select().where(articles_table.c.id == article_id)
    result = connection.execute(select)
    print(result.all())


if __name__ == '__main__':
    """Uncomment the functions below one at a time."""
    # Demo 1
    demo_select_all()

    # Demo 2
    # demo_pagination()

    # Demo 3
    # NOTE:
    # - All fields in our table cannot be NULL.
    # - Be careful that you do not want to override built-in class ``date''
    # demo_insert(
    #     datetime.date(2022, 9, 19),
    #     'A new beginning',
    #     'Place holder',
    #     'https://en.wikipedia.org/wiki/Main_Page',
    #     'https://en.wikipedia.org/static/images/project-logos/enwiki.png'
    # )

    # Demo 4
    # demo_update()

    # Demo 5
    # NOTE:
    # - This function can run multiple times. It does NOT return an error, if the
    # id is not found.
    # demo_delete()
