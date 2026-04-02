"""
This program checks required dependencies, fetches real data from the
PokeAPI, analyzes it with pandas and numpy, and generates a simple
visualization with matplotlib
"""

import importlib
import sys
from typing import Any


REQUIRED_MODULES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computations ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready"
}


def get_module_version(module: object) -> str:
    """
    Safely get a module version
    :param module: Imported module
    :return: Version string or fallback text
    """

    try:
        version: str | None = getattr(module, "__version__", None)
        if version is not None:
            return version

        return "unknown version"
    except Exception:
        return "unknown version"


def check_dependencies() -> tuple[bool, dict[str, object]]:
    """
    Check whether required dependencies are installed
    """

    imported_modules: dict[str, object] = {}
    all_available: bool = True

    print("Checking dependencies:")
    for module_name, description in REQUIRED_MODULES.items():
        try:
            module = importlib.import_module(module_name)
            imported_modules[module_name] = module
            version: str = get_module_version(module)
            print(f"[OK] {module_name} ({version}) - {description}")
        except ImportError:
            print(f"[MISSING] {module_name} - Not installed")
            all_available = False
        except Exception:
            print(f"[ERROR] {module_name} - Could not be checked")
            all_available = False

    return all_available, imported_modules


def print_install_help() -> None:
    """Print installation instructions"""
    print(
        """
Missing dependencies detected.
Install them with one of these approaches:
Using pip:
pip install -r requirements.txt
Using poetry:
poetry install
Then run the program again."""
    )

def fetch_pokemon_data(requests_module: object, limit: int) -> list[dict[str, Any]]:
    """Fetch Pokemon data from the PokeAPI"""
    pokemon_data: list[dict[str, Any]] = []
    base_url: str = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"

    try:
        response = requests_module.get(base_url, timeout=10)
        response.raise_for_status()
        results: list[dict[str, str]] = response.json().get("results", [])

        for pokemon in results:
            try:
                detail_response = requests_module.get(
                    pokemon["url"],
                    timeout=10
                )
                detail_response.raise_for_status()
                details: dict[str, Any] = detail_response.json()

                types_list: list[dict[str, Any]] = details.get("types", [])
                pokemon_entry: dict[str, Any] = {
                    "name": details.get("name", "unknown"),
                    "height": details.get("height", 0),
                    "weight": details.get("weight", 0),
                    "base_experience": details.get("base_experience", 0),
                    "type_count": len(types_list)
                }
                pokemon_data.append(pokemon_entry)
            except Exception:
                print(f"Warning: Could not load details for {pokemon['name']}")
    except Exception as error:
        print(f"Error fetching data from PokeAPI: {error}")

    return pokemon_data


def analyze_data(
        pandas_module: object,
        numpy_module: object,
        pokemon_data: list[dict[str, object]]
) -> object | None:
    """
    Convert pokemon data to a DataFrame and compute basic statistics
    :return: DataFrame or None if analysis fails
    """
    try:
        dataframe = pandas_module.DataFrame(pokemon_data)
        if dataframe.empty:
            print("No data available for analysis")
            return None

        height_array = numpy_module.array(dataframe["height"])
        weight_array = numpy_module.array(dataframe["height"])
        experience_array = numpy_module.array(dataframe["base_experience"])

        print("\nAnalyzing Matrix data...")
        print(f"Processing {len(dataframe)} data points...")

        print("\nNumeric summary:")
        print(f"- Average height: {numpy_module.mean(height_array):.2f}")
        print(f"- Average weight: {numpy_module.mean(weight_array):.2f}")
        print(
            "- Average base experience: "
            f"{numpy_module.mean(experience_array):.2f}"
        )

        top_pokemon = dataframe.sort_values(
            by="base_experience",
            ascending=False
        ).head(10)

        print("\nTop 10 Pokemon by base_experience:")
        print(top_pokemon[["name", "base_experience"]].to_string(index=False))

        return top_pokemon
    except Exception as error:
        print(f"Error during analysis: {error}")
        return None


def create_visualization(matplotlib_module: object, dataframe: object) -> str:
    """Create and save a bar chart from the analyzed Pokemon data"""
    output_file: str = "matrix_analysis.png"

    try:
        print("\nGenerating visualization...")
        matplotlib_module.figure(figsize=(12, 6))
        matplotlib_module.bar(
            dataframe["name"],
            dataframe["base_experience"]
        )
        matplotlib_module.title("Top 10 Pokemon by Base Experience")
        matplotlib_module.xlabel("Pokemon")
        matplotlib_module.ylabel("Base Experience")
        matplotlib_module.xticks(rotation=45)
        matplotlib_module.tight_layout()
        matplotlib_module.savefig(output_file)
        matplotlib_module.close()

        return output_file
    except Exception as error:
        print(f"Error creating visualization: {error}")
        return ""


def main() -> None:
    """Main program execution"""
    print(f"LOADING STATUS: Loading programs...")
    dependencies_ok, imported_modules = check_dependencies()
    if not dependencies_ok:
        print_install_help()
        sys.exit(1)

    try:
        matplotlib_pyplot = importlib.import_module("matplotlib.pyplot")
    except ImportError:
        print("\n[MISSING] matplotlib.pyplot - Visualization unavailable")
        print_install_help()
        sys.exit(1)

    pokemon_data = fetch_pokemon_data(imported_modules["requests"], limit=20)
    if not pokemon_data:
        print("\nNo Pokemon data could be retrieved")
        sys.exit(1)

    analyzed_dataframe = analyze_data(
        imported_modules["pandas"],
        imported_modules["numpy"],
        pokemon_data
    )

    if analyzed_dataframe is None:
        sys.exit(1)

    try:
        matplotlib_pyplot = importlib.import_module("matplotlib.pyplot")
    except ImportError:
        print("\n[MISSING] matplotlib.pyplot - Visualization unavailable")
        print_install_help()
        sys.exit(1)

    output_file = create_visualization(matplotlib_pyplot, analyzed_dataframe)

    if output_file:
        print("\nAnalysis complete!")
        print(f"Results saved to: {output_file}")
    else:
        print("\nAnalysis finished, but no visualization was saved.")


if __name__ == "__main__":
    main()
