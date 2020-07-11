public class AdventureStory {
    public static void main(String[] args) {
        //Choosing name
        System.out.println("Welcome to the Adventure Story, please enter your name.");
        String n = System.console().readLine();

        //Choosing character
        System.out.println("Hello " + n + "! Now choose what character you would like to be.");
        System.out.println("The choices are:");
        System.out.println(AdventureStory.GetName(1) + "(1) - A famous future-teller, who works for King Aires, and always worries about her public image.");
        System.out.println(AdventureStory.GetName(2) + "(2) - " + AdventureStory.GetName(1) + "'s son, a new apprentice who's talent isn't quite at it's peak yet.");
        System.out.println(AdventureStory.GetName(3) + "(3) - An orphan, who seems to have a successful life ahead.");
        System.out.println(AdventureStory.GetName(4) + "(4) - Who despite his privelleged past is struggling with the demands of his work.");
        int c = Integer.parseInt(System.console().readLine());
        System.out.println("You chose " + AdventureStory.GetName(c) + ". Press enter to continue.");
    }

    private static String GetName(int c)
    {
        String cname = "";

        if (c == 1) {
            cname = "Oracle";
        }

        if (c == 2) {
            cname = "Tyhnim";
        }

        if (c == 3) {
            cname = "Ellena";
        }

        if (c == 4) {
            cname = "Quin";
        }
        
        return cname;

    }
}