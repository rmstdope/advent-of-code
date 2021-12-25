namespace Day_25
{
    class Program
    {
        static void Main(string[] _)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            char[][] cucomber = new char[lines.Length][];
            bool[][] canMove = new bool[lines.Length][];
            for (int i = 0; i < lines.Length; i++)
            {
                canMove[i] = new bool[lines[i].Length];
                cucomber[i] = new char[lines[i].Length];
                for (int j = 0; j < cucomber[i].Length; j++)
                {
                    cucomber[i][j] = lines[i][j];
                    canMove[i][j] = false;
                }
            }
            bool moved;
            long numMoves = 0;
            do
            {
                moved = false;
                // Check east
                for (int i = 0; i < cucomber.Length; i++)
                {
                    for (int j = 0; j < cucomber[i].Length; j++)
                    {
                        if (cucomber[i][j] == '>')
                        {
                            int j2 = j + 1;
                            if (j2 >= cucomber[i].Length)
                                j2 = 0;
                            if (cucomber[i][j2] == '.')
                                canMove[i][j] = true;
                            else
                                canMove[i][j] = false;
                        }
                    }
                }
                // Move east
                for (int i = 0; i < cucomber.Length; i++)
                {
                    for (int j = 0; j < cucomber[i].Length; j++)
                    {
                        if (cucomber[i][j] == '>' && canMove[i][j])
                        {
                            moved = true;
                            int j2 = j + 1;
                            if (j2 >= cucomber[i].Length)
                                j2 = 0;
                            cucomber[i][j] = '.';
                            cucomber[i][j2] = '>';
                            canMove[i][j] = false;
                        }
                    }
                }
                // Check south
                for (int i = 0; i < cucomber.Length; i++)
                {
                    for (int j = 0; j < cucomber[i].Length; j++)
                    {
                        if (cucomber[i][j] == 'v')
                        {
                            int i2 = i + 1;
                            if (i2 >= cucomber.Length)
                                i2 = 0;
                            if (cucomber[i2][j] == '.')
                                canMove[i][j] = true;
                            else
                                canMove[i][j] = false;
                        }
                    }
                }
                // Move south
                for (int i = 0; i < cucomber.Length; i++)
                {
                    for (int j = 0; j < cucomber[i].Length; j++)
                    {
                        if (cucomber[i][j] == 'v' && canMove[i][j])
                        {
                            moved = true;
                            int i2 = i + 1;
                            if (i2 >= cucomber.Length)
                                i2 = 0;
                            cucomber[i][j] = '.';
                            cucomber[i2][j] = 'v';
                            canMove[i][j] = false;
                        }
                    }
                }
                if (moved)
                {
                    numMoves++;
                    //Console.WriteLine($"Making move {numMoves}.");
                    //if (numMoves == 40)
                    //{
                    //    for (int i = 0; i < cucomber.Length; i++)
                    //    {
                    //        for (int j = 0; j < cucomber[i].Length; j++)
                    //        {
                    //            Console.Write(cucomber[i][j]);
                    //        }
                    //        Console.WriteLine();
                    //    }
                    //}
                }
            } while (moved);
            Console.WriteLine(numMoves);
        }
    }
}
