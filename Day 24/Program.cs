
namespace Day_24
{
    class Program
    {
        static private int[] vars = new int[4];
        static private string[] lines = new string[0];
        static void Main(string[] args)
        {
            lines = System.IO.File.ReadAllLines("../../../input.txt");
            int[] input = new int[14];
            for (int i = 0; i < 14; i++)
                input[i] = 9;

            List<AluProgram> programs = new();
            for (int i = 0; i < 14; i++)
                programs.Add(new());
            int p = -1;
            foreach (string line in lines)
            { 
                if (line.Substring(0, 3) == "inp")
                {
                    p++;
                }
                programs[p].AddCode(line);
            }
            for (int i = 0; i < 14; i++)
                programs[i].RunPrograms();

            //inp w     w=x1
            //mul x 0   x=0
            //add x z   x=0
            //mod x 26  x=0
            //div z 1   z=0
            //add x 11  x=11
            //eql x w   x=0 (x was < 10)
            //eql x 0   x=1
            //mul y 0   y=0
            //add y 25  y=25
            //mul y x   y=25
            //add y 1   y=26
            //mul z y   z=0
            //mul y 0   y=0
            //add y w   y=x1
            //add y 6   y=x1+6
            //mul y x   y=x1+6
            //add z y   z=x1+6

            //inp w     w=x2
            //mul x 0   x=0
            //add x z   x=0   
            //mod x 26  x=0
            //div z 1   z=x1+6
            //add x 13  x=13
            //eql x w   x=0 (x was < 10)
            //eql x 0   x=1
            //mul y 0   y=0
            //add y 25  y=25
            //mul y x   y=25
            //add y 1   y=26
            //mul z y   z=(x1+6)*26
            //mul y 0   y=0
            //add y w   y=x2
            //add y 14  y=x2+14
            //mul y x   y=x2+14
            //add z y   z=(x1+6)*26 + x2+14

            //inp w     w=x3
            //mul x 0   x=0
            //add x z   x=(x1+6)*26 + x2+14
            //mod x 26  x=x2+14
            //div z 1   z=(x1+6)*26 + x2+14
            //add x 15  x=x2+14+15
            //eql x w   x=0
            //eql x 0   x=1
            //mul y 0   y=0
            //add y 25  y=25
            //mul y x   y=25
            //add y 1   y=26
            //mul z y   z=((x1+6)*26 + x2+14)*26
            //mul y 0   y=0
            //add y w   y=x3
            //add y 14  y=x3+14
            //mul y x   y=x3+14
            //add z y   z=((x1+6)*26 + x2+14)*26 + x3+14

            //inp w     w=x4
            //mul x 0   x=0
            //add x z   x=((x1+6)*26 + x2+14)*26 + x3+14
            //mod x 26  x=x3+14
            //div z 26  z=(x1+6)*26 + x2+14
            //add x -8  x=x3+6
            //eql x w   x=(x3+6 == x4)
            //eql x 0   x=(x3+6 != x4)
            //mul y 0   y=0
            //add y 25  y=25
            //mul y x   y=(x3+6 != x4)*25
            //add y 1   y=(x3+6 != x4)*25 + 1
            //mul z y   z=((x1+6)*26 + x2+14) * ((x3+6 != x4)*25 + 1)
            //mul y 0   y=0
            //add y w   y=x4
            //add y 10  y=x4+10
            //mul y x   y=(x4+10) * (x3+6 != x4)
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 1
            //add x 13
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 9
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 1
            //add x 15
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 12
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 26
            //add x -11
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 8
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 26
            //add x -4
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 13
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 26
            //add x -15
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 12
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 1
            //add x 14
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 6
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 1
            //add x 14
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 9
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 26
            //add x -1
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 15
            //mul y x
            //add z y
            //inp w
            //mul x 0
            //add x z
            //mod x 26
            //div z 26
            //add x -8
            //eql x w
            //eql x 0
            //mul y 0
            //add y 25
            //mul y x
            //add y 1
            //mul z y
            //mul y 0
            //add y w
            //add y 4
            //mul y x
            //add z y   z=z + y -> 

            //inp w     w=x14
            //mul x 0   x=0
            //add x z   x=z13
            //mod x 26  x=z13%26
            //div z 26  z=z13/26
            //add x -14 x=(z13%26)-14
            //eql x w   x=((z13%26)-14 == x14)
            //eql x 0   x=((z13%26)-14 != x14)
            //mul y 0   y=0
            //add y 25  y=25
            //mul y x   y=25 * ((z13%26)-14 != x14)
            //add y 1   y=25 * ((z13%26)-14 != x14) + 1
            //mul z y   z=(25 * ((z13%26)-14 != x14) + 1) * z13
            //mul y 0   y=0
            //add y w   y=x14
            //add y 10  y=x14+10
            //mul y x   y=(x14+10) * (25 * ((z13%26)-14 != x14) + 1) * z13 -> (25 * ((z13%26)-14 != x14) + 1) * z13 == 0 -> z13=0
            //add z y   z=z + y

            List<Tuple<int, string>> needs = new();
            List<Tuple<int, string>> newNeeds = new();
            needs.Add(new(0, ""));
            for (int j = 13; j >= 0; j--)
            {
                Console.WriteLine("Processing " + j);
                for (int i = -1000000; i < 1000000; i++)
                {
                    for (int x = 9; x > 0; x--)
                    {
                        programs[j].RunOnce(new int[] { 0, 0, 0, i }, x);
                        foreach (Tuple<int, string> need in needs)
                        {
                            if (vars[3] == need.Item1)
                            {
                                // Only add if not exists
                                bool found = false;
                                foreach (Tuple<int, string> newNeed in newNeeds)
                                {
                                    if (i == newNeed.Item1)
                                    {
                                        found = true;
                                        break;
                                    }
                                }
                                if (!found)
                                {
                                    newNeeds.Add(new(i, need.Item2 + (char)('0' + x)));
                                }
                            }
                        }
                    }
                }
                needs = newNeeds;
                newNeeds = new();
            }
            foreach (Tuple<int, string> need in needs)
            {
                if (need.Item1 == 0)
                {
                    Console.WriteLine(need.Item2);
                }
            }


            needs = new();
            newNeeds = new();
            needs.Add(new(0, ""));
            for (int j = 13; j >= 0; j--)
            {
                Console.WriteLine("Processing " + j);
                for (int i = -1000000; i < 1000000; i++)
                {
                    for (int x = 1; x < 10; x++)
                    {
                        programs[j].RunOnce(new int[] { 0, 0, 0, i }, x);
                        foreach (Tuple<int, string> need in needs)
                        {
                            if (vars[3] == need.Item1)
                            {
                                // Only add if not exists
                                bool found = false;
                                foreach (Tuple<int, string> newNeed in newNeeds)
                                {
                                    if (i == newNeed.Item1)
                                    {
                                        found = true;
                                        break;
                                    }
                                }
                                if (!found)
                                {
                                    newNeeds.Add(new(i, need.Item2 + (char)('0' + x)));
                                }
                            }
                        }
                    }
                }
                needs = newNeeds;
                newNeeds = new();
            }
            foreach (Tuple <int, string> need in needs)
            {
                if (need.Item1 == 0)
                {
                    Console.WriteLine(need.Item2);
                }
            }

            //List<Tuple<string, int[]>> results = new();
            //results.Add(new Tuple<string, int[]>("", new int[] { 0, 0, 0, 0 }));
            //for (int i = 0; i < 14; i++)
            //{
            //    Console.WriteLine("Processing " + i);
            //    List<Tuple<string, int[]>> newResults = new();
            //    foreach (Tuple<string, int[]> result in results)
            //    {
            //        for (int j = 9; j > 0; j--)
            //        {
            //            programs[i].RunOnce(result.Item2, j);
            //            bool found = false;
            //            // Fix values
            //            vars[0] = 0;
            //            vars[1] = 0;
            //            vars[2] = 0;
            //            foreach (Tuple<string, int[]> newResult in newResults)
            //            {
            //                bool ok = true;
            //                for (int k = 0; k < 4; k++)
            //                {
            //                    if (vars[k] != newResult.Item2[k])
            //                    {
            //                        ok = false;
            //                        break;
            //                    }
            //                }
            //                if (ok)
            //                {
            //                    found = true;
            //                    break;
            //                }
            //            }
            //            if (!found)
            //                newResults.Add(new(result.Item1 + (char)('0' + j), new int[] { vars[0], vars[1], vars[2], vars[3] }));
            //        }
            //    }
            //    //z[0] = 6 + v
            //    //z[1] = z[0] + 6 + v
            //    //413 405 380


            //    //foreach (Tuple<string, int[]> newResult in newResults)
            //    //{
            //    //    Console.Write(newResult.Item2[3]);
            //    //}
            //    results = newResults;
            //    newResults = new();
            //}
            //foreach (Tuple<string, int[]> result in results)
            //{
            //    if (result.Item2[3] == 0)
            //    {
            //        Console.WriteLine(results[0].Item1);
            //        break;
            //    }
            //}

            //while (true)
            //{
            //    RunProgram(input);
            //    if (vars[3] == 0)
            //        break;
            //    int pos = 13;
            //    while (input[pos] == 1)
            //    {
            //        input[pos] = 9;
            //        pos--;
            //    }
            //    input[pos]--;
            //}
            //for (int i = 0; i < 14; i++)
            //    Console.Write(input[i]);
            Console.WriteLine();
            //Console.WriteLine("w = " + vars[0]);
            //Console.WriteLine("x = " + vars[1]);
            //Console.WriteLine("y = " + vars[2]);
            //Console.WriteLine("z = " + vars[3]);
        }
        //w = inp
        //x = 1
        //y = 6 + w
        //z = 6 + w

        //w = inp
        //x = 1 // (6 + w) % 26 + 13 != 1
        //y = 26
        //z = 26 * (6 + w)

        // 
        private static void RunProgram(List<string> code, int[] input)
        {
            int readPos = 0;
            foreach (string line in code)
            {
                string[] cmd = line.Split(' ');
                switch (cmd[0])
                {
                    case "inp":
                        vars[cmd[1][0] - 'w'] = input[readPos++];
                        break;
                    case "add":
                        vars[cmd[1][0] - 'w'] += GetValue(cmd[2]);
                        break;
                    case "mul":
                        vars[cmd[1][0] - 'w'] *= GetValue(cmd[2]);
                        break;
                    case "div":
                        vars[cmd[1][0] - 'w'] /= GetValue(cmd[2]);
                        break;
                    case "mod":
                        vars[cmd[1][0] - 'w'] %= GetValue(cmd[2]);
                        break;
                    case "eql":
                        if (vars[cmd[1][0] - 'w'] == GetValue(cmd[2]))
                            vars[cmd[1][0] - 'w'] = 1;
                        else
                            vars[cmd[1][0] - 'w'] = 0;
                        break;
                    default:
                        throw new Exception("");
                }
            }
        }

        private static int GetValue(string v)
        {
            switch (v)
            {
                case "w":
                    return vars[0];
                case "x":
                    return vars[1];
                case "y":
                    return vars[2];
                case "z":
                    return vars[3];
                default:
                    return int.Parse(v);
            }
        }

        private class AluProgram
        {
            List<string> code = new List<string>();
            int[] results = new int[4 * 9];
            internal void AddCode(string line)
            {
                code.Add(line);
            }

            internal void RunOnce(int[] vs, int v)
            {
                for (int i = 0; i < 4; i++)
                    vars[i] = vs[i];
                RunProgram(code, new int[] { v });
            }

            internal void RunPrograms()
            {
                for (int i = 1; i < 10; i++)
                {
                    vars[0] = 0;
                    vars[1] = 0;
                    vars[2] = 0;
                    vars[3] = 0;
                    RunProgram(code, new int[] { i });
                    results[(i - 1) * 4 + 0] = vars[0];
                    results[(i - 1) * 4 + 1] = vars[1];
                    results[(i - 1) * 4 + 2] = vars[2];
                    results[(i - 1) * 4 + 3] = vars[3];
                }
            }
        }
    }
}
