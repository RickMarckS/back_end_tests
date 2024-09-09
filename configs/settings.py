from dotenv import  load_dotenv
import os
import json
import logging
load_dotenv()

url_base = os.environ.get('url_base')

url_modify = os.environ.get('url_modify')

post_payload_str = os.environ.get('post_payload')
post_payload = json.loads(post_payload_str) if post_payload_str else {}

patch_payload_str = os.environ.get('patch_payload')
patch_payload = json.loads(patch_payload_str) if patch_payload_str else {}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)