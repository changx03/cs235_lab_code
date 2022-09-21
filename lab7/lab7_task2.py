"""Startup code for Lab 7 SQLAlchemy  Task 2

This code provides the minimal boilerplate for SQLAlchemy ORM.
It is based on [ORM Quick Start](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)

Feel free to add additional functions if necessary.

Author: Luke Chang (xcha011@aucklanduni.ac.nz)
Date: 21/09/2022

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

from sqlalchemy import Column, Date, Integer, String, create_engine, select
from sqlalchemy.orm import Session, declarative_base

# Set echo to True, so we know what is running behind the scene.
engine = create_engine('sqlite:///covid-19.db', echo=True)
session = Session(engine)

# To make the code as short as possible, we use the base model implemented by 
# sqlalchemy.orm
Base = declarative_base()


class Article(Base):
    __tablename__ = 'articles'

    id = Column('id', Integer, primary_key=True)
    date = Column('date', Date)
    title = Column('title', String)
    first_paragraph = Column('first_paragraph', String)
    hyperlink = Column('hyperlink', String)
    image_hyperlink = Column('image_hyperlink', String)

    def __repr__(self):
        # NOTE: ``!r'' is for converting the value to a string using repr().
        return f'{self.id!r}. [{self.title!r}]({self.hyperlink!r})'


def search_article(keyword, session=session):
    """Search the title by the keyword and then return a list of Article objects.
    NOTE: The keyword is not case sensitive.
    """
    # "stmt" is the abbreviation for "Statement"
    stmt = select(Article).where(Article.title.contains(keyword))
    results = session.execute(stmt).all()
    return results

def get_article_by_id(article_id, session=session):
    # TODO: Add your code here
    article = None
    return article

class Comment(Base):
    __tablename__ = 'comments'
    # TODO: Complete this class

def get_comment_by_id(comment_id, session=session):
    # TODO: Add your code here
    comment = None
    return comment

def get_comment_by_user(user_name, session=session):
    """Join users and comments table, and use user_name to filter comments
    NOTE: You need to create the User class first!
    """
    # TODO: Add your code here
    comment = None
    return comment

def delete_comment(comment_id, session=session):
    # TODO: Add your code here
    pass

def update_comment(comment_id, comment):
    # TODO: Add your code here
    # This function should return the updated comment.
    # Note that you also want to update the timestamp with current time. 
    # (Use the `datetime` library)
    comment = None
    return comment

if __name__ == '__main__':
    articles = search_article('australia')
    for article in articles:
        print(article)

    # TODO: Test your code here.
