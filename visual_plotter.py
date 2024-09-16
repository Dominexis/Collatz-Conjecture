from typing import cast
import generic
import json



def export_visual_plot():
    """
    Exports the visual version of the loop plot to `visual_plot.txt`.
    """

    max_length = 1
    max_weight = 1
    max_value = 1
    loop_plot: dict[tuple[int, int], int] = {}

    # Extract loop plot data
    with (generic.PROGRAM_PATH / "loop_plot.json").open("r", encoding="utf-8") as file:
        loop_plot_data = cast(dict[str, dict[str, list[int]]], json.load(file))

    # Populate loop plot
    for key in loop_plot_data:
        if not loop_plot_data[key]["denominators"]:
            continue
        denominator = loop_plot_data[key]["denominators"][0]

        length = int(key.split(" ")[0][1:])
        weight = int(key.split(" ")[1][1:])
        
        max_length = max(max_length, length)
        max_weight = max(max_weight, weight)
        max_value = max(max_value, denominator)

        loop_plot[(length, weight)] = denominator
    
    max_digits = len(str(max_value))

    # Generate string array
    strings: dict[tuple[int, int], str] = {}
    for length in range(1, max_length + 1):
        for weight in range(1, max_weight + 1):
            key = (length, weight)
            if key in loop_plot:
                value = str(loop_plot[key])
                strings[key] = " "*(max_digits - len(value)) + value
            else:
                strings[key] = " "*max_digits

    # Generate output string
    output = "\n".join([
        "  ".join([
            strings[(length, weight)] for length in range(1, max_length + 1)
        ]) for weight in range(1, max_weight + 1)
    ])

    # Print to file
    with (generic.PROGRAM_PATH / "visual_plot.txt").open("w", encoding="utf-8") as file:
        file.write(output)



if __name__ == "__main__":
    export_visual_plot()