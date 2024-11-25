import os
import time


class FileUtils:
    """A class to work with files in the OS"""

    @staticmethod
    def get_downloads_folder():
        """Returns the path to the Downloads folder based on the OS."""
        # For Windows
        if os.name == 'nt':
            return os.path.join(os.environ['USERPROFILE'], 'Downloads')
        # For macOS and Linux
        elif os.name == 'posix':
            return os.path.join(os.path.expanduser('~'), 'Downloads')
        else:
            raise OSError("Unsupported operating system")

    @staticmethod
    def wait_for_file_download(file_name: str, timeout: int = 10) -> bool:
        """Waits for a file to be downloaded to the Downloads folder.
        Returns True if the file is downloaded, False otherwise.

        :param file_name: Name of the file to wait for.
        :param timeout: Time to wait in seconds. Default is 30 seconds.
        """
        downloads_path = FileUtils.get_downloads_folder()
        file_path = os.path.join(downloads_path, file_name)
        start_time = time.time()
        while time.time() - start_time <= timeout:
            if os.path.isfile(file_path):
                return True
            time.sleep(1)
        return False
