class HelloPerson {
	public static void main(String[] args) {
		System.out.println("Hello there, to use this program correctly, please enter your first name.");

        String x = System.console().readLine();
        System.out.println("Now please enter your last name.");
        String a = System.console().readLine();
        System.out.println("Ahh, I see, your name is " + x + " " + a + ".");
        //Press enter to continue.
        System.out.println("How nice, what do you think my name is though?");
        String z = System.console().readLine();

        System.out.println("HAHA, you didn't guess it, I don't even have a name!");
        
        System.out.println("Hmm... but now thinking about it, it might be nice to have a name after all.");
        System.out.println("What's your suggestion?");
        String w = System.console().readLine();
        System.out.println("Very good, that shall be my name then. I shall be called " + w + " now!");
        
	}
}