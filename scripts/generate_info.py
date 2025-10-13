import loop_plotter
import generic
import json



def export_loop_plot(length: int, weight: int, include: loop_plotter.PlotInclusions):
    """
    Exports a loop plot to `loop_plot.json`.
    """

    plot = loop_plotter.plot_loops(length, weight, include)
    with (generic.PROGRAM_PATH / "loop_plot.json").open("w", encoding="utf-8") as file:
        file.write(f"{{\n{",\n".join([" "*4 + json.dumps({f"L{key[0]} W{key[1]}": plot[key]})[1:-1] for key in plot])}\n}}")



if __name__ == "__main__":
    export_loop_plot(
        25, 25,
        {
            "denominator": True,
            "denominators": True,
            "denominator_factors": False,
            "numerators": False,
            "numerator_gcds": False,
        }
    )