import java.util.Scanner;

public class Connections {
    private Player player;
    private Grid grid;
    private int attempts;
    private int correctAttempts;
    private int unsuccessfulAttempts;

    public Connections() {
        this.attempts = 5;
        this.correctAttempts = 0;
        this.unsuccessfulAttempts = 0;
    }

    public void startGame() {
        Scanner scanner = new Scanner(System.in);

        // Display welcome message
        System.out.println("Welcome to Java Connections!");

        // Request player's name
        System.out.print("Enter your name: ");
        String playerName = scanner.nextLine();
        while (!isValidName(playerName)) {
            System.out.print("Invalid name. Please enter a valid name: ");
            playerName = scanner.nextLine();
        }
        player = new Player(playerName);

        // Display the themes
        String[] themes = WordGroup.getThemes();
        System.out.println("Themes:");
        for (String theme : themes) {
            System.out.println("- " + theme);
        }

        // Start the game loop
        while (attempts > 0) {
            playRound(scanner);
            if (gridIsEmpty()) {
                break;
            }
        }

        // Display game score
        int gameScore = (correctAttempts * 2) - unsuccessfulAttempts;
        System.out.println("Game Over! Your score: " + gameScore);

        // Update player's highest score
        player.setHighestScore(gameScore);

        // Ask if the player wants to play another game
        System.out.print("Do you want to play another game? (yes/no): ");
        String answer = scanner.nextLine();
        if (answer.equalsIgnoreCase("yes")) {
            startGame();
        } else {
            System.out.println("Your highest score was: " + player.getHighestScore());
            System.out.println("Thanks for playing!");
        }

        scanner.close();
    }

    private void playRound(Scanner scanner) {
        String[] gridWords = WordGroup.generateGroup();
        grid = new Grid(gridWords);

        // Display the grid
        grid.displayGrid();

        // Request the player to enter 3 connected words
        System.out.print("Enter 3 words separated by spaces: ");
        String[] guessedWords = scanner.nextLine().split(" ");
        while (!areValidWords(guessedWords)) {
            System.out.print("Invalid words. Please enter 3 valid words: ");
            guessedWords = scanner.nextLine().split(" ");
        }

        // Check if the words are connected
        String theme = WordGroup.checkConnections(guessedWords);
        if (!theme.equals("no connection")) {
            System.out.println("Correct! The theme is: " + theme);
            grid.removeWords(guessedWords);
            correctAttempts++;
        } else {
            System.out.println("No connection. Try again.");
            unsuccessfulAttempts++;
            if (unsuccessfulAttempts >= 1) {
                attempts = 0;
            }
        }
        attempts--;
    }

    private boolean areValidWords(String[] guessedWords) {
        if (guessedWords.length != 3) return false;
        for (String word : guessedWords) {
            if (!grid.isInGrid(word)) {
                return false;
            }
        }
        return true;
    }

    private boolean isValidName(String name) {
        return name != null && name.matches("[a-zA-Z]{4,8}");
    }

    private boolean gridIsEmpty() {
        return grid == null || grid.words.length == 0;
    }

    public static void main(String[] args) {
        new Connections().startGame();
    }
}