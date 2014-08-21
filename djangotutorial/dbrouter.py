class EnvironmentRouter(object):

    def db_for_read(self, model, **hints):
        return 'dev'

    def db_for_write(self, model, **hints):
        return 'dev'

    def allow_relation(self, obj1, obj2, **hints):
        return 'dev'

    def allow_migrate(self, db, model):
        return 'dev'
