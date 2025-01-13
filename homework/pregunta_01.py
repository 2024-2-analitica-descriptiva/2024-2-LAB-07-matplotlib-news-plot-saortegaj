"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel



import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Genera el archivo `files/plots/news.png` siguiendo las instrucciones.
    """

    # Crear carpeta 'files/plots' si no existe
    output_dir = os.path.abspath("./files/plots")  # Ruta absoluta
    if not os.path.exists(output_dir):
        print(f"Creando la carpeta: {output_dir}")
        os.makedirs(output_dir)

    # Leer los datos
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Configuración de colores, zorders y grosores de líneas
    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    linewidth = {
        'Television': 1,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    # Crear figura y graficar datos
    plt.figure()

    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidth[col],
        )

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center',
    )

    # Guardar el gráfico
    output_path = os.path.join(output_dir, "news.png")

    try:
        plt.tight_layout()
        plt.savefig(output_path)
        print(f"Gráfico guardado en: {output_path}")
    except Exception as e:
        print(f"Error al guardar el gráfico: {e}")