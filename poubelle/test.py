"""Affiche un labyrinthe généré par MazeGenerator en texte."""

from mazegenerator import MazeGenerator

DEPLACEMENTS = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def afficher(maze: list[list[int]], entree: tuple[int, int],
             sortie: tuple[int, int], chemin: str) -> None:
    """Dessine la grille : + - | pour les murs, E entrée, X sortie, . chemin."""
    positions = set()
    x, y = entree
    for lettre in chemin:
        dx, dy = DEPLACEMENTS[lettre]
        x, y = x + dx, y + dy
        positions.add((x, y))

    lignes = []
    for y, ligne in enumerate(maze):
        haut = "".join("+" + ("---" if c & 1 else "   ") for c in ligne) + "+"
        milieu = ""
        for x, c in enumerate(ligne):
            milieu += "|" if c & 8 else " "
            if (x, y) == entree:
                milieu += " E "
            elif (x, y) == sortie:
                milieu += " X "
            elif c == 15:
                milieu += " # "
            elif (x, y) in positions:
                milieu += " . "
            else:
                milieu += "   "
        milieu += "|" if ligne[-1] & 2 else " "
        lignes.append(haut)
        lignes.append(milieu)
    bas = "".join("+" + ("---" if c & 4 else "   ") for c in maze[-1]) + "+"
    lignes.append(bas)
    print("\n".join(lignes))


def main() -> None:
    """Génère un labyrinthe de test et l'affiche."""
    gen = MazeGenerator(size=(21, 15), perfect=False)
    entree = gen.maze_entry
    sortie = gen.maze_exit
    chemin = gen.shortest_path or ""
    print(f"Entrée : {entree}  Sortie : {sortie}")
    print(f"Longueur du chemin le plus court : {len(chemin)}")
    print()
    afficher(gen.maze, entree, sortie, chemin)


if __name__ == "__main__":
    main()
