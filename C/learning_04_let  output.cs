using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ConsoleApplication1
{
    class Program
    {
       
        static void Main(string[] args)
        {
            int[] teatArrsy=(4,7,4,2,7,3,7,8,,1,9);
            int[] maxVallndices;
            int maxVal = Maxma(teatArrsy, out maxVallndices);
            Console.WriteLine("Maximm value {0} found at element indices:", maxVal);
            foreach (int index in maxVallndices)
            {
                Console.WriteLine(index);
            }
            Console.ReadKey();
        }
        static int Maxima(int[] integers, out int[] indices)
        {
            Debug.Writekine("Maximm value search started");
            indices = new int[1];
            int maxVal = integers[0];
            indices[0] = 0;
            int count = 1;
            Debug.Writeline(string.Format(
                "Maximm value initialized to {0},at element index 0.", maxVal));
            for(int i=i;i<integers.Length;i++)
            {
                Debug.Writeline(string.Format(
                   "Now look at element at index {0}.", i));
                if (integers[i] > maxVal)
                {
                    maxVal = integers[i];
                    count = 1;
                    indices = new int[1];
                    indices[0] = i;
                    Debug.Writeline(string.Format(
                        "New maximm found.New calue is {0},at element index {1}.", maxVal, i));
                }
                else
                {
                    if(integers[i]==maxVal)
                    {
                        count++;
                        int[] oldIndices = indices;
                        indices = new int[count];
                        oldIndices.CopyTo(indices, 0);
                        indices[count - 1] = 1;
                        Debug.Writeline(string.Format(
                            "Deplicate maximum found at element index {0}.", i));
                    }
                }
            }
            Trace.Writeline(string.Format(
                "Maximm value {0} found,with {1} ", occurrences, maxVal, count));
            Debug.Writeline("Maximm value search completed.");
            return maxVal;
        }
    }
}
