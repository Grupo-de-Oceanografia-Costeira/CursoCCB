__author__ = "Vini Salazar"

import os
import time
import boto3
import datetime
import subprocess

# Dont hardcode this. Use biodrive.settings
SEQS_PATH = '/Users/ubuntu/storage/seqs'
SS_PATH = '/Users/ubuntu/storage/tmp'

"""
TODO
- docstring
- SS_PATH = '/home/ubuntu/storage/tmp'
- rename samplesheets to run_id.sample_sheet.csv
example keys
seqs/2017/170601_M02526_0087_000000000-G176D.tar.gz
seqs/2017/171228_M02526_0123_000000000-G1DUB.tar.gz

mock
seqs/2017/170530_M02526_0124_000000000-I834B.tar.gz
"""


def counter(start, end, quiet=False):
    """
    A counter function to measure and print run time.
    Should be called as:

    start = time.perf_counter()
    <your code here>
    end = time.perf_counter()
    counter(start, end)
    """
    delta = datetime.timedelta(seconds=abs(start - end))
    if not quiet:
        print("Took {}.".format(delta))

    return delta


def session_variables():
    """
    Defines session_variables for the script. Should be called as:
    s3, seq_keys = session_variables()
    """
    s3 = boto3.Session(profile_name='default').client('s3')
    seq_keys = [i["Key"] for i in s3.list_objects(Bucket='neopct-bioinfo',
                                                  Delimiter='results')
                ["Contents"]]

    return s3, seq_keys


def download_file(s3, key):
    """
    'key' is an item (string) from seq_keys. This function is supposed to be
    iterated over seq_keys. Looks like this:
    'seqs/2018/181019_M02526_0180_000000000-BWF45.tar.gz'
    s3 is the boto3 session client from session_variables().

    Should be run as output_file, run_id = download_file(s3, key)
    """

    run_id = key.split('/')[-1]
    output_file = os.path.join(SEQS_PATH, run_id)

    if os.path.isfile(os.path.join(SEQS_PATH, run_id)):
        print("Your file already exists at {}.".format(output_file))
        return output_file

    else:
        if run_id[-2:] == 'gz':
            try:
                print("Downloading {}.".format(run_id))
                s3.download_file('neopct-bioinfo', key, output_file)
                print(

                    "{0} was downloaded to {1}.".format(key, output_file),
                    '\n'

                    )
                return output_file
            except ClientError as err:
                print(
                    "Your file \'{}\' could not be downloaded.".format(key),
                    '\n')
        else:
            print("{} is not a compressed gz file.".format(key))


def list_contents(output_file):
    """
    Writes contents of a tar.gz file to a text file using the tar --list cmd.
    """
    print("Listing contents from {}.".format(output_file))
    contents_file = os.path.join(

                    SS_PATH,
                    output_file.split('/')[-1].split('.')[0]+'.contents.txt'

                    )

    with open(contents_file, "w") as f:
        try:
            subprocess.call(
                ['tar', '--list', '--file={}'.format(output_file)], stdout=f
                )

            return contents_file
        except OSError:
            print("'tar' command returned with non-zero exit code.")
            raise


def extract_samplesheets(contents_file, output_file):
    """
    This function reads the contents_files, and calls the tar command to
    extract only files ending in .csv (SampleSheets) from the output_file.
    It also moves them to the correct SS_PATH directory.
    """
    print("Extracting samplesheets from {}.".format(contents_file))
    run_id = output_file.split('/')[-1].split('.')[0]

    with open(contents_file, 'r') as fh:
        r = fh.readlines()
        r = [i.strip('\n') for i in r if i.strip('\n')[-3:] == 'csv']
        r = [i for i in r if len(i.split('/')) < 4]

    print("SampleSheets in {}:".format(output_file), '\n')
    [print('\t', i, '\n') for i in r]

    for ss in r:
        try:
            subprocess.call(['tar', '-zxf', output_file, '-C', SS_PATH, ss])
        except OSError:
            print("Couldn't extract {0} from {1}.".format(ss, output_file))
            pass


if __name__ == "__main__":
    now = str(datetime.datetime.now())
    print("Starting script at {}".format(now), '\n')
    monday = time.perf_counter()

    s3, seq_keys = session_variables()

    seq_keys = ['seqs/2017/170601_M02526_0087_000000000-G176D.tar.gz',
                'seqs/2017/171228_M02526_0123_000000000-G1DUB.tar.gz',
                'seqs/2017/170530_M02526_0124_000000000-I834B.tar.gz']

    for key in seq_keys:
        start = time.perf_counter()
        output_file = download_file(s3, key)
        contents_file = list_contents(output_file)
        extract_samplesheets(contents_file, output_file)
        end = time.perf_counter()
        counter(start, end)
        print('\n')

    now = str(datetime.datetime.now())
    print("All done at {}".format(now))

    friday = time.perf_counter()
    counter(monday, friday)
