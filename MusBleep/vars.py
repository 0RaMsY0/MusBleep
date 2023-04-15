
GITHUB_REPO = "https://github.com/0RaMsY0/MusBleep"

# Fonts to include.
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap",
    "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
]

# Mode
DARK_MODE  = "#121212"
LIGHT_MODE = "#fafafa"

# Ending messages
ERROR_MESSAGES = [
    "Faild to upload the music file, please try again later",
    "Faild to bleep the music file, please try again later",
    "Faild to connect to the api, please make sure it is running"
]
SUCCESS_MESSAGES = [
    "Successfully uploaded, and bleeped the music"
]
MESSAGES_STATUS = {
    "Faild to upload the music file, please try again later": "error",
    "Faild to bleep the music file, please try again later": "error",
    "Successfully uploaded, and bleeped the music": "success",
    "Faild to connect to the api, please make sure it is running": "error"
}

# Styles
PLAY_MUSIC_CARD_STYLE_DESKTOP_AND_TABLET = {
    "background": "blue",
    "border": "1px solid #b9f0ef",
    "border_radius": "5em",
    "padding": "1em",
    "box_shadow": """
        rgba(17, 7, 53, 0.05) 0px 51px 78px 0px, rgba(17, 7, 53, 0.035) 0px 21.3066px 35.4944px 0px, rgba(17, 7, 53, 0.03) 0px 11.3915px 18.9418px 0px, rgba(17, 7, 53, 0.024) 0px 6.38599px 9.8801px 0px, rgba(17, 7, 53, 0.02) 0px 3.39155px 4.58665px 0px, rgba(17, 7, 53, 0.016) 0px 1.4113px 1.55262px 0px, rgba(41, 56, 78, 0.05) 0px 1px 0px 0px inset
        """,
    "height": "100%",
    "align_items": "left",
    "width": "100%",
    "min_height": "5em",
    "padding": "2em",
    "bg": "rgba(248, 248, 248, .75)",
    "_hover": {
        "box_shadow": """
        rgba(23, 6, 100, 0.035) 0px 24px 22px 0px, rgba(23, 6, 100, 0.055) 0px 8.5846px 8.03036px 0px, rgba(23, 6, 100, 0.067) 0px 4.77692px 3.89859px 0px, rgba(23, 6, 100, 0.082) 0px 2.63479px 1.91116px 0px, rgba(23, 6, 100, 0.12) 0px 1.15891px 0.755676px 0px
    """,
    },
}

PLAY_MUSIC_CARD_STYLE_MOBILE = {
    "background": "blue",
    "border": "1px solid #b9f0ef",
    "border_radius": "5em",
    "padding": "1em",
    "box_shadow": """
        rgba(17, 7, 53, 0.05) 0px 51px 78px 0px, rgba(17, 7, 53, 0.035) 0px 21.3066px 35.4944px 0px, rgba(17, 7, 53, 0.03) 0px 11.3915px 18.9418px 0px, rgba(17, 7, 53, 0.024) 0px 6.38599px 9.8801px 0px, rgba(17, 7, 53, 0.02) 0px 3.39155px 4.58665px 0px, rgba(17, 7, 53, 0.016) 0px 1.4113px 1.55262px 0px, rgba(41, 56, 78, 0.05) 0px 1px 0px 0px inset
        """,
    "height": "100%",
    "align_items": "left",
    "width": "100%",
    "min_height": "5em",
    "padding": "1em",
    "bg": "rgba(248, 248, 248, .75)",
    "_hover": {
        "box_shadow": """
        rgba(23, 6, 100, 0.035) 0px 24px 22px 0px, rgba(23, 6, 100, 0.055) 0px 8.5846px 8.03036px 0px, rgba(23, 6, 100, 0.067) 0px 4.77692px 3.89859px 0px, rgba(23, 6, 100, 0.082) 0px 2.63479px 1.91116px 0px, rgba(23, 6, 100, 0.12) 0px 1.15891px 0.755676px 0px
    """,
    },
}