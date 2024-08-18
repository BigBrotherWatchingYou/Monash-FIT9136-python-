import java.util.Arrays;
import java.util.Scanner;

class Player {
    private String name;
    private int highestScore;

    // Default constructor
    public Player() {
        this.name = "Unknown";
        this.highestScore = 0;
    }

    // Non-default constructor
    public Player(String name) {
        setName(name);
        this.highestScore = 0;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Setter for name with validation
    public void setName(String name) {
        if (name.matches("^[A-Za-z]{4,8}$")) {
            this.name = name;
        } else {
            throw new IllegalArgumentException("Name must be 4 to 8 alphabetic characters.");
        }
    }

    // Getter for highestScore
    public int getHighestScore() {
        return highestScore;
    }

    // Setter for highestScore
    public void setHighestScore(int score) {
        if (score > highestScore) {
            this.highestScore = score;
        }
    }

    // Return the state of the Player as a String
    public String toString() {
        return "Player: " + name + ", Highest Score: " + highestScore;
    }
}

class Grid {
    private String[] words;

    // Constructor
    public Grid(String[] words) {
        this.words = words;
    }

    // Display the grid
    public void displayGrid() {
        for (int i = 0; i < words.length; i++) {
            System.out.print(words[i] + "\t");
            if ((i + 1) % 3 == 0) {
                System.out.println();
            }
        }
    }

    // Check if a word is in the grid
    public boolean containsWord(String word) {
        return Arrays.asList(words).contains(word);
    }
}

public class Connections {
    private Player player;
    private Grid grid;

    // Main method to start the program
    public static void main(String[] args) {
        Connections game = new Connections();
        game.startGame();
    }

    // Start the game
    public void startGame() {
        Scanner scanner = new Scanner(System.in);

        // Welcome message and player name input
        System.out.println("Welcome to Java Connections!");
        System.out.print("Please enter your name: ");
        String playerName = scanner.nextLine();

        try {
            player = new Player(playerName);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
            return;
        }

        // Display themes and generate word grid
        String[] themes = WordGroup.getThemes();
        System.out.println("Themes: " + String.join(", ", themes));

        String[] wordGroup = WordGroup.generateGroup();
        grid = new Grid(wordGroup);
        grid.displayGrid();

        // Game loop
        int attempts = 0;
        int correctAttempts = 0;
        boolean gameOver = false;

        while (attempts < 5 && !gameOver) {
            System.out.print("Enter 3 connected words separated by spaces: ");
            String[] inputWords = scanner.nextLine().split(" ");

            if (inputWords.length != 3 || !grid.containsWord(inputWords[0]) || !grid.containsWord(inputWords[1]) || !grid.containsWord(inputWords[2])) {
                System.out.println("Invalid input. Please enter 3 words from the grid.");
                continue;
            }

            String connection = WordGroup.checkConnections(inputWords);
            if (!connection.equals("no connection")) {
                System.out.println("Correct! The connection is: " + connection);
                correctAttempts++;
                // Remove the connected words from the grid and display the remaining words
                wordGroup = Arrays.stream(wordGroup).filter(word -> !Arrays.asList(inputWords).contains(word)).toArray(String[]::new);
                grid = new Grid(wordGroup);
                grid.displayGrid();
                if (wordGroup.length == 0) {
                    gameOver = true;
                }
            } else {
                System.out.println("No connection. Try again.");
                attempts++;
                if (attempts == 5) {
                    System.out.println("Game Over!");
                    gameOver = true;
                }
            }
        }

        int score = (correctAttempts * 2) - (attempts - correctAttempts);
        player.setHighestScore(score);
        System.out.println("Your score: " + score);
        System.out.println(player.toString());

        // Option to play another game
        System.out.print("Would you like to play another game? (yes/no): ");
        String playAgain = scanner.nextLine();
        if (playAgain.equalsIgnoreCase("yes")) {
            startGame();
        } else {
            System.out.println("Thanks for playing! Your highest score was: " + player.getHighestScore());
        }

        scanner.close();
    }
}

// Assuming the WordGroup class is provided by your instructor or environment.
class WordGroup {
    // Mock implementation for testing purposes
    public static String[] getThemes() {
        return new String[]{"Access Modifiers", "Relational Operators", "Logical Operators", "Data Types"};
    }

    public static String[] generateGroup() {
        return new String[]{"private", "protected", "public", "<=", ">=", "==", "&&", "||", "!", "int", "float", "double"};
    }

    public static String checkConnections(String[] words) {
        if (Arrays.asList(words).containsAll(Arrays.asList("private", "protected", "public"))) {
            return "Access Modifiers";
        }
        if (Arrays.asList(words).containsAll(Arrays.asList("<=", ">=", "=="))) {
            return "Relational Operators";
        }
        if (Arrays.asList(words).containsAll(Arrays.asList("&&", "||", "!"))) {
            return "Logical Operators";
        }
        if (Arrays.asList(words).containsAll(Arrays.asList("int", "float", "double"))) {
            return "Data Types";
        }
        return "no connection";
    }
}