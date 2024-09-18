import java.util.ArrayList;

public class Team {
    private String teamName;
    private ArrayList<Player> players;
    private int score;

    public Team(String teamName) {
        this.teamName = teamName;
        this.players = new ArrayList<>();
        this.score = 0;
    }

    public String getTeamName() {
        return teamName;
    }

    public void addPlayer(Player player) {
        players.add(player);
    }

    public ArrayList<Player> getPlayers() {
        return players;
    }

    public void addScore(int points) {
        score += points;
    }

    public int getScore() {
        return score;
    }

    // Get a random player by position
    public Player getRandomPlayer(String position) {
        ArrayList<Player> filteredPlayers = new ArrayList<>();
        for (Player player : players) {
            if (player.getPosition().equalsIgnoreCase(position)) {
                filteredPlayers.add(player);
            }
        }
        if (filteredPlayers.isEmpty()) return null;
        int randomIndex = new Random().nextInt(filteredPlayers.size());
        return filteredPlayers.get(randomIndex);
    }
}
