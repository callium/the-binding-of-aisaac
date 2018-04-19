import tensorflow as tf
import numpy as np

_CSV_COLUMNS = ['is_enemy_above', 'is_enemy_below', 'is_enemy_left', 'is_enemy_right', 'movement_dir', 'shot_dir']
_CSV_COLUMN_DEFAULTS = [[0],[0],[0],[0],[0],[0]]

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
    # movement_dir = tf.feature_column.numeric_column('movement_dir')
    # shot_dir = tf.feature_column.numeric_column('shot_dir')

    # Wide columns and deep columns.
    feature_columns = [
        is_enemy_above, is_enemy_below, is_enemy_left, is_enemy_right
    ]

    # return base_columns + crossed_columns
    return feature_columns

def input_fn():
    assert tf.gfile.Exists('training_data.csv'), ('%s not found' % 'training_data.csv')

    dataset = tf.data.TextLineDataset('training_data.csv')

    def parse_csv(line):
        columns = tf.decode_csv(line, record_defaults=_CSV_COLUMN_DEFAULTS)
        features = dict(zip(_CSV_COLUMNS, columns))
        labels = features.pop('movement_dir')
        features.pop('shot_dir') # Don't need this right now
        return features, labels

    dataset = dataset.map(parse_csv, num_parallel_calls=1)

    dataset = dataset.repeat(40)
    dataset = dataset.batch(500)

    # print(dataset)

    return dataset


def build_estimator():
    feature_columns = build_model_columns()
    model = tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        hidden_units=[10, 10],
        n_classes=4)
    return model

def print_dataset(ds):
    # Make an iterator
    iter = ds.make_one_shot_iterator()
    element = iter.get_next()
    with tf.Session() as sess:
        print(sess.run(element)) # output: [ 0.42116176  0.40666069]

def main():
    classifier = build_estimator()

    classifier.train(
        input_fn=lambda:input_fn(),steps=50)

    # eval_result = classifier.evaluate(
    #     input_fn=lambda:input_fn())

    # print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

if __name__ == "__main__":
    main()
