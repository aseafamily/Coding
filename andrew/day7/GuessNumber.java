import java.util.Random;
class GuessNumber {
    public static void main(String[] args) {
        System.out.println("Guess a number (0-1000).");
        Random r = new Random();
        int mySecretNumber = r.nextInt(1000);
        int count = 0;
        
        

        while (true) {
            int x = Integer.parseInt(System.console().readLine());
            count++;
            System.out.println("Your number of tries so far " + count);
            if (x > mySecretNumber) {
                System.out.println("Your number is bigger then mine.");
            } else if (x < mySecretNumber) {
                System.out.println("Your number is smaller then mine.");
            }else{
                System.out.println("You have my secert number!");
                break;
            }
        }
        
        
    }
        
}