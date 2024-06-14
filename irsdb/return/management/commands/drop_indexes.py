from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = """
    remove all filings from a given year by object id. This is faster if indexes are created already.
    """

    def handle(self, *args, **options):
        self.cursor = connection.cursor()

        all_tables = connection.introspection.table_names()
        for table in all_tables:
            if table.startswith("return"):
                index_name = "xx_%s" % table
                query = "drop index if exists %s" % (index_name)
                print("Running query: '%s' " % query)
                self.cursor.execute(query)
