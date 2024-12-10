import curses
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Initialize variables (intentionally leave out ’random’ and ’obstacles’ for now)
    sh, sw = stdscr.getmaxyx()
    w = sw // 2
    dino = [sh - 2, w]
    score = 0
    jump = False
    jump_height = 5
    jump_count = 0

    # NOTE: Obstacle logic is missing here intentionally
    # We’ll add it later on another branch, causing a merge conflict.

    while True:
        stdscr.clear()

        # Display Dino (using "D", but in the future we might change this character)
        stdscr.addstr(dino[0], dino[1], "@")

        # For now, no obstacle logic. Just increment score.
        score += 1
        stdscr.addstr(0, 0, f"Score: {score}")

        # Handle jump logic (no changes needed here)
        if jump:
            if jump_count < jump_height:
                dino[0] -= 1
                jump_count += 1
            else:
                jump = False
        else:
            if dino[0] < sh - 2:
                dino[0] += 1
            else:
                jump_count = 0

        # Check for user input (no obstacle checks here)
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == ord(' ') and dino[0] == sh - 2:
            jump = True

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
