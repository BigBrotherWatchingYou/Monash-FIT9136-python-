import java.io.*;
import java.util.*;

public class AFLGame {
    private Team teamA;
    private Team teamB;
    private Random random;

    public AFLGame(Team teamA, Team teamB) {
        this.teamA = teamA;
        this.teamB = teamB;
        this.random = new Random();
    }

    public void startGame() {
        for (int quarter = 1; quarter <= 4; quarter++) {
            System.out.println("Starting Quarter " + quarter);
            playQuarter();
            System.out.println("Score after Quarter " + quarter + ":");
            displayScores();
        }

        determineWinner();
    }

    private void playQuarter() {
        for (int event = 0; event < 80; event++) {
            simulateEvent();
        }
    }

    private void simulateEvent() {
        Player playerWithBall = teamA.getRandomPlayer("midfielder"); // Starting from midfielder for simplicity
        if (playerWithBall == null) return;

        playerWithBall.increaseKicks();
        int eventOutcome = random.nextInt(100); // Generate random event outcome

        if (eventOutcome < 5) {
            // Player kicks a goal
            playerWithBall.increaseGoals();
            teamA.addScore(6);
            System.out.println(playerWithBall.getName() + " kicked a goal!");
        } else if (eventOutcome < 15) {
            // Player kicks a behind
            playerWithBall.increaseBehinds();
            teamA.addScore(1);
            System.out.println(playerWithBall.getName() + " kicked a behind!");
        } else {
            // Ball passes or turnover
            System.out.println(playerWithBall.getName() + " passed the ball.");
        }
    }

    private void displayScores() {
        System.out.println(teamA.getTeamName() + ": " + teamA.getScore() + " points");
        System.out.println(teamB.getTeamName() + ": " + teamB.getScore() + " points");
    }

    private void determineWinner() {
        if (teamA.getScore() > teamB.getScore()) {
            System.out.println(teamA.getTeamName() + " wins!");
        } else if (teamB.getScore() > teamA.getScore()) {
            System.out.println(teamB.getTeamName() + " wins!");
        } else {
            System.out.println("The game is a draw.");
        }
    }

    public static Team loadTeamFromFile(String fileName) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(fileName));
        String teamName = reader.readLine();
        Team team = new Team(teamName);

        String line;
        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(",");
            String playerName = parts[0].trim();
            String position = parts[1].trim();
            int seasonGoals = Integer.parseInt(parts[2].trim());

            Player player = new Player(playerName, position, seasonGoals);
            team.addPlayer(player);
        }

        reader.close();
        return team;
    }

    public static void main(String[] args) {
        try {
            Team teamA = loadTeamFromFile("teamA.txt");
            Team teamB = loadTeamFromFile("teamB.txt");

            AFLGame game = new AFLGame(teamA, teamB);
            game.startGame();
        } catch (IOException e) {
            System.out.println("Error reading team files: " + e.getMessage());
        }
    }
}
