import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Initialize variables
    sh, sw = stdscr.getmaxyx()
    w = sw // 2
    dino = [sh - 2, w]
    obstacles = []
    score = 0
    jump = False
    jump_height = 5
    jump_count = 0

    while True:
        stdscr.clear()

        # Display Dino
        stdscr.addstr(dino[0], dino[1], "D")

        # Add obstacles
        if random.randint(0, 10) == 0:
            obstacles.append([sh - 2, sw - 1])

        # Move obstacles and detect collision
        for obstacle in obstacles[:]:
            obstacle[1] -= 1
            if obstacle[1] == dino[1] and obstacle[0] == dino[0]:
                stdscr.addstr(sh // 2, sw // 2 - 5, "GAME OVER!")
                stdscr.refresh()
                time.sleep(2)
                return
            if obstacle[1] < 0:
                obstacles.remove(obstacle)

        # Display obstacles
        for obstacle in obstacles:
            stdscr.addstr(obstacle[0], obstacle[1], "X")

        # Handle jump
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

        # Display score
        score += 1
        stdscr.addstr(0, 0, f"Score: {score}")

        # Check for user input
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == ord(' ') and dino[0] == sh - 2:  # Jump if on the ground
            jump = True

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
