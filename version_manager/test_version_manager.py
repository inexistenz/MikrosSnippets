#!/usr/bin/env python3

import unittest

import version_manager


class TestVersionManager(unittest.TestCase):

    def test_init(self):
        vm = version_manager.VersionManager()
        release = vm.release()
        self.assertEqual(release, '0.0.1')

        vm = version_manager.VersionManager('1.1.0')
        release = vm.release()
        self.assertEqual(release, '1.1.0')

        with self.assertRaises(version_manager.VersionParseError,
                               msg='Could not parse version string: invalid_string'):

            version_manager.VersionManager('invalid_string')

    def test_patch(self):
        vm = version_manager.VersionManager()
        chain = vm.patch()
        release = vm.release()

        self.assertEqual(vm, chain)
        self.assertEqual(release, '0.0.2')

    def test_minor(self):
        vm = version_manager.VersionManager()
        chain = vm.minor()
        release = vm.release()

        self.assertEqual(vm, chain)
        self.assertEqual(release, '0.1.0')

    def test_major(self):
        vm = version_manager.VersionManager()
        chain = vm.patch().minor().major()
        release = vm.release()

        self.assertEqual(vm, chain)
        self.assertEqual(release, '1.0.0')

    def test_rollback(self):
        vm = version_manager.VersionManager()
        vm.major()
        release = vm.release()

        self.assertEqual(release, '1.0.0')

        chain = vm.rollback()
        release = vm.release()

        self.assertEqual(vm, chain)
        self.assertEqual(release, '0.0.1')

        with self.assertRaises(version_manager.RollbackError,
                               msg='Cannot rollback!'):
            vm.rollback()


if __name__ == '__name__':
    unittest.main()
