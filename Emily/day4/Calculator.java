//This is going to be used to create a calculator, on Day#3.
class Calculator {
	public static void main(String[] args) {
		System.out.println("I am a calculator! Type a number for me to add if you want me to show you how much of a genius I am!(evil laugh)");

		int x = Integer.parseInt(System.console().readLine()) ; 
		System.out.println("HAHA, I am a genius, am I not? Now, type another number, and you will again see how much of a genius I am!(evil laugh)");
		int y = Integer.parseInt(System.console().readLine()) ;
		int z = x/y;

		//System.out.println();

		System.out.println("I know that " + x + " / " + y + " = " + z);
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