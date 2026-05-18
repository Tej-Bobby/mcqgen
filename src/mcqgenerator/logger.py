import logging 
import os
from datetime import datetime

LOG_FILE=f"mcq_generator_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_path=os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(os.path.dirname(log_path), exist_ok=True)

LOG_FORMAT=os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,filename=log_path, format="[%(asctime)s] %(levelname)s - %(message)s", force=True)

