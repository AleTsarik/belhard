# 1. Написать модели SQLAlchemy к представленной структуре БД
from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pk = Column('id', INTEGER, primary_key=True)


class Statuses(Base):
    __tablename__ = 'statuses'
    name = Column(VARCHAR(10), unique=True)


class Orders(Base):
    __tablename__ = 'orders'
    user_id = Column(INTEGER, ForeignKey('users.id'))
    status_id = Column(INTEGER, ForeignKey('statuses.id'))


class Users(Base):
    __tablename__ = 'users'
    name = Column(VARCHAR(24))
    email = Column(VARCHAR(24), unique=True)


class OrderItems(Base):
    __tablename__ = 'order_items'
    order_id = Column(INTEGER, ForeignKey('orders.id'))
    product_id = Column(INTEGER, ForeignKey('products.id'))


class Products(Base):
    __tablename__ = 'products'
    title = Column(VARCHAR(36))
    description = Column(VARCHAR(140))
    category_id = Column(INTEGER, ForeignKey('categories.id'))


class Categories(Base):
    __tablename__ = 'categories'
    name = Column(VARCHAR(24), unique=True)
