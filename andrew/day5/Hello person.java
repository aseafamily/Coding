class Calculator {
	public static void main(String[] agrs) {
        System.out.println("What is your name?")
		System.out.println("I am a calculator! Please type a number:");
		int x = Integer.parseInt(System.console().readLine());

		System.out.println("Please type amother number");
		int y = Integer.parseInt(System.console().readLine());
		int z = x * y;

		//System.out.println();

		
		System.out.println("I know the answer of " + x + " x " + y + " = " +z);
		System.out.println("(Evil laugh)");
	}
}