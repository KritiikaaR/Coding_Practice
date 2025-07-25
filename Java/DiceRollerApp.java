import java.util.Scanner;

// Represents a single die
class Die {
    int sides;  // Number of sides on the die
    int value;  // Current value after rolling
    
    // Default constructor: creates a 6-sided die with initial value 1
    public Die() {
        sides = 6;
        value = 1;    
    }
    
    // Constructor: creates a die with custom number of sides
    public Die(int sides) {
        this.sides = sides;
        value = 1;
    }
    
    // Rolls the die (random value between 1 and sides)
    public void roll() {
        value = (int)(Math.random() * sides) + 1;
    }
    
    // Returns the current value of the die
    public int getValue() {
        return value;
    }
}

// Represents a pair of two dice
class PairOfDice {
    Die d1;  // First die
    Die d2;  // Second die
    
    // Default constructor: creates 2 dice with 6 sides each
    public PairOfDice() {
        d1 = new Die();
        d2 = new Die();
    }
    
    // Constructor: creates 2 dice with custom number of sides
    public PairOfDice(int sides) {
        d1 = new Die(sides);
        d2 = new Die(sides);
    }
    
    // Rolls both dice
    public void roll() {
        d1.roll();
        d2.roll();
    }
    
    // Returns value of the first die
    public int getValue1() {
        return d1.getValue();
    }
    
    // Returns value of the second die
    public int getValue2() {
        return d2.getValue();
    }
    
    // Returns the sum of both dice values
    public int getSum() {
        return d1.getValue() + d2.getValue();
    }
}

// A utility class for validating user input
class Validator {
    // Gets an integer value from the user
    public static int getInt(Scanner sc, String prompt) {
        int i = 0;
        boolean isValid = false;

        while (!isValid) {
            System.out.print(prompt);
            if (sc.hasNextInt()) {
                i = sc.nextInt();
                isValid = true;
            } else {
                System.out.println("Error! Invalid integer value. Try again.");
            }
            sc.nextLine();  // Discard any extra input
        }
        return i;
    }

    // Gets an integer within a specific range
    public static int getIntWithinRange(Scanner sc, String prompt, int min, int max) {
        int i = 0;
        boolean isValid = false;
        
        while (!isValid) {
            i = getInt(sc, prompt);
            if (i <= min)
                System.out.println("Error! Number must be greater than " + min);
            else if (i >= max)
                System.out.println("Error! Number must be less than " + max);
            else
                isValid = true;
        }
        return i;
    }

    // Gets a double value from the user
    public static double getDouble(Scanner sc, String prompt) {
        double d = 0;
        boolean isValid = false;
        while (!isValid) {
            System.out.print(prompt);
            if (sc.hasNextDouble()) {
                d = sc.nextDouble();
                isValid = true;
            } else {
                System.out.println("Error! Invalid decimal value. Try again.");
            }
            sc.nextLine();  // Discard any extra input
        }
        return d;
    }

    // Gets a double within a specific range
    public static double getDoubleWithinRange(Scanner sc, String prompt, double min, double max) {
        double d = 0;
        boolean isValid = false;
        while (!isValid) {
            d = getDouble(sc, prompt);
            if (d <= min)
                System.out.println("Error! Number must be greater than " + min);
            else if (d >= max)
                System.out.println("Error! Number must be less than " + max);
            else
                isValid = true;
        }
        return d;
    }

    // Ensures the user enters a non-empty string
    public static String getRequiredString(Scanner sc, String prompt) {
        String s = "";
        boolean isValid = false;
        while (!isValid) {
            System.out.print(prompt);
            s = sc.nextLine();
            if (s == null || s.equals("")) {
                System.out.println("Error! This entry is required. Try again.");
            } else {
                isValid = true;
            }
        }
        return s;
    }
}

// Main class for the Dice Roller Application
public class DiceRollerApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PairOfDice dice = new PairOfDice(); // Create a pair of dice
        String choice;
        
        // Repeat rolling until user chooses 'n'
        do {
            dice.roll();  // Roll both dice
            int val1 = dice.getValue1();  // Value of first die
            int val2 = dice.getValue2();  // Value of second die
            int sum = dice.getSum();      // Sum of both dice
            
            // Display results
            System.out.println("Dice 1: " + val1);
            System.out.println("Dice 2: " + val2);
            System.out.println("Sum: " + sum);
            
            // Special messages for specific outcomes
            if (val1 == 1 && val2 == 1) {
                System.out.println("Snake Eyes!");
            } else if (val1 == 6 && val2 == 6) {
                System.out.println("Box Cars!");
            } else if (sum == 7) {
                System.out.println("Craps!");
            }
            
            // Ask user if they want to roll again
            choice = Validator.getRequiredString(sc, "Do you want to roll again? (y/n): ");
                
        } while (choice.equalsIgnoreCase("y"));  // Loop until user enters 'n'
        
        sc.close();    
    }
}
