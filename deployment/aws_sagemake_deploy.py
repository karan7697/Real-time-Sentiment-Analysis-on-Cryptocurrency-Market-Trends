import sagemaker
from sagemaker.pytorch import PyTorchModel

role = 'your-aws-role'
bucket = 'your-s3-bucket-name'

model = PyTorchModel(model_data='s3://{}/model.tar.gz'.format(bucket),
                     role=role,
                     entry_point='bert_sentiment.py',
                     framework_version='1.6.0',
                     py_version='py3')

predictor = model.deploy(instance_type='ml.m4.xlarge', initial_instance_count=1)
