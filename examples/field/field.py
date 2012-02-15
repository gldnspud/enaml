#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from traits.api import HasTraits, Str, Range, on_trait_change


class Person(HasTraits):
    """ A simple class representing a person object.

    """
    first_name = Str


if __name__ == '__main__':
    import enaml
    with enaml.imports():
        from person_view import PersonView
    
    john = Person(first_name='John')
    
    view = PersonView(person=john)
    view.show()

