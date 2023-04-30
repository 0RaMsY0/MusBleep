import pynecone as pc

config = pc.Config(
    app_name="MusBleep",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.PROD,
)
