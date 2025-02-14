import os
import sys
if os.name == "nt":
    import msvcrt

    class Keyboard :
        """
        Classe contenant les caractères de contrôle pour Windows.
        """

        TOP         = "^[H"    # top
        DOWN        = "^[P"    # down
        RIGHT       = "^[M"    # right
        LEFT        = "^[K"    # left
        DEL         = "^[S"    # del
        END         = "^[O"    # end
        NL          = "\r"     # newline
        TAB         = "\t"     # tab
        BS          = "\x08"   # backspace
        ctrl_A      = "\x01"   # ctrl+A
        ctrl_Z      = "\x1a"   # ctrl+Z
        ctrl_E      = "\x05"   # ctrl+E
        ctrl_R      = "\x12"   # ctrl+R
        ctrl_T      = "\x14"   # ctrl+T
        ctrl_Y      = "\x19"   # ctrl+Y
        ctrl_U      = "\x15"   # ctrl+U
        ctrl_I      = "\t"     # ctrl+I
        ctrl_O      = "\x0f"   # ctrl+O
        ctrl_P      = "\x10"   # ctrl+P
        ctrl_Q      = "\x11"   # ctrl+Q
        ctrl_S      = "\x13"   # ctrl+S
        ctrl_D      = "\x04"   # ctrl+D
        ctrl_F      = "\x06"   # ctrl+F
        ctrl_G      = "\x07"   # ctrl+G
        ctrl_H      = "\x08"   # ctrl+H
        ctrl_J      = "\n"     # ctrl+J
        ctrl_K      = "\x0b"   # ctrl+K
        ctrl_L      = "\x0c"   # ctrl+L
        ctrl_M      = "\r"     # ctrl+M
        ctrl_W      = "\x17"   # ctrl+W
        ctrl_X      = "\x18"   # ctrl+X
        ctrl_C      = "\x03"   # ctrl+C
        ctrl_B      = "\x02"   # ctrl+B
        ctrl_N      = "\x0e"   # ctrl+N
        ctrl_UP     = "^[\x8d" # ctrl+UP
        ctrl_DOWN   = "^[\x91" # ctrl+DOWN
        ctrl_LEFT   = "^[s"    # ctrl+LEFT
        ctrl_RIGHT  = "^[t"    # ctrl+RIGHT
        ctrl_NL     = "\n"     # ctrl+newline
        ctrl_BS     = "\x7f"   # ctrl+backspace
        ctrl_AST    = "\x1c"   # ctrl+*
        ctrl_DOLLAR = "\x1d"   # ctrl+$

        @staticmethod
        def ctrl(char:str) -> str :
            """
            Retourne le caractère de contrôle associé à un caractère (pour Windows).

            Parameters:
            -----------
            char : str
                caractère à transformer
            
            Returns:
            --------
            str
                caractère de contrôle associé
            """

            assert type(char) == str, "char is not a str"

            ctrl_char = {
                "\x01" : "^A", "\x1a" : "^Z", "\x05" : "^E", "\x12" : "^R",
                "\x14" : "^T", "\x19" : "^Y", "\x15" : "^U", "\t"   : "^I",
                "\x0f" : "^O", "\x10" : "^P", "\x11" : "^Q", "\x13" : "^S",
                "\x04" : "^D", "\x06" : "^F", "\x07" : "^G", "\x08" : "^H",
                "\n"   : "^J", "\x0b" : "^K", "\x0c" : "^L", "\r"   : "^M",
                "\x17" : "^W", "\x18" : "^X", "\x03" : "^C", "\x02" : "^B",
                "\x0e" : "^N",
                "^[\x8d": "^UP"  , "^[\x91": "^DOWN" ,
                "^[s"   : "^LEFT", "^[t"   : "^RIGHT",
                "\n"    : "\n"   , "\x7f"  : "^BACK" ,
                "\x1c" : "^*", "\x1d" : "^$",
            }

            return ctrl_char.get(char)
    
        @staticmethod
        def getch() -> str :
            """
            Attend la frappe d'un caractère puis le retourne (pour Windows).
            
            Returns:
            --------
            str
                caractère fr
            """

            sys.stdout.flush()
            ch = ""

            ch = msvcrt.getwch()

            if ord(ch) == 224 :
                ch = "^[" + Keyboard.getch()

            return ch
else:
    import tty
    import termios

    class Keyboard:
        """
        Classe contenant les caractères de contrôle pour Linux.
        """

        TOP         = "^[[A"    # top
        DOWN        = "^[[B"    # down
        RIGHT       = "^[[C"    # right
        LEFT        = "^[[D"    # left
        DEL         = "^[[3~"   # del
        END         = "^[[F"    # end
        NL          = "\r"      # newline
        TAB         = "\t"      # tab
        BS          = "\x7f"    # backspace
        ctrl_A      = "\x01"    # ctrl+A
        ctrl_Z      = "\x1a"    # ctrl+Z
        ctrl_E      = "\x05"    # ctrl+E
        ctrl_R      = "\x12"    # ctrl+R
        ctrl_T      = "\x14"    # ctrl+T
        ctrl_Y      = "\x19"    # ctrl+Y
        ctrl_U      = "\x15"    # ctrl+U
        ctrl_I      = "\t"      # ctrl+I
        ctrl_O      = "\x0f"    # ctrl+O
        ctrl_P      = "\x10"    # ctrl+P
        ctrl_Q      = "\x11"    # ctrl+Q
        ctrl_S      = "\x13"    # ctrl+S
        ctrl_D      = "\x04"    # ctrl+D
        ctrl_F      = "\x06"    # ctrl+F
        ctrl_G      = "\x07"    # ctrl+G
        ctrl_H      = "\x08"    # ctrl+H
        ctrl_J      = "\n"      # ctrl+J
        ctrl_K      = "\x0b"    # ctrl+K
        ctrl_L      = "\x0c"    # ctrl+L
        ctrl_M      = "\r"      # ctrl+M
        ctrl_W      = "\x17"    # ctrl+W
        ctrl_X      = "\x18"    # ctrl+X
        ctrl_C      = "\x03"    # ctrl+C
        ctrl_B      = "\x02"    # ctrl+B
        ctrl_N      = "\x0e"    # ctrl+N
        ctrl_UP     = "^[[1;5A" # ctrl+UP
        ctrl_DOWN   = "^[[1;5B" # ctrl+DOWN
        ctrl_LEFT   = "^[[1;5D" # ctrl+LEFT
        ctrl_RIGHT  = "^[[1;5C" # ctrl+RIGHT
        ctrl_NL     = "\n"      # ctrl+newline
        ctrl_BS     = "\x08"    # ctrl+backspace
        ctrl_AST    = "\x1c"    # ctrl+*
        ctrl_DOLLAR = "\x1d"    # ctrl+$

        @staticmethod
        def ctrl(char:str) -> str :
            """
            Retourne le caractère de contrôle associé à un caractère (pour Linux).

            Parameters:
            -----------
            char : str
                caractère à transformer
            
            Returns:
            --------
            str
                caractère de contrôle associé
            """

            assert type(char) == str, "char is not a str"
            
            ctrl_char = {
                "\x01" : "^A", "\x1a" : "^Z", "\x05" : "^E", "\x12" : "^R",
                "\x14" : "^T", "\x19" : "^Y", "\x15" : "^U", "\t"   : "^I",
                "\x0f" : "^O", "\x10" : "^P", "\x11" : "^Q", "\x13" : "^S",
                "\x04" : "^D", "\x06" : "^F", "\x07" : "^G", "\x08" : "^H",
                "\n"   : "^J", "\x0b" : "^K", "\x0c" : "^L", "\r"   : "^M",
                "\x17" : "^W", "\x18" : "^X", "\x03" : "^C", "\x02" : "^B",
                "\x0e" : "^N",
                "^[[1;5A": "^UP"  , "^[[1;5B": "^DOWN" ,
                "^[[1;5D": "^LEFT", "^[[1;5C": "^RIGHT",
                "\n"     : "\n"   , "\x08"   : "^BACK" ,
                "\x1c" : "^*", "\x1d" : "^$",
            }
            
            return ctrl_char.get(char)

        def getch() -> str :
            """
            Attend la frappe d'un caractère puis le retourne (pour Linux).
            
            Returns:
            --------
            str
                caractère fr
            """
        

            sys.stdout.flush()
            ch = ""

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try :
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally :
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            if ord(ch) == 27 :
                _ch = Keyboard.getch()
                _ch += Keyboard.getch()

                while _ch[-1].isnumeric() or _ch[-1] == ";" :
                    _ch += Keyboard.getch()

                ch = "^[" + _ch

            return ch