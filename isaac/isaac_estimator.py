import tensorflow as tf
import numpy as np

feature_columns = [
        tf.feature_column.numeric_column("IsEnemyAbove"),
        tf.feature_column.numeric_column("IsEnemyBelow"),
        tf.feature_column.numeric_column("IsEnemyLeft"),
        tf.feature_column.numeric_column("IsEnemyRight")
    ]

_CSV_COLUMNS = ['IsEnemyAbove', 'IsEnemyBelow', 'IsEnemyLeft', 'IsEnemyRight', 'MovementDir', 'ShotDir']
_CSV_COLUMN_DEFAULTS = [[''],[''],[''],[''],[''],['']]

def input_fn():
    # Get all of the training data
    lines = [line.rstrip('\n') for line in open('training_data.csv')]
    # OR
    dataset = tf.data.TextLineDataset("training_data.csv")

    def parse_data(value):
        columns = tf.decode_csv(value, record_defaults=_CSV_COLUMN_DEFAULTS)
        features = dict(zip(_CSV_COLUMNS, columns))
        labels = features.pop('MovementDir')
        return features, labels

    dataset = dataset.map(parse_data, num_parallel_calls=5)
    dataset = dataset.repeat(40)
    dataset = dataset.batch(40)

    return dataset