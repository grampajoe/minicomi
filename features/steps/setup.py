from behave import given, when, then


@given('there\'s no admin account')
def step_impl(context):
    import django
    from django.contrib.auth import get_user_model

    django.setup()

    # Bye
    User = get_user_model()
    User.objects.all().delete()


@when(u'I go to {url:S}')
def step_impl(context, url):
    context.get_browser().get(context.base_url + url)


@when('I enter {username}, {password}, and {email}')
def step_impl(context, username, password, email):
    browser = context.get_browser()

    username_field = browser.find_element_by_name('username')
    password1_field = browser.find_element_by_name('password1')
    password2_field = browser.find_element_by_name('password2')
    email_field = browser.find_element_by_name('email')

    username_field.send_keys(username)
    password1_field.send_keys(password)
    password2_field.send_keys(password)
    email_field.send_keys(email)

    username_field.submit()


@then(u'I should be logged in as {username}')
def step_impl(context, username):
    browser = context.get_browser()
    page_text = browser.find_element_by_tag_name('body').text

    assert 'Django administration' in page_text
    assert 'Welcome, %s.' % username in page_text
