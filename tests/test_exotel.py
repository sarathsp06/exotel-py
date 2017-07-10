# -*- coding: utf-8 -*-


from exotel import Exotel


def test_sms(mock_http):
    mock_http.register_uri(
        'POST',
        'https://twilix.exotel.in/v1/Accounts/123/Sms/send.json',
        text=''.join((
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<TwilioResponse>',
            '<SMSMessage>...</SMSMessage>',
            '</TwilioResponse>',
        )),
    )
    e = Exotel(sid='123', token='abc')
    rep = e.sms(
        from_number='012-345-6789',
        to='345-678-9012',
        body='Hello, world!',
    )
    assert rep.status_code == 200


def test_call_flow(mock_http):
    mock_http.register_uri(
        'POST',
        'https://twilix.exotel.in/v1/Accounts/123/Calls/connect.json',
        text=''.join((
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<TwilioResponse>',
            '<Call>...</Call>',
            '</TwilioResponse>',
        )),
    )
    e = Exotel(sid='123', token='abc')
    rep = e.call_flow(
        from_number='012-345-6789',
        caller_id='345-678-9012',
        flow_id='345',
    )
    assert rep.status_code == 200


def test_call_number(mock_http):
    mock_http.register_uri(
        'POST',
        'https://twilix.exotel.in/v1/Accounts/123/Calls/connect.json',
        text=''.join((
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<TwilioResponse>',
            '<Call>...</Call>',
            '</TwilioResponse>',
        )),
    )
    e = Exotel(sid='123', token='abc')
    rep = e.call_number(
        from_number='012-345-6789',
        to='345-678-9012',
        caller_id='678-901-2345',
    )
    assert rep.status_code == 200


def test_call_details(mock_http):
    mock_http.register_uri(
        'GET',
        'https://twilix.exotel.in/v1/Accounts/123/Calls/234.json',
        text=''.join((
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<TwilioResponse>',
            '<Call>...</Call>',
            '</TwilioResponse>',
        )),
    )
    e = Exotel(sid='123', token='abc')
    rep = e.call_details(call_sid='234')
    assert rep.status_code == 200


def test_sms_details(mock_http):
    mock_http.register_uri(
        'GET',
        'https://twilix.exotel.in/v1/Accounts/123/Sms/Messages/234.json',
        text=''.join((
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<TwilioResponse>',
            '<Call>...</Call>',
            '</TwilioResponse>',
        )),
    )
    e = Exotel(sid='123', token='abc')
    rep = e.sms_details(sms_sid='234')
    assert rep.status_code == 200
