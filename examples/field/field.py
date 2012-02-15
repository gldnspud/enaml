#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from traits.api import HasTraits, Unicode


class Person(HasTraits):
    """ A simple class representing a person object.

    """
    first_name = Unicode


if __name__ == '__main__':
    import enaml
    with enaml.imports():
        from person_view import PersonView
    
    # Testing that Unicode strings work fine.
    adele = Person(first_name=u'Ad\N{LATIN SMALL LETTER E WITH GRAVE}le')
    
    view = PersonView(person=adele)
    view.show()

