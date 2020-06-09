from submarine.ml.tensorflow.model import DeepFM
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-conf", help="a JSON configuration file for DeepFM", type=str)
    parser.add_argument("-task_type", default='train',
                        help="train or evaluate, by default is train")
    args = parser.parse_args()
    json_path = args.conf
    task_type = args.task_type

    model = DeepFM(json_path=json_path)

    if task_type == 'train':
        model.train()
        result = model.evaluate()
        print("Model metrics : ", result)
