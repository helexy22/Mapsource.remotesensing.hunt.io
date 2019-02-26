class Program
{
	delegate double ProcessDelegate(double param1,double param2);  //使用委托来调用函数
	static double Multiply(double param1,double param2)
	{
		return param1*param2;
	}
	static double Divide(double param1,double param2)
	{
		return param1/param2;
	}
	static void Main(string[] args)
	{
		ProcessDelegate process;
		Console.WriteLine("Enter 2 numbers separated with a comma:");
		string input=Console.Readline();
		int commaPos=input.IndexOf(',');
		double param1=Convert.ToDouble(input.Substring{0,commaPos});
		double param2=Convert.ToDouble(input.Substring{commaPos+1,
		input.Langth-commaPos-1});
		Console.WriteLine("Enter M to multiply or D to divide");
		input=Console.Readline();
		if(input="M")
			Process=new processDelegata(Multiply);
		else
			process=new processDelegata(Divide);
		Console.WriteLine("Result:{0}",process(param1 param2));
		Console.ReadKey();
	}
	
	///这段代码定义了一个委托Processdelegate，其返回类型和参数与函数 Multiply和Divided配。委托的定义如下所示：
       delegate double Processdelegate(double paraml，double param2)；

     delegate关键字指定该定义是用于委托的，而不是用于函数的（该定义所在的位置与函数定义相同）。接着，该定义指定 double返回类型和两个double参数。实际使用的名称可以是任意的，所以可以给委托类型和参数指定任意名称。这里委托名是 ProcessDelegate，double参数名是 param１和param2.
	Main中的代码首先使用新的委托类型声明一个变量：
	static void Main(string[]args)
	{
		Processdelegate process;
	}

	接着用些比较标准的C#代码请求由逗号分隔的两个数字，并把这些数字放在两个 double变量中：

	Console，Writeline（"Enter 2 numbers separated with a comma:");
	string input=Console.Readline();
	int commaPos=input.IndexOf(',');
	double parami=Convert.Todouble(input Substring(0;commaPos});
	double param2=Convert.Todouble(input Substring{commaPos +1，input Length--commaPos--1})：
	///
}
