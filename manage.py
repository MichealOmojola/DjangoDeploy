#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import pickle
from unpickleload import *
# from unpickleload import make_keras_picklable


# import pickle
# from tensorflow.keras.models import Model
# # from tensorflow.python.keras.engine.training import Model
# from tensorflow.python.keras.layers import deserialize, serialize
# from tensorflow.python.keras.saving import saving_utils


# # tensorflow.python.compat.v1.disable_eager_execution()

# def unpack(model, training_config, weights):
#     restored_model = deserialize(model)
#     if training_config is not None:
#         restored_model.compile(
#             **saving_utils.compile_args_from_training_config(
#                 training_config
#             )
#         )
#     restored_model.set_weights(weights)
#     return restored_model

# # Hotfix function
# def make_keras_picklable():

#     def __reduce__(self):
#         model_metadata = saving_utils.model_metadata(self)
#         training_config = model_metadata.get("training_config", None)
#         model = serialize(self)
#         weights = self.get_weights()
#         return (unpack, (model, training_config, weights))

#     cls = Model
#     cls.__reduce__ = __reduce__

# make_keras_picklable()




def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoAPI.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    make_keras_picklable()
    # Run the function
    main()