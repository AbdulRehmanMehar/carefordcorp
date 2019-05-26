from wtforms import Form, IntegerField, TextAreaField, StringField, validators
from ..models import Category, Product
from wtforms.ext.sqlalchemy.fields import QuerySelectField


def get_cats():
    return Category.query


class UpdateProductForm(Form):

    title = StringField('Name', [
        validators.DataRequired(),
        validators.length(min=5, max=50)
    ], description='Surgical Knife')

    price = IntegerField('Price', [
        validators.DataRequired(),
    ], description='150 usd')

    description = TextAreaField('Description', [
        validators.DataRequired(),
        validators.length(min=100, max=1500)
    ], description='Anything about the product')

    category = QuerySelectField('Category', query_factory=get_cats, get_pk=lambda a: a.id, get_label=lambda a: a.name, allow_blank=False)

    def set_default(self, prod):
        self.title.data = prod.title
        self.price.data = prod.price
        self.category.data = prod.category
        self.description.data = prod.description
