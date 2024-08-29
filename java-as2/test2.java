public class test2 {
    import java.uitl.Scanner;

public class Connections{
    private Player player;
    private Grid grid;
    private int unsuccessfulAttempts;
    private InputClass inputClass;
    public int attempts;

     // default constructor

    /*
    default constsructor
    */
    public Connections(){
        this.attempts = 0;
        this.grid = null;
        this.Player = new Player();
        this.attempt = 5;
        this.unsuccessfulAttempts = 0;
        this.inputClass = new InputClass();
        this.grid = null;
    }

    /*
    Non- default constructor
    */
    public Connections(Player player, Grid grid){
        this.attempts = 0;
        this.Player = new Player();
        this.attempt = 5;
        this.unsuccessfulAttempts = 0;
        this.inputClass = new InputClass();
        this.grid = grid;

    }
    
    /*
    main game programm
    */
    public void startGame(){
         //print the welcome message
        System.out.println("Welcome to the java Connection game");
        
        //check if there's a player to invoid collision
        if (player.getName().equals("Unknown")){
            //create player
            String playerName = inputClass.getPlayername();
            player.setName(playerName);
        }

        //display the themes
        String[] themes = WordGroup.getThemes();
        System.out.println("Themes: ");
        for (String theme : themes){
            System.out.println("- " + theme);
        }

        //Generate the grid and display if it's not set
        if (grid == null){
            String[] girdWords = WordGroup.generateGroup();
            grid = new Grid(girdWords);
        }
        // display grid
        grid.displayGrid();

        // let user start guessing, stops when 5 attempts are all used
        while(attempts >= 0 && !girdIsEmpty()){
            playRound();
        }

        // end the game
        System.out.print("Do you want to play another game? (yes/no): ");

        String answer = inputClass.getScanner().nextLine();
        if (answer == "yes" || answer == "YES"){
            resetGame();
            startGame();
            }
        }

    /*
    method for each round 
    */
    public void playRound(Scanner scanner){
        //ask the user to input 3 words(guess)
        String[] guessedWord = inputClass.getGuessWords();

        //check connections
        if (!theme.equals("no nonnection")){
            // correct guess
            System.out.println("Correct! The theme is: " + theme);
            grid.removeWords(guessedWord);
        }else{
            System.out.println("No connection.");
            unsuccessfulAttempts++;
        }
        attempts--;
    }
    /*
    method for reset the game
    */
    private void resetGame()
    {
        this.attempts = 0;
        unsuccessfulAttempts = 5;
        this.grid = null;
    }


    
    //main method
    public static void main(String[] args)
    {
        //Game starter
        new Connections().startGame();//use the constructer to start the game
    }
    
   
    
}
}
