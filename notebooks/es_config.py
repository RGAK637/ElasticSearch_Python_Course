import os
from pathlib import Path

from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv(Path(__file__).with_name(".env"))

es = Elasticsearch(
    os.environ["ES_URL"],
    basic_auth=(os.environ["ES_USERNAME"], os.environ["ES_PASSWORD"]),
    verify_certs=False,
)