import os

import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file',
                            action='store',
                            dest='filename',
                            help='filename')

    def handle(self, *args, **options):
        if 'filename' not in options:
            raise ValueError('no filename given')

        filename = options['filename']

        print('Uploading build to linode')
        self.upload_linode(filename)
        print('Done')

    def upload_linode(self, filename):
        linode_obj_config = {
            "endpoint_url": 'https://%s' % settings.LINODE_ENDPOINT_URL_LIVE_DEPLOYMENTS,
        }

        client = boto3.client('s3', **linode_obj_config)
        client.upload_file(
            Filename=filename,
            Bucket=settings.LINODE_S3_BUCKET_LIVE_DEPLOYMENTS,
            Key=os.path.basename(filename)
        )
