import math

def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges using pure Python lists.
    """
    n = len(image)
    m = len(image[0])

    # Create padded 2D list with zeros
    padded = [[0 for _ in range(m+2)] for _ in range(n+2)]

    # Copy image into padded version
    for i in range(n):
        for j in range(m):
            padded[i+1][j+1] = image[i][j]

    # Sobel kernels (still 2D lists)
    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    Ky = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]

    # Output image
    output = [[0 for _ in range(m)] for _ in range(n)]

    # Convolution
    for i in range(1, n+1):
        for j in range(1, m+1):
            gx = 0
            gy = 0

            # Apply 3×3 kernels manually
            for ki in range(3):
                for kj in range(3):
                    pixel = padded[i-1 + ki][j-1 + kj]
                    gx += pixel * Kx[ki][kj]
                    gy += pixel * Ky[ki][kj]

            output[i-1][j-1] = math.sqrt(gx*gx + gy*gy)

    return output
