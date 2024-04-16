import smtplib

# SMTP => Simple Mail Transfer Protocol
# TLS = Transport Layer Security

my_email = "pythonrohan2@gmail.com"
password = "123abcd()"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="rohanmovaliya@gmail.com",
    msg="Subject:Hello \n\n This is the body of my email.",
)
connection.close()

# We can also write above code as
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="rohanmovaliya@gmail.com",
#         msg="Subject:Hello \n\n This is the body of my email."
#     )


# Errors Solution Check Criteria
# 1) Network Connectivity
