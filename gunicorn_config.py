from os import environ
import multiprocessing

PORT = int(environ.get("PORT", 8080))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()