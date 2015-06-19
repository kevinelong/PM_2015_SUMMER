"""
A sample StopWatch that is a demonstration of how to use classes and methods
"""


class StopWatch(object):
    """
    A stopwatch to help print out timings.
    """

    FORMAT_TYPES = ('24hr', '12hr')

    def start(self):
        self.start = time.time()

    def stop(self):
        self.end = time.time()
        print '{} seconds'.format(self.end - self.start)

    def lap(self):
        """
        Prints the amount of time that has elapsed since the stopwatch has
        started. Does not stop the timer.
        """
        print time.time() - self.start

    def print_time(self, time_int):
        """
        Given an interger of the number of seconds, print the time using the
        format_type that the user has requested
        """
        # TODO: Implement this

    def pause(self):
        """
        Stops the current timer but does not reset it.
        """
        # TODO: Implement this

    def get_current_time(self):
        """
        Return the current time (aka time.time())
        """
        return time.time()

    def is_running(self):
        """
        Returns a boolean if the stopwatch has been stopped or not
        """
        # TODO: Implement this

    def set_time_format(self, format_type):
        """
        Allows us to be able to define how we want to show the time.

        Options are things like 24hr time or 12hr time
        """
        if format_type not in self.FORMAT_TYPES:
            raise KeyError(
                '{} is not an allowable time format type, available '
                'values are: {}'.format(format_type, self.FORMAT_TYPES)
            )

        self.format_type = format_type

    def __init__(self, format_type=None):
        self.format_type = format_type
