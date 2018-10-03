import logging,os,json,logging.config
#from MS_2 import child_ms2


default_path = "../config/log_config.json"
path = default_path
print(os.path.abspath(default_path))
print(os.path.exists(path))
if os.path.exists(path):
    print("path exists")
    with open(path, 'rt') as f:
        config = json.load(f)
        # print(config)
    logging.config.dictConfig(config)
else:
    print("default_logger")
    logging.basicConfig(level='INFO')