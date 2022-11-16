
namespace Day_22
{
    class Program
    {
        static bool[] grid = new bool[101 * 101 * 101];
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Command> commands = new List<Command>();
            foreach (string line in lines)
            {
                commands.Add(new(line));
            }    
            foreach (Command command in commands)
            {
                command.Process(grid);
            }
            long num = 0;
            for (int z = -50; z < 51; z++)
            {
                for (int y = -50; y < 51; y++)
                {
                    for (int x = -50; x < 51; x++)
                    {
                        if (grid[(z + 50) * 101 * 101 + (y + 50) * 101 + x + 50])
                            num++;
                    }
                }
            }
            Console.WriteLine(num);
            //
            // Part 2
            //

            List<Command> newCommands = new();
            List<Command> processCommands = new();
            for (int i = 0; i < commands.Count; i++)
            {
                processCommands.Add(commands[i]);
                while (processCommands.Count > 0)
                {
                    bool intersects = false;
                    for (int j = 0; j < newCommands.Count; j++)
                    {
                        if (processCommands[0].Intersect(newCommands[j]))
                        {
                            intersects = true;
                            List<Command> newRange = processCommands[0].RunMerge(newCommands[j]);
                            processCommands.AddRange(newRange);
                            newCommands.RemoveAt(j);
                            if (newRange.Count > 0 && processCommands[0].on)
                                processCommands.RemoveAt(0);
                            j--;
                        }
                    }
                    if (!intersects)
                    {
                        if (processCommands[0].on)
                            newCommands.Add(processCommands[0]);
                        processCommands.RemoveAt(0);
                    }
                }
            }
            num = 0;
            foreach (Command command in newCommands)
            {
                //if (command.fromCoords[0] > 50 ||
                //    command.toCoords[0] < -50)
                //    continue;
                //if (command.fromCoords[1] > 50 ||
                //    command.toCoords[1] < -50)
                //    continue;
                //if (command.fromCoords[2] > 50 ||
                //    command.toCoords[2] < -50)
                //    continue;
                //long x = Math.Min(50, command.toCoords[0]) - Math.Max(-50, command.fromCoords[0]) + 1;
                //long y = Math.Min(50, command.toCoords[1]) - Math.Max(-50, command.fromCoords[1]) + 1;
                //long z = Math.Min(50, command.toCoords[2]) - Math.Max(-50, command.fromCoords[2]) + 1;
                long x = (command.toCoords[0] - command.fromCoords[0] + 1);
                long y = (command.toCoords[1] - command.fromCoords[1] + 1);
                long z = (command.toCoords[2] - command.fromCoords[2] + 1);
                num += x * y * z;
            }
            Console.WriteLine(num);
        }

        private class Command
        {
            internal bool on;
            internal int[] fromCoords;
            internal int[] toCoords;

            public Command(string line)
            {
                fromCoords = new int[3];
                toCoords = new int[3];
                string[] l = line.Split(' ');
                if (l[0] == "on")
                    on = true;
                else
                    on = false;
                l = l[1].Split(',');
                for (int i = 0; i < 3; i++)
                {
                    string[] n = l[i].Substring(2).Split("..");
                    fromCoords[i] = int.Parse(n[0]);
                    toCoords[i] = int.Parse(n[1]);
                }
            }

            public Command(bool on, int[] fromCoords, int[] toCoords)
            {
                this.on = on;
                this.fromCoords = new int[3];
                this.toCoords = new int[3];
                for (int i = 0; i < 3; i++)
                {
                    this.fromCoords[i] = fromCoords[i];
                    this.toCoords[i] = toCoords[i];
                }
            }

            internal bool Intersect(Command command)
            {
                if (fromCoords[0] > command.toCoords[0] || toCoords[0] < command.fromCoords[0])
                    return false;
                if (fromCoords[1] > command.toCoords[1] || toCoords[1] < command.fromCoords[1])
                    return false;
                if (fromCoords[2] > command.toCoords[2] || toCoords[2] < command.fromCoords[2])
                    return false;
                return true;
            }

            internal void Process(bool[] grid)
            {
                for (int z = Math.Max(-50, fromCoords[0]); z < Math.Min(50, toCoords[0]) + 1; z++)
                {
                    for (int y = Math.Max(-50, fromCoords[1]); y < Math.Min(50, toCoords[1]) + 1; y++)
                    {
                        for (int x = Math.Max(-50, fromCoords[2]); x < Math.Min(50, toCoords[2]) + 1; x++)
                        {
                            grid[(z + 50) * 101 * 101 + (y + 50) * 101 + x + 50] = on;
                        }
                    }
                }
            }

            internal List<Command> RunMerge(Command command)
            {
                // off + off of off + on yields no
                if (!command.on)
                    return new();

                // on + on yields 15
                //  on + off yields 7
                List<int>[] l = new List<int>[] { new(), new(), new() };
                for (int i = 0; i < 3; i++)
                {
                    l[i].Add(fromCoords[i]);
                    l[i].Add(toCoords[i]);
                    l[i].Add(command.fromCoords[i]);
                    l[i].Add(command.toCoords[i]);
                    l[i].Sort();
                }
                List<Command> newCommands = new();
                // Create 27 subes and check which should be included
                Command cmd;
                for (int z = 0; z < 3; z++)
                {
                    for (int y = 0; y < 3; y++)
                    {
                        for (int x = 0; x < 3; x++)
                        {
                            cmd = new Command(true,
                                new int[] { l[0][x], l[1][y], l[2][z] },
                                new int[] { l[0][x + 1], l[1][y + 1], l[2][z + 1] });
                            // Adjust to not overlap
                            if (x == 0)
                                cmd.toCoords[0]--;
                            if (x == 2)
                                cmd.fromCoords[0]++;
                            if (y == 0)
                                cmd.toCoords[1]--;
                            if (y == 2)
                                cmd.fromCoords[1]++;
                            if (z == 0)
                                cmd.toCoords[2]--;
                            if (z == 2)
                                cmd.fromCoords[2]++;
                            if (ShouldAdd(cmd, command))
                                newCommands.Add(cmd);
                        }
                    }
                }
                
                return newCommands;
            }

            private bool ShouldAdd(Command toAdd, Command second)
            {
                // Check if no cube
                if (toAdd.toCoords[0] < toAdd.fromCoords[0] ||
                    toAdd.toCoords[1] < toAdd.fromCoords[1] ||
                    toAdd.toCoords[2] < toAdd.fromCoords[2])
                    return false;
                if (Intersect(toAdd))
                {
                    if (!on)
                        return false;
                    else
                        return true;
                }
                if (second.Intersect(toAdd))
                {
                    if (!second.on)
                        return false;
                    else
                        return true;
                }
                return false;
            }
        }
    }
}
