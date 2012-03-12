#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from wpyf.application import Application
from ...components.abstract_application import AbstractTkApplication

class WPFApplication(AbstractTkApplication):
    """ A WPF implementation of AbstractTkApplication.

    """
    def initialize(self, *args, **kwargs):
        """ Initializes the underlying wpyf Application object. It does
        *not* start the event loop. If the application object is already
        created, it is a no-op.

        """
        app = getattr(self, '_wpf_app', None)
        if app is None:
           self._wpf_app = Application()

    def start_event_loop(self):
        """ Starts the underlying application object's event loop, or
        does nothing if it is already started. A RuntimeError will be
        raised if the application object is not yet created.

        """
        app = getattr(self, '_wpf_app', None)
        if app is None:
            msg = 'Cannot start event loop. Application object not created.'
            raise RuntimeError(msg)

        if not getattr(app, '_in_event_loop', False):
            self._in_event_loop = True
            app.Run()
            self._in_event_loop = False

    def event_loop_running(self):
        """ Returns True if the main event loop is running, False
        otherwise.

        """
        return getattr(self, '_in_event_loop', False)

    def app_object(self):
        """ Returns the underlying application object, or None if one
        does not exist.

        """
        return getattr(self, '_wpf_app', None)


    def is_main_thread(self):
        """ Return True if this method was called from the main event
        thread, False otherwise.

        """
        # FIXME: Wpyf is never running in the main thread. We need to
        # rethink the semantics.
        return True

    def call_on_main(self, callback, *args, **kwargs):
        """ Invoke the given callable in the main gui event thread at
        some point in the future.

        Parameters
        ----------
        callback : callable
            The callable object to execute at some point in the future.

        *args
            Any positional arguments to pass to the callback.

        **kwargs
            Any keyword arguments to pass to the callback.

        """
        #DeferredCaller.enqueue(callback, *args, **kwargs)
        pass

    def timer(self, ms, callback, *args, **kwargs):
        """ Invoke the given callable in the main gui event thread at
        the given number of milliseconds in the future.

        Parameters
        ----------
        ms : int
            The number of milliseconds in the future to invoke the
            callable.

        callback : callable
            The callable object to execute at some point in the future.

        *args :
            Any positional arguments to pass to the callback.

        **kwargs :
            Any keyword arguments to pass to the callback.

        """
        pass

    def process_events(self):
        """ Process all of the pending events in the event queue.

        """
        pass

