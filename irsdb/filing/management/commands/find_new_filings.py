import csv
import os
from os.path import isfile, join

from django.core.management.base import BaseCommand
from irsx.settings import WORKING_DIRECTORY

from irsdb.filing.models import Filing


class Command(BaseCommand):
    help = """
    Read the yearly csv file line by line and add new lines if
    they don't exist. Lines are added in bulk at the end.
    """

    def get_writer(self, headers):
        outfilehandle = open("results.csv", "w")
        dw = csv.DictWriter(outfilehandle, headers, extrasaction="ignore")
        dw.writeheader()
        return dw

    def handle(self, *args, **options):
        print("reviewing findings in %s dir" % WORKING_DIRECTORY)
        headers = [
            "object_id",
        ]
        writer = self.get_writer(headers)

        onlyfiles = [
            f
            for f in os.listdir(WORKING_DIRECTORY)
            if isfile(join(WORKING_DIRECTORY, f))
        ]
        num_found = 0
        found_files = {}

        for file in onlyfiles:

            return_id = file.replace("_public.xml", "")

            try:
                Filing.objects.get(object_id=return_id)
            except Filing.DoesNotExist:
                writer.writerow({"object_id": return_id})
            except Filing.MultipleObjectsReturned:
                print("Multiple objects returned for %s " % return_id)

                num_found += 1
        print(found_files)
        print("Found a total of %s filings not entered" % num_found)
