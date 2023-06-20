## Password Hash Downloader

Welcome to the Password Hash Downloader, a powerful Python tool for downloading and saving password hash files from [an](https://haveibeenpwned.com/) API. With this application, you can obtain a large set of password hashes for analysis, security, or other purposes.

### Requirements

Before getting started, make sure you have Python 3 installed on your system. Additionally, you will need a few additional Python modules:

- `aiohttp`
- `asyncio`
- `click`

You can easily install these modules by running the following command:

```
pip install -r requirements.txt
```

### Instructions

Please follow the instructions below to use the Password Hash Downloader:

1. Clone the GitHub repository to your computer by running the command:

```
git clone https://github.com/username/password-hash-downloader.git
```

2. Navigate to the program directory:

```
cd password-hash-downloader
```

3. If you want to keep your workspace clean, you can create a virtual environment specific to the project by running the following command:

```
python -m venv env
```

4. Activate the virtual environment:

- Windows:

```
env\Scripts\activate
```

- Unix/macOS:

```
source env/bin/activate
```

5. Now you are ready to run the program! Use the following command with your preferred options:

```
python main.py --files_path <folder_path> --quiet --process <number_of_processes> --thread <number_of_threads> --mode <mode> --single
```

- `--files_path <folder_path>`: Specify the destination folder where you want to save the password hash files. If the folder does not exist, it will be created automatically.
- `--quiet`: Optional. If specified, it disables output messages during execution.
- `--process <number_of_processes>`: Specify the number of processes to use for downloading the hash files.
- `--thread <number_of_threads>`: Specify the number of threads to use for each process.
- `--mode <mode>`: Optional. Specify the hashing mode of the files to download. Available modes are "sha1" (default) and "ntlm".
- `--single`: Optional. If specified, it saves all password hashes in a single file instead of multiple files.

For example, to run the program with 2 processes, 4 threads each, saving the files in the "hashes" folder, using the "ntlm" mode, and saving all hashes in a single file, execute the following command:

```
python main.py --files_path hashes --process 2 --thread 4 --mode ntlm --single
```

6. Once you run the command, the program will start the process of downloading the password hash files from the API. The files will be saved in the specified folder. If you chose the `--quiet` option, you will not see any progress messages during execution.

7. After the download is complete, you will find the password hash files in the specified folder. You can now use them for your analysis, security purposes, or other needs.

