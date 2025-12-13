"""Entry-point program for Module 1 exercise 6.

Analytics garden management system with nested statistics and
a small inheritance hierarchy.
"""


class Plant:
    """Base plant type used in the garden analytics system"""
    def __init__(self, name: str, height: int) -> None:
        """Create a Plant with a name and height also stablishes
           plant_type as regular for Plant base type.
        """
        self._name: str = name
        self._height: int = height
        self._plant_type: str = "regular"

    def get_name(self) -> str:
        """Returns the name of this plant"""
        return self._name

    def get_height(self) -> int:
        return self._height

    def grow(self) -> int:
        """Simulate one day of growth and returns the amount grown."""
        self._height += 1
        return 1

    def get_info(self) -> str:
        """Returns a basic textual description of this plant"""
        return f"{self._name}: {self._height}cm"

    def get_plant_type(self) -> str:
        return self._plant_type


class FloweringPlant(Plant):
    """Plant that can bloom and has a flower color"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Creates a FloweringPlant with a color and updates plant_type"""
        super().__init__(name, height)
        self._color: str = color
        self._plant_type: str = "flowering"

    def get_info(self) -> str:
        """Returns description including flower color and blooming state"""
        return f"{super().get_info()}, {self._color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Special flowering plant which has prize_points."""
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        """Create a PrizeFlower with aditional prize_points"""
        super().__init__(name, height, color)
        self._prize_points: int = prize_points
        self._plant_type: str = "prize"

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self._prize_points}"


class GardenManager:
    """Manager for a single garden and its analytics"""
    total_gardens_managed: int = 0

    class GardenStats:
        """Helper nested class to track statistics for a garden"""

        def __init__(self) -> None:
            """Create counters for analytics"""
            self._plants_added: int = 0
            self._total_growth: int = 0
            self._regular_count: int = 0
            self._flowering_count: int = 0
            self._prize_count: int = 0

        def register_plant(self, plant: Plant) -> None:
            """Update counters when a new plant is added."""
            self._plants_added += 1
            plant_type: str = plant.get_plant_type()
            if plant_type == "prize":
                self._prize_count += 1
            elif plant_type == "flowering":
                self._flowering_count += 1
            else:
                self._regular_count += 1

        def register_gorwth(self, amount: int) -> None:
            """Record additional growth for analytics"""
            self._total_growth += amount

        def get_plants_added(self) -> int:
            return self._plants_added

        def get_total_growth(self) -> int:
            return self._total_growth

        def get_regular_count(self) -> int:
            return self._regular_count

        def get_flowering_count(self) -> int:
            return self._flowering_count

        def get_prize_count(self) -> int:
            return self._prize_count

    def __init__(self, owner_name: str) -> None:
        """Create a garden manager for a specific owner."""
        self._owner_name: str = owner_name
        self._plants: list[Plant] = []
        self.stats: GardenManager.GardenStats = GardenManager.GardenStats()
        GardenManager.total_gardens_managed += 1

    def get_owner(self) -> str:
        return self._owner_name

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden and update statistics"""
        self._plants.append(plant)
        self.stats.register_plant(plant)
        print(f"Added {plant.get_name()} to {self._owner_name}'s garden")

    def grow_all_plants(self) -> None:
        """Simulate growth for all plants in the garden."""
        print(f"{self._owner_name} is helping all plants grow...")
        for plant in self._plants:
            growth = plant.grow()
            self.stats.register_gorwth(growth)
            print(f"{plant.get_name()} grew {growth}cm")

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validates that a plant height is non-negative"""
        return height >= 0

    @staticmethod
    def compute_score(stats: GardenStats) -> int:
        """Computes a score for a garden based on its stats"""
        return (
            64 * stats.get_plants_added()
            + 2 * stats.get_total_growth()
            + 4 * stats.get_regular_count()
            + 6 * stats.get_flowering_count()
            + 10 * stats.get_prize_count()
        )

    def print_report(self, other_manager: "GardenManager"):
        """Print a detailed report for this garden."""
        print(f"=== {self._owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self._plants:
            print(f"- {plant.get_info()}")
        print(
            "Plants added: "
            f"{self.stats.get_plants_added()}, "
            f"Total growth: {self.stats.get_total_growth()}cm"
        )
        print(
            "Plant types: "
            f"{self.stats.get_regular_count()} regular, "
            f"{self.stats.get_flowering_count()} flowering, "
            f"{self.stats.get_prize_count()}, prize Flowers"
        )
        is_valid_height: bool = GardenManager.validate_height(self._plants[0].get_height())
        own_score: int = GardenManager.compute_score(self.stats)
        their_score: int = GardenManager.compute_score(other_manager.stats)
        print(
            f"Height validation test: {is_valid_height}\n"
            "Garden scores - "
            f"{self._owner_name}: {own_score}, {other_manager.get_owner()}: {their_score}"
        )
        print(f"Total gardens managed: {GardenManager.total_gardens_managed}")

    @classmethod
    def alice_and_bob_garden_network(cls) -> tuple["GardenManager", "GardenManager"]:
        """Create a small demo network of managed gardens."""
        alice: GardenManager = cls("Alice")
        bob: GardenManager = cls("Bob")

        oak: Plant = Plant("Oak Tree", 100)
        rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
        sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

        alice.add_plant(oak)
        alice.add_plant(rose)
        alice.add_plant(sunflower)

        bob.stats._plants_added = 1
        bob.stats._regular_count = 1
        bob.stats._total_growth = 12

        return alice, bob

def main() -> None:
    """Run a demo of the garden management analytics system."""
    print("=== Garden Management System Demo ===")
    alice_manager, bob_manager = GardenManager.alice_and_bob_garden_network()
    alice_manager.grow_all_plants()
    alice_manager.print_report(bob_manager)

if __name__ == "__main__":
    main()