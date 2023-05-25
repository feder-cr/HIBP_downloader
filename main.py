import logging
import logging.handlers
import os
import sys
import click

from downloader import Downloader


@click.command()
@click.option('--files_path', default='hashes', help='Specify the path where you want to save 16**5 self-updating files.')
@click.option('--quiet',is_flag=True , default=False, help='Suppress output messages')
@click.option('--process',  type=int, required=True, help='Specify the number of processes to use.')
@click.option('--thread', type=int, required=True, help='Specify the number of threads to use for each process.')
@click.option('--mode', default="sha1", help='Specify the hashing mode of file to download. Available mode: ntlm, sha1. (default: sha1)')
@click.option('--single',is_flag=True , default=False, help='If set to True, save all hashes in a single file instead of multiple files')
def main(thread, process, files_path, quiet, mode, single):
    if(single == True):
        single = "single"
    else:
        single = "multiple"
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.handlers.SysLogHandler(address = '/dev/log')]
    )
    if not os.path.exists(files_path):
        os.makedirs(files_path)
    d = Downloader(quiet, process, thread, f'{files_path}', 16**5, mode, single)
    d.start()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.exception("Fatal error:")
        sys.stderr.write(f"Fatal error: {str(e)}\n")