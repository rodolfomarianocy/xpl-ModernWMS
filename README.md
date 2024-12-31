# xpl-ModernWMS
It is possible to view the MD5 hash of the admin password and other attributes without authentication, even after initial setup and password change. This is due to excessive information exposure, lack of session management, and inadequate access control on the /user/list?culture=en-us endpoint.
