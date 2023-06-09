<div align="center">
    <h1 align="center">
        <image src="assets/MusBleep.png" height="300px">
    </h1>

[![Issues](https://img.shields.io/github/issues/0RaMsY0/MusBleep?style=for-the-badge)](https://github.com/0RaMsY0/MusBleep/issues)
[![License](https://img.shields.io/github/license/0RaMsY0/MusBleep?color=brightgreen&style=for-the-badge)](https://github.com/0RaMsY0/MusBleep/blob/main/LICENSE)
[![Downloads](https://img.shields.io/github/downloads/0RaMsY0/MusBleep/total?style=for-the-badge)]()

</div>

# Getting started

MusBleep is a self-hosted application that makes it easy to censor explicit content in music tracks. Our application is designed for everyone who wants to enjoy their favorite music without being exposed to explicit content. The application relies on [Whisper](https://github.com/linto-ai/whisper-timestamped) to analyze the audio, and [FastAPI](https://github.com/tiangolo/fastapi) to provide a RESTful API for communication between the front-end and back-end. MusBleep also offers different types of Whisper models for users to choose from depending on their computational resources.

To get started with MusBleep, you'll need to install it on your own server or local machine. Our application relies on [Pynecone](https://github.com/pynecone-io/pynecone), [Whisper](https://github.com/linto-ai/whisper-timestamped), and [FastAPI](https://github.com/tiangolo/fastapi), so make sure you have those installed before you begin.

We've included detailed instructions on how to install and use our application in the sections below. If you have any questions or need further assistance, please don't hesitate to reach out to our team. We're always happy to help!

# Installation and configuration

Musbleep requires the following to get started:

* Python 3.10+ - programming language used to build the application
* Pynecone - library used for building the Front-End
* FastAPI - web framework used to build the API
* whisper-timestamped - library used for converting audio to text
* ffmpeg - for audio manipulation
* Linux OS (Ubuntu, Kali Linux, Arch) - operating system required to run the application

you can run the setup script located at ```MusBleep/scripts/setup.py``` to automaticly download everything that you will need.

```bash
$ python MusBleep/scripts/setup.py setup
```

> **_Note_**: It may takes some time depending on your internet speed

here are the commands that will be executed by the setup script:
```bash
# Installing python libs
$ pip install fastapi
$ pip install uvicorn
$ pip install pynecone
$ pip install rich
$ pip install git+https://github.com/linto-ai/whisper-timestamped

# Installing bun
$ curl -fsSL https://bun.sh/install | bash

# Installing nodejs 
$ curl -fsSL "https://deb.nodesource.com/setup_19.x" | sudo bash -

# Installing ffmpeg
$ git clone https://git.ffmpeg.org/ffmpeg.git ~/ffmpeg && cd ~/ffmpeg && ./configure && make && make install
```

* ## API configue

you may need to change some values in the API configue located at ```MusBleep/api/conf/api-conf.json```, currentlly the default configuration is:
```json
{
    "port": 9090,
    "whisper_model_type": "small",
    "curse_words": [
        "ZnVjaw==", 
        "Yml0Y2g=", 
        "Yml0Y2hlcw==", 
        "c2hpdA==", 
        "ZGFtbg==", 
        "YXNz", 
        "cHVzc3k=",
        "bmlnZ2E=",
        "d2hvcmU=",
        "ZGljaw==",
        "Y29jaw==",
        "YXJzZQ==",
        "YXJzZWhlYWQ=",
        "YXJzZWhvbGU=",
        "YXNz",
        "YXNzaG9sZQ==",
        "YmFzdGFyZA==",
        "Ymxvb2R5",
        "Ym9sbG9ja3M=",
        "YnJvdGhlcmZ1Y2tlcg==",
        "YnVnZ2Vy",
        "YnVsbHNoaXQ=",
        "Y29ja3N1Y2tlcg==",
        "Y3JhcA==",
        "Y3VudA==",
        "ZGFtbiBpdA==", 
        "ZGlja2hlYWQ=", 
        "ZHlrZQ==", 
        "ZmF0aGVyZnVja2Vy", 
        "ZnJpZ2dlcg==", 
        "Z29kZGFtbg==", 
        "Z29kc2RhbW4=", 
        "aGVsbA==", 
        "aG9seSBzaGl0", 
        "aG9yc2VzaGl0", 
        "a2lrZQ==", 
        "bW90aGVyZnVja2Vy", 
        "bmlncmE=", 
        "cGlzcw==", 
        "cHJpY2s=", 
        "c2hpdGU=", 
        "c2lzdGVyZnVja2Vy",
        "c2x1dA==",
        "c3Bhc3RpYw==", 
        "dHVyZA==", 
        "ZnVja2luZw==", 
        "aG9l", 
        "ZioqKmluZw==", 
        "cG9ybg==", 
        "cG9ybmh1Yg==", 
        "Ym9vYnM=", 
        "YnJlYXN0cw==", 
        "YnJlYXN0", 
        "dGlkZGllcw==", 
        "dGlkZHk=", 
        "c3RyaXBlcg=="
    ]
}
```
here we manly going to focus on the ```whisper_model_type``` you can see all the diffrent types of the whisper model in the following table:

|   Size  | parameters | English-only | Multilingual | Required VRAM |
| ------- | ---------- | ------------ | ------------ | ------------- |
| tiny    |	39 M       |	 ✓        |	   ✓        |      ~1 GB    |
| base	  | 74 M       |	 ✓        |	   ✓        |      ~1 GB    |
| small	  | 244 M      |	 ✓        |	   ✓        |      ~2 GB    |
| medium  |	769 M	   |     ✓        |	   ✓        |      ~5 GB    |
| large   |	1550 M     |	 x        |	   ✓         |     ~10 GB   |
| large-v2|	1550 M     |	 x        |	   ✓         |     ~10 GB   |

> **_Note_**: Keep in mind that opting for a large or large-v2 model will require a significant amount of resources. Therefore, we recommend using a small or medium model. However, if you have a machine capable of running those large models, you can go for it.

if you want to add more words to ```"curse_words"``` list you will need to encrypt it in base64, you can use this script to do so:
```python
import base64

word = "something explicit"
word_to_bytes = bytes(word, "ascii")
encoded_word = base64.b64encode(word_to_bytes)

print(f"'{word}' = {encoded_word}")

"""

Output:
'something explicit' = b'c29tZXRoaW5nIGV4cGxpY2l0'

"""
```
> **_Note_**: No need to add the `b` before the encoded curse words to the configue, just add "c29tZXRoaW5nIGV4cGxpY2l0"

it is important to use the ```ascii``` encoding type because the curse words reader will use it too.

if you encounter the following error in the API logs:
```bash
2023-04-15 02:55:50.409 | CRITICAL | utils.curse_words:curse_words:20 - "hello" is not encoded in base64
```
then you need to go back to the configue and replace the curse word "hello" with it encoded one in base64.

* ## MusBleep configue 

You can also change the MusBleep configue file located at ```MusBleep/conf/MusBleep-conf.json``` to change the default port (3000) and the API url:

```json
{
    "api": "http://localhost:9090",
    "port": 3000
}
```

in case the API isn't up when trying to upload a music to bleep, an error message will appear to the user.

<div align="center">

<img src="MusBleep/../assets/api_checker_error_message.png" />

</div>

# Usage

Running MusBleep is done by first running the API, then the Front-end itself:
* Running the API

```bash
$ cd MusBleep/api
$ python api.py
```

* Running the Front-end

```bash
$ pc init
$ pc run
```

> **_Note_**: You need to be in the root directory of the project before executing this command

After running the API and the front-end, you can navigate to [```http:/localhost:3000```](http:/localhost:3000) to use MusBleep.

<image src="assets/MusBleep_preview.png" alt="MusBleep preview" style="border-radius: 10px;" />

# Contributing

We welcome contributions from the community! If you find a bug or want to suggest a new feature, please open an issue on this repository to discuss it with the team. When contributing code, please make sure to follow the coding standards and testing procedures outlined in the repository. To submit your changes, fork the repository and submit a pull request with a detailed description of the changes made. We'll review your code as soon as possible and merge it if it meets our quality standards.

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/0RaMsY0/MusBleep/blob/main/LICENSE) file for details.