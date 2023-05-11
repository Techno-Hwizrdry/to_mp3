# to_mp3

This Python3 script will convert a single wav and ogg file to a mp3 file.

The powershell script will convery multiple wav and ogg files to mp3 files.

The python script runs inside a Docker container.  Thus, you will need Docker to run it.

## Disclaimer
This project is a proof of concept for testing and educational purposes.
Do not use this to violate any copyright laws.
Please check the legal regulations in your country before using it.
I do not take any responsibility for what you do with this program.

## Prerequisites
This script requires:
* Docker
* Windows Powershell (to run to_mp3.ps1)

## Setup
Once those prerequisites have been installed, git clone this repo, and cd into it.

## Usage
To convert a single file:

`docker run -v ${pwd}:/app/ to_mp3 python to_mp3.py -i <file to convert>`

To convert multiple files, via Windows Powershell:

`.\to_mp3.ps1`

For more options:

`docker run -v ${pwd}:/app/ to_mp3 python to_mp3.py -h`
