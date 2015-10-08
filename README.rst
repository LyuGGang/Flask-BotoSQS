Flask-BotoSQS: Boto3_ SQS integration for Flask_
===============================================

.. _Boto3: https://github.com/boto/boto3
.. _Flask: https://github.com/mitsuhiko/flask

Initialize
----------
::

    from flask_boto_sqs import FlaskBotoSQS
    
    flask_boto_sqs = FlaskBotoSQS(app)
    
or::

    flask_boto_sqs = FlaskBotoSQS()
    flask_boto_sqs.init_app(app)


Configuration
-------------

Put kwargs for FlaskBotoSQS to 'FLASK_BOTO_SQS' in your Flask configuration.
::

    app.config['FLASK_BOTO_SQS'] = {
        'region': 'ap-northeast-1',
        'aws_access_key_id': 'YOUR_AWS_ACCESS_KEY_ID',
        'aws_secret_access_key': 'YOUR_AWS_SECRET_ACCESS_KEY'
    }


Usage
-----
::

    # https://boto3.readthedocs.org/en/latest/guide/sqs.html

    q = flask_boto_sqs.sqs.get_queue_by_name(QueueName='your-queue-name')

    # write
    resp = q.send_message('What a lovely day!')
    print resp.get('MessageId')

    # read
    for m in q.receive_messages():
        print m.body
        m.delete()
