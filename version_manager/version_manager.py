'''VersionManager module contains VersionManager class and relevant exceptions'''

import re

# Regex used to parse a version string
VER_EXPR = re.compile(r'(?P<MAJOR>\d+).(?P<MINOR>\d+).(?P<PATCH>\d+)')

class RollbackError(Exception):
    '''Exception for rollback errors'''
    def __init__(self):
        super().__init__('Cannot rollback!')

class VersionParseError(Exception):
    '''Exception for version string parsing errors'''

    def __init__(self, version_string):
        '''Constructor. Sets the message using the invalid version string.

        :param str version_string: the problem version_string
        '''

        super().__init__('Could not parse version string: ' + version_string)

class VersionManager:
    '''VersionManager class for updating version strings and keeping track of
    previous versions'''

    def __init__(self, init_version=None):
        '''Constructor. Sets the version to 0.0.1 by default unless a version
        string is given.

        :param str init_version: a version string in the form of MAJOR.MINOR.PATCH
        '''

        self.MAJOR = 0
        self.MINOR = 0
        self.PATCH = 1
        self.version_stack = []

        if init_version is not None:
            self.parse_version(init_version)

    def major(self):
        '''Increment the major version number by 1 and set minor and patch
        numbers to 0. This function also adds the current version to the stack
        before incrementing.

        :returns: itself for chaining
        :rtype: VersionManager
        '''

        self.save_version()

        self.MAJOR += 1
        self.MINOR = 0
        self.PATCH = 0

        return self

    def minor(self):
        '''Increment the minor version number by 1 and set patch numbers to 0.
        This function also adds the current version to the stack before
        incrementing.

        :returns: itself for chaining
        :rtype: VersionManager
        '''

        self.save_version()

        self.MINOR += 1
        self.PATCH = 0

        return self

    def patch(self):
        '''Increment the patch version number by 1. This function also adds the
        current version to the stack before incrementing.

        :returns: itself for chaining
        :rtype: VersionManager
        '''

        self.save_version()

        self.PATCH += 1

        return self

    def rollback(self):
        '''Increment the patch version number by 1. This function also adds the
        current version to the stack before incrementing.

        :returns: itself for chaining
        :rtype: VersionManager
        :raises RollbackError: if there are no versions to rollback to
        '''

        if not self.version_stack:
            raise RollbackError()

        prev = self.version_stack.pop()

        self.MAJOR = prev[0]
        self.MINOR = prev[1]
        self.PATCH = prev[2]

        return self

    def release(self):
        '''Return string of the current version number.

        :returns: string of the current release
        :rtype: str
        '''

        return str(self)

    def parse_version(self, version):
        '''Parse version string using regex and set the properties for the
        VersionManager class.

        :param str version: A version string of the form MAJOR.MINOR.PATCH
        :raises VersionParseError: if version string cannot be parsed by VER_EXPR regex
        '''

        m = VER_EXPR.match(version)
        if m is None:
            raise VersionParseError(version)

        d = m.groupdict()

        self.MAJOR = int(d['MAJOR'])
        self.MINOR = int(d['MINOR'])
        self.PATCH = int(d['PATCH'])

    def save_version(self):
        '''Add a previous version to the stack as a tuple.'''

        self.version_stack.append((self.MAJOR, self.MINOR, self.PATCH))

    def __str__(self):
        '''Return string of the current version number.

        :returns: string of the current release
        :rtype: str
        '''

        return '{MAJOR}.{MINOR}.{PATCH}'.format(MAJOR=self.MAJOR,
                                                MINOR=self.MINOR,
                                                PATCH=self.PATCH)

