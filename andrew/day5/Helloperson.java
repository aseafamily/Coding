class Helloperson {
	public static void main(String[] agrs) {
        System.out.println("What is your first name?");
        String x = System.console().readLine();
        System.out.println("What is your last name?");
        String y = System.console().readLine();
		System.out.println("I know your name is "+ x + " " + y);
	}
}