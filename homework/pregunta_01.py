"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    ruta_data="files\input/news.csv"
    plt.figure()
    
    colors={
        "Television":"dimgray",
        'Newspaper':'grey',
        'Internet':'tab:blue',
        'Radio':'lightgrey',
    }

    zorder={
        'Television':1,
        'Newspaper':1,
        'Internet':2,
        'Radio':1,
    }

    linewidths={
        'Television':2,
        'Newspaper':2,
        'Internet':3,
        'Radio':2,
    }

    reader=pd.read_csv(ruta_data,index_col=0)
    for col in reader.columns:
        plt.plot(reader[col],color=colors[col] ,label=col, zorder=zorder[col],linewidth=linewidths[col],)

    plt.title("how people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in reader.columns:
        first_year=reader.index[0]
        plt.scatter(
            x=first_year,
            y=reader[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )
        plt.text(
            first_year - 0.2,
            reader[col][first_year],
            col + " "+ str(reader[col][first_year]) + "%",
            ha='right',
            va='center',
            color=colors[col],
        )

        last_year=reader.index[-1]
        plt.text(
            last_year + 0.2,
            reader[col][last_year],
            str(reader[col][first_year]) + "%",
            ha='left',
            va='center',
            color=colors[col],
        )
        plt.scatter(
            x=last_year,
            y=reader[col][last_year],
            color=colors[col],
            zorder=zorder[col],
        )
    

    base_folder = "files"
    plot_folder = os.path.join(base_folder, "plots")

    # Crear las carpetas
    os.makedirs(plot_folder, exist_ok=True)

    plt.tight_layout()
    plt.savefig("files/plots/news.png")


    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
pregunta_01()