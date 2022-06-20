def main():
    T = int(input());

    for t in range(T):
        board = []

        countlive = 0;

        for i in range(5):
            l = input();
            ls = list(map(int, l))
            countlive += ls.count(1);
            board.append(ls);

        ## now board is ready

       newGrid = board.copy()
        for i in range(5):
            for j in range(5):
     
                # compute 8-neighbor sum
                # using toroidal boundary conditions - x and y wrap around
                # so that the simulaton takes place on a toroidal surface.
                total = int((grid[i][ (j-1)%N] + grid[i][ (j+1)%N] +
                             grid[(i-1)%N][ j] + grid[(i+1   )%N][ j] +
                             grid[(i-1)%N][ (j-1)%N] + grid[(i-1)%N][ (j+1)%N] +
                             grid[(i+1)%N][ (j-1)%N] + grid[(i+1)%N][ (j+1)%N])/255)
     
                # apply Conway's rules
                if grid[i, j]  == ON:
                    if (total < 2) or (total > 3):
                        newGrid[i][ j] = OFF
                else:
                    if total == 3:
                        newGrid[i][ j] = ON


if __name__ == '__main__':
    main()
