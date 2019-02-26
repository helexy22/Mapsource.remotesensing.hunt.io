// function overloading
class Program
{
    static int MaxValue(int[] intArray)
    {
        int MaxVal=intArray[0];
        for(inti=1;i<intArray.Length;i++)
        {
            if(intArray[i]>maxVal)
            maxVal=intArray[i];
        }
        return maxVal;
    }
    static void Main(string[] args)
    {
        int[] myArray={1,8,3,6,2,5,9,3,0,2};
        int maxVal=MaxValue(myArray);
        Console.WritleLine("The maximum value in myArray is {0}",maxVal);
        Console.ReadKey();
    }
}
