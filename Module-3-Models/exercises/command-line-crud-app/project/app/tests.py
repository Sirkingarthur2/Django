from django.test import TestCase
from app import models

# Create your tests here.

class TestPalette(TestCase):
    def test_can_create_palette(self):
        palette = models.create(
            "Alice",
            "Red, Blue",
            True,
        )

        self.assertIsNotNone(palette)
        self.assertEqual(palette.name, "Alice")
        self.assertEqual(palette.colors, "Red, Blue")
        self.assertTrue(palette.favorite_colors)

    def test_can_view_all_palettes_at_once(self):
        palettes_data = [
            {"name": "Alice", "colors": "Red, Blue", "favorite_colors": True},
            {"name": "Bob", "colors": "Green, Yellow", "favorite_colors": False},
            {"name": "Charlie", "colors": "Purple, Orange", "favorite_colors": True},
        ]

        for palette_data in palettes_data:
            models.create(
                palette_data["name"],
                palette_data["colors"],
                palette_data["favorite_colors"],
            )

        palettes = models.read_all()

        self.assertEqual(len(palettes), len(palettes_data))

        palettes_data = sorted(palettes_data, key=lambda p: p["name"])
        palettes = sorted(palettes, key=lambda p: p.name)

        for data, palette in zip(palettes_data, palettes):
            self.assertEqual(data["name"], palette.name)
            self.assertEqual(data["colors"], palette.colors)
            self.assertEqual(data["favorite_colors"], palette.favorite_colors)

    def test_can_search_by_name(self):
        palettes_data = [
            {"name": "Alice", "colors": "Red, Blue", "favorite_colors": True},
            {"name": "Bob", "colors": "Green, Yellow", "favorite_colors": False},
            {"name": "Charlie", "colors": "Purple, Orange", "favorite_colors": True},
        ]

        for palette_data in palettes_data:
            models.create(
                palette_data["name"],
                palette_data["colors"],
                palette_data["favorite_colors"],
            )

        self.assertIsNone(models.search_by_name("NonExistent"))

        palette = models.search_by_name("Charlie")

        self.assertIsNotNone(palette)
        self.assertEqual(palette.colors, "Purple, Orange")

    def test_can_view_favorites(self):
        palettes_data = [
            {"name": "Alice", "colors": "Red, Blue", "favorite_colors": True},
            {"name": "Bob", "colors": "Green, Yellow", "favorite_colors": False},
            {"name": "Charlie", "colors": "Purple, Orange", "favorite_colors": True},
        ]

        for palette_data in palettes_data:
            models.create(
                palette_data["name"],
                palette_data["colors"],
                palette_data["favorite_colors"],
            )

        self.assertEqual(len(models.read_favorites()), 2)

    def test_can_update_palette_colors(self):
        palettes_data = [
            {"name": "Alice", "colors": "Red, Blue", "favorite_colors": True},
            {"name": "Bob", "colors": "Green, Yellow", "favorite_colors": False},
            {"name": "Charlie", "colors": "Purple, Orange", "favorite_colors": True},
        ]

        for palette_data in palettes_data:
            models.create(
                palette_data["name"],
                palette_data["colors"],
                palette_data["favorite_colors"],
            )

        models.update("Alice", "Black, White", False)

        self.assertEqual(
            models.search_by_name("Alice").colors, "Black, White"
        )

    def test_can_delete_palette(self):
        palettes_data = [
            {"name": "Alice", "colors": "Red, Blue", "favorite_colors": True},
            {"name": "Bob", "colors": "Green, Yellow", "favorite_colors": False},
            {"name": "Charlie", "colors": "Purple, Orange", "favorite_colors": True},
        ]

        for palette_data in palettes_data:
            models.create(
                palette_data["name"],
                palette_data["colors"],
                palette_data["favorite_colors"],
            )

        models.delete("Bob")

        self.assertEqual(len(models.read_all()), 2)