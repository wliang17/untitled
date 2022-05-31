

#安装包
from loguru import logger
logger.add('a.log',format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
logger.info('这是一条info日志')
logger.debug('这是一条debug日志')
logger.warning('这是一条warning日志')
logger.success('这是一条success日志')
logger.error('这是一条error日志')
logger.error('这是一条{}日志'.format('error'))