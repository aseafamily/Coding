import java.util.Random;

class GuessNumber {
    public static void main(String[] args) {
        System.out.println("Guess a number.(0-100)");
        Random r = new Random();
        int mySecretNumber = r.nextInt(100);
        int count = 0;
        
        while (true) {
        
            int guessNumber = Integer.parseInt(System.console().readLine());
            count++;
            if (guessNumber > mySecretNumber) {
                System.out.println("Your guess is larger than mine.");
            } else if (guessNumber < mySecretNumber) {
                System.out.println("Your guess is smaller than mine.");
            } else {
                System.out.println("You guessed the number.");
                System.out.println("Your number of tries is " + count + ".");
                break;
            }
            System.out.println("Your number of tries is " + count + ".");
        }
    
            
    }
}
