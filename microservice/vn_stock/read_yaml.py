import yaml

def read_yaml(path:str)->dict:
    """read yaml file by path

    Args:
        path (str): _description_

    Returns:
        dict: data of yaml file
    """
    data_bytes = open("/home/ziuteng/ncd_proj/ncd_project/microservice/vnstock/vnstock.yml" , "r")
    yaml_data = yaml.load(data_bytes, Loader=yaml.FullLoader)
    return yaml_data