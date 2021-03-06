from PIL import Image
import matplotlib.pyplot as plt


# Route n-queens based on algorithm selected.
def queens(n = 4, algo = "branch"):

    print("n-queens",n)

    if algo == "branch":
        # get no of solution possible and their position as list
        count, pos = nqueens_branch(n)
    else:
        # get no of solution possible and their position as list
        count, pos = nqueens_backtrack(n)


# Use Branch and bound to solve the problem.
def nqueens_branch(n):
    # Set initial count to 0
    count = 0
    pos = []
    return count, pos


# Use Backtracking to solve the problem.
def nqueens_backtrack(n):
    count = 0
    # ist to hold queen positions
    pos = []
    print("N =", n, "in backtrack")
    return count, pos

# Print the possible soultions as 0,1 on board
def show():
    pass


# Display the solution as an image
def display(queen_data):
    try:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        table = ax.table(cellText = queen_data, loc='center')
        table.set_fontsize(14)
        table.scale(1, 5)

        ax.axis('off')
        plt.show()
    except Exception as ex:
        print(ex)


# save the n queens image
def save(queen_data, img_name = "nqueen_solution"):
    try:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)

        table = ax.table(cellText = queen_data, loc='center')
        table.set_fontsize(14)
        table.scale(1,5)

        ax.axis('off')
        plt.savefig(img_name)
    except Exception as ex:
        print(ex)

# Get an image and identify the n-value, no of queens and position of queens if present.
def scan_queen(image_path):
    try:
        n = 0
        count = 0
        pos = []

        img = Image.open(image_path).convert('RGB')
        pixel = img.load()

        width = img.size[0]
        height = img.size[1]

        white = (255, 255, 255)

        for i in range(width - 1):
            if pixel[i, (height/2)] == white and pixel[i+1, (height/2)] != white:
                n += 1

        print("No of Rows identified is ", n-1)

        return count, pos, n-1
    except Exception as ex:
        print(ex)

# Solve nqueens if queens are present at a position.
def position_solver(n, pos):
    count = 0
    pos = []
    return count, pos


# Solve n-queens for an image
def image_solver(image_path):
    try:
        count, pos, n = scan_queen(image_path)

        if len(pos) == 0 :
            nqueens_backtrack(n)
        else:
            position_solver(n, pos)
    except Exception as ex:
        print(ex)

# Return Positions and solution space as audio.
def alexa():
    pass
