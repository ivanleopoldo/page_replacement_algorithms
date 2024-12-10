import importlib.util
import os

directory = "core"

all_metadata = []

for filename in os.listdir(directory):
    if filename.endswith(".py"):
        file_path = os.path.join(directory, filename)

        module_name = os.path.splitext(filename)[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "metadata"):
            all_metadata.append(module.metadata)
