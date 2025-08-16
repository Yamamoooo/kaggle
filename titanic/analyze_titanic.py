import matplotlib.pyplot as plt
import pandas as pd


class analyzer:
    def __init__(self, csv_file, sep=","):
        self.df = pd.read_csv(csv_file, sep=sep)

    def get_information(self):
        print("先頭の5行を表示")
        print(self.df.head())
        print(f"dataframeの形状を確認:{self.df.shape}")
        print(f"indexの確認;{self.df.index}")
        print(f"カラムの確認:{self.df.columns}")
        print(f"dataframeの各列のデータ型を確認:{self.df.dtypes}")

    def scatter_matrix(self):
        pd.plotting.scatter_matrix(self.df, figsize=(10, 10), diagonal="kde")
        plt.show()
        pd.plotting.scatter_matrix(self.df, figsize=(10, 10), diagonal="hist")
        plt.show()

    def check_correlation(self):
        for column in self.df.columns:
            plt.plot(self.df[column], self.df["Survived"])
            plt.xlabel(column)
            plt.ylabel("Survived")
            plt.legend()
            plt.show()
