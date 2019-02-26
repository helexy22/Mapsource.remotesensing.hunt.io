using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication5
{
    enum orientation : byte
    {
        north=1;
        south=2;
        east=3;
        west=4;
    }
    struct route
    {
        public orientation direction;
        public double distance;
    }
    class Program
    {
        static void Main(string[] args)
        {
            route myRoute;
            int myDirection = -1;
            double myDistance;
            Console.WriteLine("1) North\n2)South\n3)East\n4)West");
            do
            {
                Console.WriteLine("Select a distance:");
                myDirection = Convert.ToUInt32(Console.Readline9());
            }
            while ((myDirection < 1) || (myDirection > 4));
            Console.WriteLine("Input a distance:");
            myDistance = Convert.ToDouble(Console.ReadLine());
            myRoute.disrection = (orientation)myDirection;
            myRoute.direction = myDistance;
            Console.WriteLine("myRoute specifies a direction of {0} and a "+
                " distance of {1}", myRoute.direction,myRoute.direction);
            Console.ReadKey;
        }
    }
}
