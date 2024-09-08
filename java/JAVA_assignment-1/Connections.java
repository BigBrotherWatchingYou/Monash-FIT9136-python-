public class Connections {
    private Player player; 
    private Grid grid; 
    private int attempts; 
    private int unsuccessfulAttempts;
    private InputClass inputClass; 

    // Default constructor
    public Connections() {
        this.player = new Player(); // Initializes with a default player
        this.grid = null; // Grid will be initialized later
        this.attempts = 5; // Player has 5 attempts to guess correctly
        this.unsuccessfulAttempts = 0; // No unsuccessful attempts initially
        this.inputClass = new InputClass(); // Initialize input handler
    }

    // Non-default constructor
    public Connections(Player player, Grid grid) {
        this.player = player; // Initializes with a provided player
        this.grid = grid; // Initializes with a provided grid
        this.attempts = 5; // Player has 5 attempts to guess correctly
        this.unsuccessfulAttempts = 0; // No unsuccessful attempts initially
        this.inputClass = new InputClass(); // Initialize input handler
    }

    // Method to start the game
    public void startGame() {
        // Display welcome message
        System.out.println("Welcome to Java Connections!");

        // Request player's name if not set
        if (player.getName().equals("Unknown")) {
            String playerName = inputClass.getPlayerName(); // Get a valid player name
            player.setName(playerName); // Set the player's name
        }

        // Display the themes available in the game
        String[] themes = WordGroup.getThemes();
        System.out.println("Themes:");
        for (String theme : themes) {
            System.out.println("- " + theme);
        }

        // Generate and display the grid of words if it hasn't been set yet
        if (grid == null) {
            String[] gridWords = WordGroup.generateGroup(); // Generate a random set of words
            grid = new Grid(gridWords); // Initialize the grid with these words
        }
        grid.displayGrid(); // Display the grid to the player

        // Main game loop: continue until no attempts are left or the grid is empty
        while (attempts > 0 && !gridIsEmpty()) {
            playRound(); // Let the player make a guess
        }

        // Game over: Display the player's score
        System.out.println("Game Over! Your score: " + calculateScore());



        // Ask if the player wants to play another game
        System.out.print("Do you want to play another game? (yes/no): ");
        String answer = inputClass.getScanner().nextLine();
        if (answer.equalsIgnoreCase("yes")) {
            resetGame(); // Reset the game state for a new game
            startGame(); // Start a new game
        } else {
            // Display the player's highest score and exit the game
            System.out.println("Your highest score was: " + player.getHighestScore());
            System.out.println("Thanks for playing!");
        }
    }

    // Method to handle a single round of the game
    private void playRound() {
        // Request the player to enter 3 connected words
        String[] guessedWords = inputClass.getGuessedWords(grid.getWords());

        // Check if the words are connected using the WordGroup class
        String theme = WordGroup.checkConnections(guessedWords);

        if (!theme.equals("no connection")) {
            // If the words are correctly connected
            System.out.println("Correct! The theme is: " + theme);
            grid.removeWords(guessedWords); // Remove the guessed words from the grid
        } else {
            // If the words are not connected
            System.out.println("No connection.");
            unsuccessfulAttempts++; // Increase the count of incorrect guesses
            if (unsuccessfulAttempts >= 5) {
                attempts = 0; // End the game after one unsuccessful attempt
            }
        }
        attempts--; // Decrease the number of remaining attempts
    }

    // Method to calculate the player's score
    private int calculateScore() {
        // Calculate score based on correct and incorrect attempts
        return (5 - attempts) * 2 - unsuccessfulAttempts;
    }

    // Method to check if the grid is empty
    private boolean gridIsEmpty() {
        // Returns true if there are no more words left in the grid
        return grid.isEmpty();
    }

    // Method to reset the game state for a new game
    private void resetGame() {
        this.attempts = 5; // Reset the number of attempts
        this.unsuccessfulAttempts = 0; // Reset the number of incorrect guesses
        this.grid = null; // Reset the grid (a new one will be generated)
    }

    // Main method to start the program
    public static void main(String[] args) {
        new Connections().startGame(); // Start the game using the default constructor
    }
}