from gevent import monkey
monkey.patch_all()
import multiprocessing

bind = '0.0.0.0:26666'
workers = multiprocessing.cpu_count() * 2 +1
threads = 2
worker_class = 'gevent'
worker_connections = 1000
#debug = True
#daemon = True
# 访问日志目录
accesslog = './log/access/gunicorn_access.log'
# 错误信息日志目录
errorlog = './log/error/gunicorn_error.log'
loglevel = 'warning'