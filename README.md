# Select_same_ploy_count_mesh
 Select Meshes with Same Poly Count

A Python script for Autodesk Maya that selects all meshes in the scene with the same poly count as the currently selected mesh.

Features:

- Selects all meshes with the same poly count as the active selection
- Works with meshes only (ignores other object types)
- Prints the poly count of the initial selection to the console
- Selects meshes with matching poly count, making it easy to work with similar objects

Usage:

1. Select a mesh object in Maya
2. Run the script
3. The script will select all meshes in the scene with the same poly count as the initial selection

Requirements:

- Autodesk Maya (tested on Maya 2023)
- Python (included with Maya)


This script is useful for artists and technicians who need to work with multiple objects of similar complexity, such as characters, vehicles, or props. By selecting all meshes with the same poly count, you can easily apply materials, shaders, or other attributes to multiple objects at once.