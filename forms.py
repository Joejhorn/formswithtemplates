from flask_wtf import Flaskform
from wtforms import StringField, IntegerField, SumbitField


class Addform(Flaskform):

  name = StringField('Name of Puppy: ')
  submit = SumbitField('Add Puppy')


class DelForm(Flaskform):

  id = IntegerField("id number of Puppy to Remove")
  submit = SumbitField('Remove Puppy')
