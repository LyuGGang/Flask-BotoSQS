Flask-BotoSQS: Boto_ SQS integration for Flask_
===============================================

.. _Boto: https://github.com/boto/boto
.. _Flask: https://github.com/mitsuhiko/flask

Initialize
----------

    from flask_boto_sqs import FlaskBotoSQS

    sqs = FlaskBotoSQS(app)
    
or

    sqs = FlaskBotoSQS()
    sqs.init_app(app)


Configuration
-------------

Put kwargs for FlaskBotoSQS to 'FLASK_BOTO_SQS' in your Flask configuration.

    app.config['FLASK_BOTO_SQS'] = {
        'region': 'ap-northeast-1',
        'aws_access_key_id': 'YOUR_AWS_ACCESS_KEY_ID',
        'aws_secret_access_key': 'YOUR_AWS_SECRET_ACCESS_KEY'
    }


Usage
-----

    # http://docs.pythonboto.org/en/latest/ref/sqs.html
    # http://docs.pythonboto.org/en/latest/sqs_tut.html

    q = sqs.conn.get_queue('your-queue-name')

    # write
    from boto.sqs.message import Message
    m = Message()
    m.set_body('What a lovely day!')
    q.write(m)

    # read
    m = q.read()
    res = m.get_body()
    print res
    q.delete_message(m)