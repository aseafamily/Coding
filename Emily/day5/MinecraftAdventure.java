class MinecraftAdventure {
	public static void main(String[] args) {
        //Your name
        System.out.println("Hello there, and welcome to the Minecraft Adventure. Please enter your character's name, it doesn't thave to be your own.");
        String x = System.console().readLine();
        
        //Greetings
        System.out.println("Hello " + x + "! Press enter to continue.");
        String a = System.console().readLine();
        
        //Spawning/meeting the evil villager
        System.out.println("You spawn in the middle of the desert, and see a village nearby. You start to run towards it. When you get closer, a villager approaches you.");
        System.out.println("For some reason, it's eyes are red. Hello, it says, Give me your name and you may enter this village.");
        System.out.println("You decide that following the villager's directions seems like a pretty good choice. But... you don't have to give it your real name do you?");
        System.out.println("Enter your name:");
        String z = System.console().readLine();

        //Meeting the other villagers
        System.out.println("Greetings, " + z + " the villager says, follow me.");
        System.out.println("The villager leads you to a large house, but it's unlike any village house you've ever seen. It's made out of iron blocks, and there are metal bars instead of windows.");
        System.out.println("Inside, there are other villagers. The villager that you met introduces you to them.");
        System.out.println("This is " + z + ", it says.");
        System.out.println("It turns to you, and says, And these are the other villagers " + z + ".");
        System.out.println("Greetings " + z + ", the other villagers say, welcome to our village.");
        
        //Code Name
        System.out.println("To become a member of this village, one of the villagers say, You need to have a code name. What will be yours?");
        System.out.println("You decide that you will play along. Enter your code name.");
        String c = System.console().readLine();
        
        // Meeting the leader
        System.out.println("You are now a member of this village " + z + ", the villager says, Your code name is " + c + ", remember that.");
        System.out.println("The villagers come to a silent agreement after a moments of pause, and the one who asked for your code name stands up.");
        System.out.println("It gestures for you to follow it, and leads you to a room. In the center, is a man in black.");
        
	}
}