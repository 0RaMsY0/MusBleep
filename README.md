<div align="center">
    <h1 align="center">
        <image src="assets/MusBleep.png" height="300px">
    </h1>

[![Issues](https://img.shields.io/github/issues/0RaMsY0/MusBleep?style=for-the-badge)](https://github.com/0RaMsY0/MusBleep/issues)
[![License](https://img.shields.io/github/license/0RaMsY0/MusBleep?color=brightgreen&style=for-the-badge)](https://github.com/0RaMsY0/MusBleep/blob/main/LICENSE)
[![Downloads](https://img.shields.io/github/downloads/0RaMsY0/MusBleep/total?style=for-the-badge)]()

</div>

# Getting started

MusBleep is a self-hosted project that makes it easy to censor explicit content in music tracks. Our application is designed for everyone who wants to enjoy there favorite music without being exposed to explicit content.

To get started with MusBleep, you'll need to install it on your own server or local machine. Our application relies on [Pynecone](https://github.com/pynecone-io/pynecone), [Whisper](https://github.com/linto-ai/whisper-timestamped), and [FastAPI](https://github.com/tiangolo/fastapi), so make sure you have those installed before you begin.

We've included detailed instructions on how to install and use our application in the sections below. If you have any questions or need further assistance, please don't hesitate to reach out to our team. We're always happy to help!

# Installation

Musbleep requires the following to get started:

* python3.10+
* Pynecone
* FastAPI
* whisper-timestamped
* Linux OS (Ubuntu, kali linux, arch...)

you can run the setup script located at ```MusBleep/scripts/setup.py``` to automaticly download everything that you will need.

```bash
$ python MusBleep/scripts/setup.py setup
```

> **_Note_**: It may takes some time depending on your internet speed

you may need to change some values in the API configue located at ```MusBleep/api/conf/api-conf.json```, currentlly the default configuration is:
```json
{
    "port": 9090,
    "whisper_model_type": "small"
}
```
here we manly going to focus on the ```whisper_model_type``` you can see all the diffrent types of the whisper model in the following table:

|   Size  | parameters | English-only | Multilingual |
| ------- | ---------- | ------------ | ------------ |
| tiny    |	39 M       |	 ✓        |	   ✓         |
| base	  | 74 M       |	 ✓        |	   ✓        |
| small	  | 244 M      |	 ✓        |	   ✓        |
| medium  |	769 M	   |     ✓        |	   ✓        |
| large   |	1550 M     |	 x        |	   ✓         |
| large-v2|	1550 M     |	 x        |	   ✓         |

> **_Note_**: Keep in mind that going for a large or large-v2 model will require a lot of ressources so we recommend to use small, or medium model, but of course if you have a machine that is capable of running those large models you can go for it.

# Usage

Running MusBleep is done by first running the API, then the Front-end itself:
* Running the API

```bash
$ cd MusBleep/api
$ python api.py
```

* Running the Front-end

```bash
$ pc run
```

> **_Note_**: You need to be in the root directory of the project before executing this command

After that you can navigate to ```http:/localhost:3000``` and you will see that MusBleep is running.

<image src="assets/MusBleep_preview.png" alt="MusBleep preview" style="border-radius: 10px;" />

# Contributing
We welcome contributions from the community! If you find a bug or want to suggest a new feature, please open an issue on this repository. If you want to contribute code, please fork the repository and submit a pull request. We'll review your code as soon as possible!

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/0RaMsY0/MusBleep/blob/main/LICENSE) file for details.