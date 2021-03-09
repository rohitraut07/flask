import os
import unittest
from flask import current_app
from flask_testing import TestCase

from app.manage import fapp


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        fapp.config.from_object('app.main.config.DevelopmentConfig')
        return fapp

    def test_app_is_development(self):
        self.assertTrue(fapp.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            fapp.config[
                'SQLALCHEMY_DATABASE_URI'] == f"postgresql://{fapp.config['DATABASE_USER']}:{fapp.config['DATABASE_PASSWORD']}@{fapp.config['DATABASE_URI']}:{fapp.config['DATABASE_PORT']}/{fapp.config['DATABASE_NAME']}"
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        fapp.config.from_object('app.main.config.TestingConfig')
        return fapp

    def test_app_is_testing(self):
        self.assertTrue(fapp.config['DEBUG'])
        self.assertTrue(
            fapp.config[
                'SQLALCHEMY_DATABASE_URI'] == f"postgresql://{fapp.config['DATABASE_USER']}:{fapp.config['DATABASE_PASSWORD']}@{fapp.config['DATABASE_URI']}:{fapp.config['DATABASE_PORT']}/{fapp.config['DATABASE_NAME']}"
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        fapp.config.from_object('app.main.config.ProductionConfig')
        return fapp

    def test_app_is_production(self):
        self.assertTrue(fapp.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
