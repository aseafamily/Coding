import java.text.DecimalFormat;

//This is going to be used to add some stuff to the Calculator, on Day6.
class Calculator {
	public static void main(String[] args) {
		//First number
		System.out.println("I am a calculator! Type the first number you want me to add/subtract/multiply/divide if you want me to show you how much of a genius I am!(evil laugh)");
		double x = Double.parseDouble(System.console().readLine());
		
		//Operator
		System.out.println("Do you not see I am a genius? Now type the operator you want to use, and you will see the true geniusness of me!(+ or - or * or /)");
		String o = System.console().readLine();

		//Second number
		System.out.println("HAHA, I am truly a genius, am I not? Now, type another number, and you will yet again see how much of a genius I am!(evil laugh)");
		double y = Double.parseDouble(System.console().readLine());

		//The answer
		double z = 0;

		//If equations
		if (o.equals("+")) {
			z = x+y;
		}

		if (o.equals("-")) {
			z = x-y;
		}
		
		if (o.equals("*")) {
			z = x*y;
		}

		if (o.equals("/")) {
			z = x/y;
		}

		DecimalFormat df2 = new DecimalFormat("#.###");


		System.out.println("I know that " + x + o + y + " = " + df2.format(z) + "!!!");
		System.out.println("I KNOW EVERYTHING!!!(evil laugh)");


	}
}
//Now we need to actually make a calculator. Remember that after every line we need a semicolon.
//This is the copy for Day4, we are going to make a more complicaated calculator today, at least I think.
//To get to this, you do Code (and then the notepad thingy is called).
//Blue color is reserved color. What does reserved color mean though?
//Not everything is in one color, and the best thing about this app is that if you put your mouse on one curly braket, it will show you the matching one. Same with parenthesis.
//There's also intellisense, so we don't have to remember everything. There's code on a coding app! Intellisense is really important.
//Light blue means variable. So args, is a variable. And is x, y, and z.