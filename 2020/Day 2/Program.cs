using System;
using System.Linq;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            int num1 = 0;
            int num2 = 0;
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            foreach (string line in lines) 
            {
                string[] arr = line.Split(' ');
                int c = arr[2].Count(f => f == arr[1][0]);
                string[] toFrom = arr[0].Split('-');
                int fromNum = Int32.Parse(toFrom[0]);
                int toNum = Int32.Parse(toFrom[1]);
                if (fromNum <= c && toNum >= c)
                {
                    num1++;
                }
                int f1 = arr[2][fromNum - 1] == arr[1][0] ? 1 : 0;
                int f2 = arr[2][toNum - 1] == arr[1][0] ? 1 : 0;
                if (f1 + f2 == 1)
                {
                    num2++;
                }
            }
            Console.WriteLine(num1);
            Console.WriteLine(num2);
        }
    }
}
