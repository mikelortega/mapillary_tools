from mapillary_tools.uploader import send_videos_for_processing
import inspect


class Command:
    name = 'send_videos_for_processing'
    help = "Helper tool : Send videos for processing at Mapillary."

    def add_basic_arguments(self, parser):
        parser.add_argument(
            "--user_name", help="Mapillary user name", required=True)
        parser.add_argument(
            "--user_email", help="user email, used to create Mapillary account", default=None, required=False)
        parser.add_argument(
            "--user_password", help="password associated with the Mapillary user account", default=None, required=False)
        parser.add_argument(
            '--user_key', help='Manually specify user key', default=False, required=False)
        parser.add_argument(
            '--api_version', help='Choose which Mapillary API version to use', default=1.0, required=False)
# consider having api version as string
        parser.add_argument(
            '--skip_subfolders', help='Skip all subfolders and import only the videos in the given directory path.', action='store_true', default=False, required=False)
        parser.add_argument('--video_import_path', help='Path to a video or a directory with one or more video files.',
                            action='store', required=True)
        parser.add_argument(
            '--organization_username', help="Specify organization user name", default=None, required=False)
        parser.add_argument(
            '--organization_key', help="Specify organization key", default=None, required=False)
        parser.add_argument(
            '--private', help="Specify whether the import is private", action='store_true', default=False, required=False)
        parser.add_argument(
            '--sampling_distance', help="Specify distance between images to be used when sampling video", default=2, required=False)
        
    def add_advanced_arguments(self, parser):
        parser.add_argument(
            "--master_upload", help="Uploading on behalf of someone else. Specify end user account where images must be assigned. Internal user only", default=None, required=False)
        parser.add_argument(
            '--filter_night_time', help="Unsupported feature. Filter images taken between sunset and sunrise", action='store_true', default=False, required=False)
        
    def run(self, args):
        vars_args = vars(args)
        send_videos_for_processing(
            **({k: v for k, v in vars_args.iteritems() if k in inspect.getargspec(send_videos_for_processing).args}))
