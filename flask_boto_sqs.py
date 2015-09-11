# -*- coding: utf-8 -*-
"""
Boto SQS integration for Flask
by LyuGGang (https://github.com/LyuGGang/Flask-BotoSQS)
"""
import flask
import boto.sqs

class FlaskBotoSQS(object):

    def __init__(self, app=None, conf_key=None):
        """
        :type app: flask.Flask
        :parm str conf_key: Key of flask config.
        """
        self.conf_key = conf_key
        if app is not None:
            self.init_app(app, conf_key)


    def init_app(self, app, conf_key=None):
        """
        :type app: flask.Flask
        :parm str conf_key: Key of flask config.
        """
        conf_key = conf_key or self.conf_key or 'FLASK_BOTO_SQS'
        self.conf_key = conf_key
        conf = app.config[conf_key]
        if not isinstance(conf, dict):
            raise TypeError("FLASK_BOTO_SQS conf should be dict")

        close_on_teardown = conf.pop('close_on_teardown', False)
        conn = boto.sqs.connect_to_region(
            conf['region'],
            aws_access_key_id=conf['aws_access_key_id'],
            aws_secret_access_key=conf['aws_secret_access_key'])

        app.extensions.setdefault('botosqs', {})
        app.extensions['botosqs'][self] = conn

        if close_on_teardown:
            @app.teardown_appcontext
            def close_connection(exc=None):
                #TODO: close connection
                pass

    @property
    def conn(self):
        """
        :rtype: boto.sqs.connection
        """
        return flask.current_app.extensions['botosqs'][self]