using System;
using System.Collections.Generic;

namespace Day_16
{
    class Program
    {
        static private string bin;
        static private int numRead;
        static private int sumVer;
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            bin = "";
            numRead = 0;
            sumVer = 0;
            foreach (char c in lines[0])
            {
                switch (c)
                {
                    case '0':
                        bin += "0000";
                            break;
                    case '1':
                        bin += "0001";
                        break;
                    case '2':
                        bin += "0010";
                        break;
                    case '3':
                        bin += "0011";
                        break;
                    case '4':
                        bin += "0100";
                        break;
                    case '5':
                        bin += "0101";
                        break;
                    case '6':
                        bin += "0110";
                        break;
                    case '7':
                        bin += "0111";
                        break;
                    case '8':
                        bin += "1000";
                        break;
                    case '9':
                        bin += "1001";
                        break;
                    case 'A':
                        bin += "1010";
                        break;
                    case 'B':
                        bin += "1011";
                        break;
                    case 'C':
                        bin += "1100";
                        break;
                    case 'D':
                        bin += "1101";
                        break;
                    case 'E':
                        bin += "1110";
                        break;
                    case 'F':
                        bin += "1111";
                        break;
                }
            }
            long v = Parse();
            Console.WriteLine(sumVer);
            Console.WriteLine(v);
        }

        private static long Parse()
        {
            int ver = ReadValue(3);
            sumVer += ver;
            int typeID = ReadValue(3);
            switch (typeID)
            {
                case 4:
                    int v;
                    long val = 0;
                    do
                    {
                        v = ReadValue(5);
                        val = val << 4;
                        val += v & 0xF;
                    } while (v >= 16);
                    if (numRead % 4 > 0)
                    {
                        //RemoveZeros(4 - numRead % 4);
                    }
                    return val;
                    break;
                default:
                    int lengthID = ReadValue(1);
                    int length;
                    List<long> values = new List<long>();
                    if (lengthID == 0)
                    {
                        length = ReadValue(15);
                        string save = bin.Substring(length, bin.Length - length);
                        bin = bin.Substring(0, length);
                        while (bin.Length > 0)
                        {
                            values.Add(Parse());
                        }
                        bin = save;
                    }
                    else
                    {
                        length = ReadValue(11);
                        for (int i = 0; i < length; i++)
                            values.Add(Parse());
                    }
                    return Calc(typeID, values);
            }
        }

        private static long Calc(int typeID, List<long> values)
        {
            long val = 0;
            switch (typeID)
            {
                case 0:
                    val = 0;
                    foreach (long v in values)
                        val += v;
                    break;
                case 1:
                    val = 1;
                    foreach (long v in values)
                        val *= v;
                    break;
                case 2:
                    val = Int64.MaxValue;
                    foreach (long v in values)
                        val = Math.Min(v, val);
                    break;
                case 3:
                    val = 0;
                    foreach (long v in values)
                        val = Math.Max(v, val);
                    break;
                case 5:
                    val = 0;
                    if (values[0] > values[1])
                        val = 1;
                    break;
                case 6:
                    val = 0;
                    if (values[0] < values[1])
                        val = 1;
                    break;
                case 7:
                    val = 0;
                    if (values[0] == values[1])
                        val = 1;
                    break;
            }
            return val;
        }

        private static void RemoveZeros(int v)
        {
            bin = bin.Substring(4 - numRead % 4);
            numRead += 4 - numRead % 4;
        }

        private static int ReadValue(int num)
        {
            string v = bin.Substring(0, num);
            bin = bin.Substring(num);
            numRead += num;
            int val = 1 << (v.Length - 1);
            int sum = 0;
            foreach (char c in v)
            {
                if (c == '1')
                    sum += val;
                val = val >> 1;
            }
            return sum;
        }
    }
}
