basic.show_leds("""
    . . . . .
        . . # . .
        . . . . .
        . . # . .
        . . . . .
""")

def on_forever():
    basic.show_leds("""
        . . . . .
                . . # . .
                . . . . .
                . . # . .
                . . . . .
    """)
basic.forever(on_forever)
