import os
import yaml


def update_dict(d: dict, params: dict) -> dict:
    """Overwrite config parameters"""
    print("Overwriting config parameters:")

    for k, v in params.items():
        *path, key = k.split(".")
        inner_dict = d
        for path_key in path:
            inner_dict = inner_dict[path_key]
        old_v = inner_dict.get(key)
        inner_dict[key] = v
        print(f"{k} ".ljust(50, "."), f"{old_v} -> {v}")

    return d


def save_config(config: dict, directory: str, filename="config.yml"):
    """Read config to a file"""
    os.makedirs(directory, exist_ok=True)
    fp = os.path.join(directory, filename)
    with open(fp, "w") as f:
        yaml.dump(config, f)


def read_yaml_config(cfg_path: str) -> dict:
    """Read yaml config to a dictionary"""
    with open(cfg_path) as cfg:
        cfg_yaml = yaml.load(cfg, Loader=yaml.FullLoader)

    return cfg_yaml
