import keyring

HEADERS = {
    'Content-Type': 'application/json',
    "X-Frame-Options": "SAMEORIGIN",
    "Content-Security-Policy": "default-src 'self'",
    "Referrer-Policy": "no-referrer,strict-origin-when-cross-origin",
    "X-XSS-Protection": "1; mode=block",
    "Server": "Maor&Roy INC"
}

# Set the keyring service name
# KEYRING_SERVICE_NAME = 'wolt-servcie'

# Get the email and password from the keyring
# EMAIL = keyring.get_password(KEYRING_SERVICE_NAME, 'WoltAutomation@gmail.com')
# PASSWORD = keyring.get_password(KEYRING_SERVICE_NAME, 'ferxqoxirjiaswio')

# Create the CREDENTIALS dictionary
CREDENTIALS = {
    'EMAIL': "WoltAutomation@gmail.com",
    'PASSWORD': "ferxqoxirjiaswio"
}
