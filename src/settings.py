import os

SRC_ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

CREDENTIALS_DIR_PATH = os.path.join(SRC_ROOT_DIR_PATH, 'credentials')
GCP_CREDENTIALS_PATH = os.path.join(CREDENTIALS_DIR_PATH, 'gcp-quickstart-sa.json')
