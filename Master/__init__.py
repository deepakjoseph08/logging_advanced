import logging,os,json,logging.config


path = "../config/log_config.json"
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
# Creating