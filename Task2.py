def shadow_mail(email):
    if '@' not in email:
        return 'Это не емейл, алё!'
    a_index = email.find('@')
    a = '***@**'
    return email[:a_index - 5] + a + email[a_index + 5:]


print(shadow_mail('somebody_email@gmail.com'))
