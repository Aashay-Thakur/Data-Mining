from csv import writer as csv_writer
from pandas import read_csv
from sklearn.model_selection import KFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

print_row_limit = 10
print_col_limit = 4

def convert_files(data_file):
    with open(data_file, 'r') as in_file:
        stripped = (line.strip().replace('\t', ',') for line in in_file)
        lines = (line.strip().split(",") for line in stripped if line)
        with open(Path(str(data_file) + '.csv'), 'w', newline="") as out_file:
            writer = csv_writer(out_file, lineterminator='\n')
            writer.writerows(lines)

def pre_process(dataframe):
    label_encoder = LabelEncoder()
    for column in dataframe.columns:
        dataframe[column] = label_encoder.fit_transform(dataframe[column])
    return dataframe

def split(dataframe):
    array = dataframe.values
    X = array[:, 1:22]
    Y = array[:, 0]
    return X, Y


if __name__ == "__main__":
    
    if not Path("./data/mushroom.test.csv").exists():
        convert_files(Path("./data/mushroom.test"))
    if not Path("./data/mushroom.training.csv").exists():
        convert_files(Path("./data/mushroom.training"))

    train_file = Path("data/mushroom.training.csv")
    test_file = Path("data/mushroom.test.csv")

    print(f"\nTraining file: {train_file}")
    print(f"Test file: {test_file}\n")

    names = ['outcome',
            'cap-shape', 
            'cap-surface', 
            'cap-color', 
            'bruises', 
            'odor', 
            'gill-attachment', 
            'gill-spacing', 
            'gill-size', 
            'gill-color', 
            'stalk-shape', 
            'stalk=surface-above-ring', 
            'stalk-surface-below-ring', 
            'stalk-color-above-ring', 
            'stalk-color-below-ring', 
            'veil-type', 
            'veil-color', 
            'ring-number', 
            'ring-type', 
            'spore-print-color', 
            'population', 
            'habitat', 
            ]
    
    print("Press 1 to use the training file")
    print("Press 2 to use the test file")
    choice = int(input())
    if choice == 1:
        dataframe = read_csv(train_file, names=names, header=None)
    elif choice == 2:
        dataframe = read_csv(test_file, names=names, header=None)
    else:
        print("Invalid choice")
        exit(1)

    print(f"\n{'-' * 10} Before Preprocessing {'-' * 10}\n")
    print(dataframe.head(print_row_limit)[names[:print_col_limit]])

    dataframe = pre_process(dataframe)

    print(f"\n{'-' * 10} After Preprocessing {'-' * 10}\n")
    print(dataframe.head(print_row_limit)[names[:print_col_limit]])

    X, Y = split(dataframe)

    kfold = KFold(n_splits=10)
    model = GaussianNB()
    results = cross_val_score(model, X, Y, cv=kfold)
    print(f"\n\n{'-' * 20}\nAccuracy: {results.mean()*100:.2f}%")
    print(f"SD (σ): {results.std()*100.0:.3f}\n{'-' * 20}\n\n")
