import pandas as pd
import time

vocab_dict = dict()

def create_vocab_dict(s: str) -> dict:
    tmp_vocab_list = (s[0:len(s)-1].strip()).split()
    print(tmp_vocab_list)

def load_dataset():
    train_set = pd.read_csv("../data/train.csv")
    for l, m, r in zip(train_set["prompt"], train_set["response_a"], train_set["response_b"]):
        print(l)
        create_vocab_dict(l)
        create_vocab_dict(m)
        create_vocab_dict(r)
        break

if __name__ == "__main__":
    print("test begin!!")
    time.sleep(1)
    load_dataset()
