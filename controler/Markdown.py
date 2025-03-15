import re

class Markdown:
    @staticmethod
    def superscript(match:re.Match) -> str:
        """
        Convertit un texte en exposant en texte avec des codes ANSI.

        Parameters:
        -----------
        match : re.Match
            Texte à convertir.

        Returns:
        --------
        str
            Texte converti.
        """

        text = match.group(1)

        ansis = { # Liste des codes ANSI pour les exposants
            "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "+": "⁺", "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ", "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ⁱ", "j": "ʲ", "k": "ᵏ", "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "r": "ʳ", "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ", "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ", "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᶲ", "K": "ᶪ", "L": "ᴸ", "M": "ᴹ", "N": "ᴺ", "O": "ᴼ", "P": "ᵽ", "R": "ʳ", "S": "ᵿ", "T": "ᵀ", "U": "ᴿ", "V": "ᵿ", "W": "ʷ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", " ": " ",
        }

        return "".join(ansis.get(char) for char in text)  # Remplace les caractères par leurs équivalents en exposants

    @staticmethod
    def subscript(match:re.Match) -> str:
        """
        Convertit un texte en indice en texte avec des codes ANSI.

        Parameters:
        -----------
        match : re.Match
            Texte à convertir.

        Returns:
        --------
        str
            Texte converti.
        """

        text = match.group(1)

        ansis = { # Liste des codes ANSI pour les indices
            "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉", "+": "₊", "-": "₋", "=": "₌", "(": "₍", ")": "₎", "a": "ₐ", "e": "ₑ", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ", "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ", "p": "ₚ", "r": "ᵣ", "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "x": "ₓ", " ": " ",
        }

        return "".join(ansis.get(char) for char in text) # Remplace les caractères par leurs équivalents en indices
    
    @staticmethod
    def latex(math:re.Match) -> str:
        """
        Convertit une formule LaTeX en formule ASCII.

        Parameters:
        -----------
        math : re.Match
            Formule LaTeX à convertir.
        
        Returns:
        --------
        str
            Formule convertie en ASCII.
        """

        math = math.group(1)
        
        replacements = [
            (r"_\{(.*?)\}", Markdown.subscript),             # Indices
            (r"_(.)", Markdown.subscript),                   # Indices
            (r"\^\{(.*?)\}", Markdown.superscript),          # Exposants
            (r"\^(.)", Markdown.superscript),                # Exposants
            (r"\\frac\b\s*\{(.*?)\}\{(.*?)\}", r"\1 / \2"),  # Fraction
            (r"\\sqrt\b\s*\{(.*?)\}", r"√(\1)"),             # Racine carrée
            (r"\\times\b\s*", "×"),                          # Multiplication
            (r"\\cdot\b\s*", "·"),                           # Produit scalaire
            (r"\\pm\b\s*", "±"),                             # Plus ou moins
            (r"\\mp\b\s*", "∓"),                             # Moins ou plus
            (r"\\div\b\s*", "÷"),                            # Division
            (r"\\leq\b\s*", "≤"),                            # Inférieur ou égal
            (r"\\geq\b\s*", "≥"),                            # Supérieur ou égal
            (r"\\neq\b\s*", "≠"),                            # Différent
            (r"\\approx\b\s*", "≈"),                         # Approximativement
            (r"\\equiv\b\s*", "≡"),                          # Équivalent
            (r"\\infty\b\s*", "∞"),                          # Infini
            (r"\\forall\b\s*", "∀"),                         # Pour tout
            (r"\\exists\b\s*", "∃"),                         # Il existe
            (r"\\nexists\b\s*", "∄"),                        # Il n'existe pas
            (r"\\in\b\s*", "∈"),                             # Appartient
            (r"\\notin\b\s*", "∉"),                          # N'appartient pas
            (r"\\subset\b\s*", "⊂"),                         # Inclus
            (r"\\subseteq\b\s*", "⊆"),                       # Inclus ou égal
            (r"\\cup\b\s*", "∪"),                            # Union
            (r"\\cap\b\s*", "∩"),                            # Intersection
            (r"\\emptyset\b\s*", "∅"),                       # Ensemble vide
            (r"\\mathbb\b\s*\{R\}", "ℝ"),                    # Ensemble des réels
            (r"\\mathbb\b\s*\{N\}", "ℕ"),                    # Ensemble des naturels
            (r"\\mathbb\b\s*\{Z\}", "ℤ"),                    # Ensemble des entiers
            (r"\\mathbb\b\s*\{Q\}", "ℚ"),                    # Ensemble des rationnels
            (r"\\mathbb\b\s*\{C\}", "ℂ"),                    # Ensemble des complexes
            (r"\\mathbb\b\s*\{P\}", "ℙ"),                    # Ensemble des premiers
            (r"\\mathbb\b\s*\{H\}", "ℍ"),                    # Quaternions
            (r"\\alpha\b\s*", "α"),                          # Alpha
            (r"\\beta\b\s*", "β"),                           # Bêta
            (r"\\gamma\b\s*", "γ"),                          # Gamma
            (r"\\delta\b\s*", "δ"),                          # Delta
            (r"\\epsilon\b\s*", "ε"),                        # Epsilon
            (r"\\zeta\b\s*", "ζ"),                           # Zêta
            (r"\\eta\b\s*", "η"),                            # Êta
            (r"\\theta\b\s*", "θ"),                          # Thêta
            (r"\\iota\b\s*", "ι"),                           # Iota
            (r"\\kappa\b\s*", "κ"),                          # Kappa
            (r"\\lambda\b\s*", "λ"),                         # Lambda
            (r"\\mu\b\s*", "μ"),                             # Mu
            (r"\\nu\b\s*", "ν"),                             # Nu
            (r"\\xi\b\s*", "ξ"),                             # Xi
            (r"\\omicron\b\s*", "ο"),                        # Omicron
            (r"\\pi\b\s*", "π"),                             # Pi
            (r"\\rho\b\s*", "ρ"),                            # Rho
            (r"\\sigma\b\s*", "σ"),                          # Sigma
            (r"\\tau\b\s*", "τ"),                            # Tau
            (r"\\upsilon\b\s*", "υ"),                        # Upsilon
            (r"\\phi\b\s*", "φ"),                            # Phi
            (r"\\chi\b\s*", "χ"),                            # Chi
            (r"\\psi\b\s*", "ψ"),                            # Psi
            (r"\\omega\b\s*", "ω"),                          # Oméga
            (r"\\Alpha\b\s*", "Α"),                          # Alpha majuscule
            (r"\\Beta\b\s*", "Β"),                           # Bêta majuscule
            (r"\\Gamma\b\s*", "Γ"),                          # Gamma majuscule
            (r"\\Delta\b\s*", "Δ"),                          # Delta majuscule
            (r"\\Epsilon\b\s*", "Ε"),                        # Epsilon majuscule
            (r"\\Zeta\b\s*", "Ζ"),                           # Zêta majuscule
            (r"\\Eta\b\s*", "Η"),                            # Êta majuscule
            (r"\\Theta\b\s*", "Θ"),                          # Thêta majuscule
            (r"\\Iota\b\s*", "Ι"),                           # Iota majuscule
            (r"\\Kappa\b\s*", "Κ"),                          # Kappa majuscule
            (r"\\Lambda\b\s*", "Λ"),                         # Lambda majuscule
            (r"\\Mu\b\s*", "Μ"),                             # Mu majuscule
            (r"\\Nu\b\s*", "Ν"),                             # Nu majuscule
            (r"\\Xi\b\s*", "Ξ"),                             # Xi majuscule
            (r"\\Omicron\b\s*", "Ο"),                        # Omicron majuscule
            (r"\\Pi\b\s*", "Π"),                             # Pi majuscule
            (r"\\Rho\b\s*", "Ρ"),                            # Rho majuscule
            (r"\\Sigma\b\s*", "Σ"),                          # Sigma majuscule
            (r"\\Tau\b\s*", "Τ"),                            # Tau majuscule
            (r"\\Upsilon\b\s*", "Υ"),                        # Upsilon majuscule
            (r"\\Phi\b\s*", "Φ"),                            # Phi majuscule
        ]
        
        for pattern, replacement in replacements:  # Applique les remplacements LaTeX -> ASCII
            math = re.sub(pattern, replacement, math)

        return "\033[3m" + math + "\033[0m"  # Met la formule en italique
    
    @staticmethod
    def generate(md_text: str) -> str:
        """
        Convertit un texte Markdown en texte avec ANSI escapes et ASCII pour la mise en forme.

        Parameters:
        -----------
        md_text : str
            Le texte en Markdown.
        
        Returns:
        --------
        str
            Le texte en ASCII avec les codes ANSI.
        """
        
        lines = md_text.split("\n")
        output = []

        while lines:
            line = lines.pop(0)
            if match := re.match(r"^(#{1,6}) (.*)$", line):  # Vérifie si la ligne est un titre
                level = len(match.group(1))  # Niveau du titre
                title = match.group(2)  # Texte du titre
                
                match level:
                    case 1:
                        formatted = "╔" + "═" * (len(title) + 2) + "╗\n" + "║ " + "\033[1;37m" + title + "\033[0m" + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝"
                    case 2:
                        formatted = "┌" + "─" * (len(title) + 2) + "┐\n" + "│ " + "\033[1;37m" + title + "\033[0m" + " │\n" + "╘" + "═" * (len(title) + 2) + "╛"
                    case 3:
                        formatted = "┌" + "─" * (len(title) + 2) + "┐\n" + "│ " + "\033[1;37m" + title + "\033[0m" + " │\n" + "└" + "─" * (len(title) + 2) + "┘"
                    case 4:
                        formatted = " " + "\033[1;37m" + title + "\033[0m" + " \n" + "═" * (len(title) + 2)
                    case 5:
                        formatted = " " + "\033[1;37m" + title + "\033[0m" + " \n" + "╍" * (len(title) + 2)
                    case 6:
                        formatted = " " + "\033[1;37m" + title + "\033[0m" + " \n" + "─" * (len(title) + 2)
                
                output.append(formatted)
            elif match := re.match(r"^\`\`\`(.*?)$", line): # Vérifie si la ligne est un bloc de code
                while (line := lines.pop(0)) != "```":
                    output.append("\033[2m" + line + "\033[0m")
            else:  # Si la ligne n'est pas un titre
                replacements = [
                    (r"\$(.*?)\$", Markdown.latex),                                        # LaTeX
                    (r"\*\*(.*?)\*\*", r"\033[1;37m\1\033[0m"),                            # Gras
                    (r"__(.*?)__", r"\033[1;37m\1\033[0m"),                                # Gras
                    (r"\*(.*?)\*", r"\033[3m\1\033[0m"),                                   # Italique
                    (r"_(.*?)_", r"\033[3m\1\033[0m"),                                     # Italique
                    (r"\~\~(.*?)\~\~", r"\033[9m\1\033[0m"),                               # Barré
                    (r"\`(.*?)\`", r"\033[2m\1\033[0m"),                                   # Code
                    (r"(?<!\033)\[(.*?)\]\((.*?)\)", r"\033]8;;\2\033\\\1\033]8;;\033\\"), # Lien
                ]
                
                for pattern, replacement in replacements : # Applique les remplacements markdown -> ANSI
                    line = re.sub(pattern, replacement, line)

                output.append(line)
        
        return "\n".join(output)  # Retourne le texte formaté