from config.config import config
import logging,os,json,logging.config
import Master.child_ms1 as ms1
from MS_2 import   child_ms2

logger = logging.getLogger('logger')
logger.info("Master_app")
ms = ms1.ms1()
ms.cms1_test()

ms2 = child_ms2.csm2()
ms2.cms2_test()