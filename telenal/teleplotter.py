import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

matplotlib.rcParams["savefig.dpi"] = 300
matplotlib.rcParams["figure.dpi"] = 200


def plot_normal_distribution(data: list) -> None:
    data.sort()
    mean_ = np.mean(data)
    std_ = np.std(data)
    pdf = stats.norm.pdf(data, mean_, std_)
    plt.plot(data, pdf)
    plt.show()


def plot_wordcloud(wordcloud) -> None:
    plt.figure(dpi=360)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def plot_bars_from_dict(
    dict_: dict,
    labelsize=None,
    figure: tuple[int, int, int] = None,
    title="Chart",
    style="seaborn",
) -> None:
    dict_ = {k: v for k, v in sorted(dict_.items(), key=lambda item: item[1])}
    print(f"Plotting this data: {dict_}")
    plt.style.use(style)
    x = list(dict_.keys())
    y = list(dict_.values())

    if figure:
        plt.figure(figsize=(figure[0], figure[1]), dpi=figure[2])
    if labelsize:
        plt.tick_params(which="minor", labelsize=labelsize)
        plt.tick_params(which="major", labelsize=labelsize)
    plt.barh(x, y, color="green")
    plt.title(title)
    plt.show()
    plt.savefig("image.png", dpi=200)
