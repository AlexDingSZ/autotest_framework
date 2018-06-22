import os
"""
获取路径的上一级
"""
def get_parent_path(current_path):
    return os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
