using System;

namespace Day_17
{
    class Pos
    {
        public int x;
        public int y;
        public int vx;
        public int vy;
        public void Step()
        {
            x += vx;
            y += vy;
            if (vx > 0)
                vx--;
            else if (vx < 0)
                vx++;
            vy--;
        }

        internal bool IsWithin(int x1, int x2, int y1, int y2)
        {
            return (x >= x1 && x <= x2 && y >= y1 && y <= y2);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            //int x1 = 20;
            //int x2 = 30;
            //int y1 = -10;
            //int y2 = -5;
            int x1 = 81;
            int x2 = 129;
            int y1 = -150;
            int y2 = -108;
            Pos p = new Pos();
            int highestY = 0;
            int num = 0;
            for (int vy = -150; vy < 10000; vy++)
            {
                for (int vx = 0; vx < 200; vx++)
                {
                    int roundHighestY = 0;
                    if (vy == 9 && vx == 6)
                        p.x = 0;
                    p.x = 0;
                    p.y = 0;
                    p.vx = vx;
                    p.vy = vy;
                    do
                    {
                        p.Step();
                        if (p.y > roundHighestY)
                            roundHighestY = p.y;
                        if (p.IsWithin(x1, x2, y1, y2))
                        {
                            num++;
                            if (roundHighestY > highestY)
                                highestY = roundHighestY;
                                break;
                        }
                        if (p.x > x2)
                            break;
                        if (p.vx == 0 && p.y < y1)
                            break;
                    } while (true);
                }
            }
            Console.WriteLine(highestY);
            Console.WriteLine(num);
        }

    }
}
