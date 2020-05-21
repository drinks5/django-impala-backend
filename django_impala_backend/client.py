import os
import sys

from django.db.backends.base.client import BaseDatabaseClient


class DatabaseClient(BaseDatabaseClient):
    executable_name = 'impala-shell'

    def runshell(self):
        settings_dict = self.connection.settings_dict
        args = [self.executable_name]
        db = settings_dict['OPTIONS'].get('db', settings_dict['NAME'])
        user = settings_dict['OPTIONS'].get('user', settings_dict['USER'])
        passwd = settings_dict['OPTIONS'].get('passwd', settings_dict['PASSWORD'])
        host = settings_dict['OPTIONS'].get('host', settings_dict['HOST'])
        port = settings_dict['OPTIONS'].get('port', settings_dict['PORT'])

        if user:
            args += ["--user=%s" % user]
        if passwd:
            args += ["--password=%s" % passwd]
        if host:
            args += ["--host=%s" % host]
        if port:
            args += ["--port=%s" % port]
        if db:
            args += [db]

        if os.name == 'nt':
            sys.exit(os.system(" ".join(args)))
        else:
            os.execvp(self.executable_name, args)
