from nodeconductor.logging.loggers import EventLogger, event_logger


class OpenIDEventLogger(EventLogger):

    class Meta:
        event_types = ('auth_logged_in_with_openid',)
        event_groups = {'users': event_types}


event_logger.register('auth_openid', OpenIDEventLogger)
