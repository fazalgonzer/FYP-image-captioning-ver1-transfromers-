import os 
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s:%(message)s]"

log_dir= "logs"
log_file_path=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(level=logging.INFO,
                    format=logging_str,

                    handlers=[logging.FileHandler(log_file_path),
                              logging.StreamHandler(sys.stdout)
                            


                    ]
                    )


logger=logging.getLogger("Imagecaptionlogger")
