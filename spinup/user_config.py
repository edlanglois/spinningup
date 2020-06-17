import configparser
import os
import os.path as osp
import tempfile

CONFIG_DIR = osp.join(
    os.getenv("XDG_CONFIG_HOME", osp.expanduser("~/.config")), "spinup"
)
config = configparser.ConfigParser()
config.read(osp.join(CONFIG_DIR, "config"))

# Default neural network backend for each algo
# (Must be either 'tf1' or 'pytorch')
DEFAULT_BACKEND = {
    'vpg': 'pytorch',
    'trpo': 'tf1',
    'ppo': 'pytorch',
    'ddpg': 'pytorch',
    'td3': 'pytorch',
    'sac': 'pytorch'
}

# Where experiment outputs are saved by default:
DEFAULT_DATA_DIR = config.get(
    "spinup", "data_dir", fallback=osp.join(tempfile.gettempdir(), "experiments")
)

# Whether to automatically insert a date and time stamp into the names of
# save directories:
FORCE_DATESTAMP = config.getboolean("spinup", "force_datestamp", fallback=False)

# Whether GridSearch provides automatically-generated default shorthands:
DEFAULT_SHORTHAND = config.getboolean("spinup", "default_shorthand", fallback=True)

# Tells the GridSearch how many seconds to pause for before launching 
# experiments.
WAIT_BEFORE_LAUNCH = config.getint("spinup", "wait_before_launch", fallback=5)
