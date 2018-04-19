import tensorflow as tf
import numpy as np

_CSV_COLUMNS = ['is_enemy_above', 'is_enemy_below', 'is_enemy_left', 'is_enemy_right', 'movement_dir', 'shot_dir']
_CSV_COLUMN_DEFAULTS = [[''],[''],[''],[''],[''],['']]

def build_model_columns():
    # is_enemy_above = tf.feature_column.categorical_column_with_vocabulary_list(
    # 'is_enemy_above', [
    #     '0', '1'])
        
    # is_enemy_below = tf.feature_column.categorical_column_with_vocabulary_list(
    # 'is_enemy_below', [
    #     '0', '1'])

    # is_enemy_left = tf.feature_column.categorical_column_with_vocabulary_list(
    # 'is_enemy_left', [
    #     '0', '1'])

    # is_enemy_right = tf.feature_column.categorical_column_with_vocabulary_list(
    # 'is_enemy_right', [
    #     '0', '1'])

    # movement_dir = tf.feature_column.categorical_column_with_vocabulary_list(
    # 'movement_dir', [
    #     '0', '1', '2', '3', '4'])

    # shot_dir = tf.feature_column.categorical_column_with_vocabulary_list(
    # 'shot_dir', [
    #     '0', '1', '2', '3', '4'])

    is_enemy_above = tf.feature_column.numeric_column('is_enemy_above')
    is_enemy_below = tf.feature_column.numeric_column('is_enemy_below')
    is_enemy_left = tf.feature_column.numeric_column('is_enemy_left')
    is_enemy_right = tf.feature_column.numeric_column('is_enemy_right')
    movement_dir = tf.feature_column.numeric_column('movement_dir')
    shot_dir = tf.feature_column.numeric_column('shot_dir')

    # Wide columns and deep columns.
    feature_columns = [
        is_enemy_above, is_enemy_below, is_enemy_left, is_enemy_right, movement_dir,
        shot_dir,
    ]

    # return base_columns + crossed_columns
    return feature_columns

def input_fn():
    dataset = tf.data.TextLineDataset("training_data.csv")
    def parse_csv(value):
        columns = tf.decode_csv(value, record_defaults=_CSV_COLUMN_DEFAULTS)
        features = dict(zip(_CSV_COLUMNS, columns))
        labels = features.pop('movement_dir')
        return features, labels

    dataset = dataset.map(parse_csv, num_parallel_calls=5)
    dataset = dataset.repeat(40)
    dataset = dataset.batch(40)
    return dataset


def build_estimator():
    feature_columns = build_model_columns()
    model = tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        hidden_units=[10, 10],
        n_classes=4)
    return model

def main():
    classifier = build_estimator()

    # classifier.train(
    #     input_fn=lambda:input_fn(),steps=50)

    # eval_result = classifier.evaluate(
    #     input_fn=lambda:input_fn())

    # print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

if __name__ == "__main__":
    main()
